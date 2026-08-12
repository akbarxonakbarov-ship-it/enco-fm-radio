from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    telegram_file_id: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    telegram_file_unique_id: Mapped[str | None] = mapped_column(String(255))

    title: Mapped[str | None] = mapped_column(String(500))
    artist: Mapped[str | None] = mapped_column(String(500))
    album: Mapped[str | None] = mapped_column(String(500))
    filename: Mapped[str | None] = mapped_column(String(1000))

    duration: Mapped[int | None] = mapped_column(Integer)
    file_size: Mapped[int | None] = mapped_column(BigInteger)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    play_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
