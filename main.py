from core.password_manager import PasswordManager
from gui.login_window import LoginWindow


def main():
    manager = PasswordManager()
    LoginWindow(manager).run()


if __name__ == "__main__":
    main()
