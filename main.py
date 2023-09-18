from pyrogram import Client, idle, types, filters

import config
import dep_config as config

bot = Client(
    name=config.APP_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@bot.on_message()
def process_message(client: Client, message: types.Message) -> None:
    print("received")
    if message.web_app_data:
        print(message.web_app_data)

if __name__ == "__main__":

    print(f"Starting {config.APP_NAME}")
    try:
        bot.start()
        bot.send_message(
            chat_id=247189896, 
            text="Ci sono!", 
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[types.InlineKeyboardButton(
                    text="Avvia Web App",
                    web_app=types.WebAppInfo(url="https://qwertywasd029.github.io/TelegramWebAppTest")
                )]]
            )
        )
        idle()
        bot.stop()
    except KeyboardInterrupt:
        pass
    print(f"Stopping {config.APP_NAME}")