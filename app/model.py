from datetime import datetime
from sqlalchemy import String, func, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...

class PetFeeding(Base):
    __tablename__ = 'PetFeeding'

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_name: Mapped[str] = mapped_column(String(30),nullable=False)
    person_name: Mapped[str]
    amount_servings: Mapped[float] = mapped_column(
        CheckConstraint('amount_serving > 0')
        )
    time_feeding: Mapped[datetime] = mapped_column(server_default=func.now())

    

 