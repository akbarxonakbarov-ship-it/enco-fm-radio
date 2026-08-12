# Enco FM Radio

Telegram 24/7 radio system.

## Components

- `database-bot` — private admin/database bot
- `autodj` — future 24/7 streaming worker
- PostgreSQL — track/playlist/history storage

## Current milestone

Database bot accepts audio files from the configured admin and stores Telegram file metadata in PostgreSQL.

## Setup

1. Copy `.env.example` to `.env`
2. Fill `BOT_TOKEN` and `ADMIN_USER_ID`
3. Run:

```bash
docker compose up --build
```

## Important

Never commit `.env`, Telegram bot tokens, API credentials, or Telegram session strings.
