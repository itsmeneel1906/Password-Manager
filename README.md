# SecureVault Password Manager

A local desktop password manager built with Python and Tkinter. Credentials are encrypted at rest in SQLite with a key derived from your master password using Argon2id. The master password is never stored.

## Requirements

- Python 3.10 or later
- `pip install -r requirements.txt`

## Run

From this folder, run `python main.py`. On first launch, create a strong master password. Select **Suggest** to fill in a random password generated on your device; it is optional and you can edit the suggestion or enter your own. Save the recovery code shown after vault creation somewhere safe. If you forget the master password, select **Forgot master password?** and use that code to set a new one. The recovery code is shown only once. Unlock your vault on later launches. Use the toolbar to add, edit, search, copy, generate, and delete credentials. Clipboard contents are cleared after 30 seconds where the platform supports it.

The database is created automatically under `data/passwords.db`. Use **Vault → Create encrypted backup** to make a portable encrypted backup. Store backups somewhere safe; backup files are not automatically synchronized.

## Security notes

- Passwords and other credential fields are encrypted with Fernet (AES-128-CBC plus HMAC-SHA256) using a random vault key. That key is wrapped using keys derived with Argon2id from the master password and the recovery code.
- SQLite contains encrypted values only. The master password is not persisted.
- Keep a separate backup, remember your master password, and store your recovery code securely. A forgotten master password can only be reset with the recovery code. Deleting the database or losing both secrets loses access to the vault.
- This is a local single-user application, not an audited security product. Protect your operating system account and avoid using it on a compromised device.

## Project layout

`core/` contains vault, authentication, encryption, and generation logic; `database/` handles SQLite; `gui/` provides the desktop interface; `models/` and `utils/` provide data types and helpers; `tests/` covers core behavior. Database and backup files live in `data/` and are excluded from version control.

## Development

Run the test suite with `python -m pytest`. The application uses only Python's standard library and `cryptography` (Argon2id support is required).
