from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import select

from app.config import settings
from app.database.models import Track
from app.database.session import SessionLocal

router = Router()


def is_admin(message: Message) -> bool:
    return message.from_user is not None and message.from_user.id == settings.admin_user_id


@router.message(CommandStart())
async def start(message: Message) -> None:
    if not is_admin(message):
        await message.answer("⛔ Access denied.")
        return

    await message.answer(
        "📻 Enco FM — Database Bot\n\n"
        "Audio fayl yuboring. Men uni music library'ga saqlayman."
    )


@router.message()
async def receive_audio(message: Message) -> None:
    if not is_admin(message):
        await message.answer("⛔ Access denied.")
        return

    if not message.audio:
        await message.answer("🎵 Iltimos, audio fayl yuboring.")
        return

    audio = message.audio

    async with SessionLocal() as session:
        existing = await session.scalar(
            select(Track).where(Track.telegram_file_id == audio.file_id)
        )

        if existing:
            await message.answer(f"ℹ️ Bu audio allaqachon mavjud: Track #{existing.id}")
            return

        track = Track(
            telegram_file_id=audio.file_id,
            telegram_file_unique_id=audio.file_unique_id,
            title=audio.title,
            artist=audio.performer,
            album=audio.album,
            filename=audio.file_name,
            duration=audio.duration,
            file_size=audio.file_size,
        )

        session.add(track)
        await session.commit()
        await session.refresh(track)

    title = audio.title or audio.file_name or "Unknown"
    artist = audio.performer or "Unknown"

    await message.answer(
        f"✅ AUDIO ADDED\n\n"
        f"🆔 Track: #{track.id}\n"
        f"🎵 {title}\n"
        f"👤 {artist}\n"
        f"⏱ {audio.duration or 0} sec"
    )
