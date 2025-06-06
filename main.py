from telethon.sync import TelegramClient
from decouple import config


bot = TelegramClient(
    config('LOGIN'),
    api_id=int(config('API_ID')),
    api_hash=config('API_HASH'),
)

bot.start()

with open('channels.txt', 'r', encoding='utf-8') as f:
    channel_usernames = [line.strip() for line in f if line.strip()]


for channel_username in channel_usernames:
    try:
        entity = bot.get_entity(channel_username)
        messages = bot.get_messages(entity, limit=100)
        print(f"Последние 100 сообщений из канала {channel_username}:")
        for msg in messages:
            if msg.message:
                bot.forward_messages('me', msg)
    except Exception as e:
        print(f"Не удалось получить сообщения из канала {channel_username}: {e}")
