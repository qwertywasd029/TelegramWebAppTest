from pyrogram import Client

import config
import dep_config as config

bot = Client(
    name=config.APP_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

if __name__ == "__main__":

    print(f"Starting {config.APP_NAME}")
    try:
        bot.start()
        bot.send_message(chat_id=247189896, text="Ci sono!")
        bot.stop()
    except KeyboardInterrupt:
        pass
    print(f"Stopping {config.APP_NAME}")