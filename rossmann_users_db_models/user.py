from datetime import datetime, timezone

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from rossmann_users_db_models import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    registration_datetime_utc: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc)
    )
