from database import Base, PKint, unique_str
from sqlalchemy import text, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated


more_than_user = Annotated[bool, mapped_column(default=False, 
                                         server_default=text('false'), 
                                         nullable=False)]


class User(Base):
    id: Mapped[PKint]
    phone_number: Mapped[unique_str]
    first_name: Mapped[str] = mapped_column(String(32), nullable=False)
    last_name: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[unique_str]
    password: Mapped[str]

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[more_than_user]
    is_super_admin: Mapped[more_than_user]