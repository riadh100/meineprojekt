"""
Erstellt einen Administrator
für Yasin AI.
"""

import getpass

from app.database.session import (
    SessionLocal,
)

from app.models.user import User

from app.yasin.utils.yasin_security_utils import (
    sha256,
)


def create_admin():

    db = SessionLocal()

    try:

        print("=" * 60)
        print("YASIN AI ADMIN SETUP")
        print("=" * 60)

        username = input(
            "Benutzername: "
        )

        email = input(
            "E-Mail: "
        )

        password = getpass.getpass(
            "Passwort: "
        )

        exists = (
            db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )

        if exists:

            print(
                "Administrator existiert bereits."
            )

            return

        admin = User(

            username=username,

            email=email,

            password_hash=sha256(
                password
            ),

            role="ADMIN",

            is_active=True,

            is_superuser=True,

        )

        db.add(admin)

        db.commit()

        print()

        print(
            "Administrator erfolgreich erstellt."
        )

    finally:

        db.close()


if __name__ == "__main__":

    create_admin()
