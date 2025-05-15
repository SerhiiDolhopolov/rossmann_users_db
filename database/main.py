from database.db import init_db, get_db
from database.services.user_service import create_user

from users_db_models import User


def main():
    init_db()
    db = next(get_db())
    try:
        if db.query(User).first():
            return
        create_user(db, 'Daenerys', 'Targaryen')
        create_user(db, 'Viserys', 'Targaryen')
        create_user(db, 'Rhaegar', 'Targaryen')
        create_user(db, 'Balon', 'Greyjoy')
        create_user(db, 'Theon', 'Greyjoy')
        create_user(db, 'Yara', 'Greyjoy')
    finally:
        db.close()


if __name__ == "__main__":
    main()
