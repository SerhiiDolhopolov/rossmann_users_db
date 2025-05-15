from sqlalchemy.orm import Session

from users_db_models import User


def create_user(db: Session, 
                first_name: str, 
                last_name: str) -> User:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    password = 'password'
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user