from telegram.ext import ApplicationBuilder, CommandHandler
import requests
from dotenv import load_dotenv
import os
load_dotenv()



CHAT_ID = os.getenv("CHAT_ID")

SECRET_KEY = os.getenv("SECRET_KEY")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()



async def start(update, context):
    await update.message.reply_text("👋 Welcome to the Bot!\nYou can update your social links using these commands:\n✅ /set_telegram <your Telegram URL>\n➡️ Example: /set_telegram https://t.me/yourchannel\n\n✅ /set_instagram <your Instagram URL>\n➡️ Example: /set_instagram https://instagram.com/yourprofile\n\nMake sure to include the full link (starting with https://)\n\nNeed help? Just type /help at any time.")

async def set_instagram(update, context):
    if update.effective_chat.id == CHAT_ID:
        all_args = context.args
        if update.message:
            if len(all_args) != 1:
                await update.message.reply_text("please provide 1 url as input")
                return


            response = requests.post("http://localhost:5050/update", json={
                "instagram": all_args[0],
                "key": SECRET_KEY,
                "telegram": None
            })
            
            await update.message.reply_text(f"✅ Instagram link set successfully to {all_args[0]}")
    else:
        await update.message.reply_text("🚫 This command can only be used in the authorized chat.")

async def set_telegram(update, context):
    if update.effective_chat.id == CHAT_ID:
        all_args = context.args
        
        if update.message:

            if len(all_args) != 1:
                await update.message.reply_text("please provide 1 url as input")
                return


            response = requests.post("http://localhost:5050/update", json={
                "telegram": all_args[0],
                "key": SECRET_KEY,
                "instagram": None
            })

            await update.message.reply_text(f"✅ Telegram link set successfully to {all_args[0]}")
    else:
        await update.message.reply_text("🚫 This command can only be used in the authorized chat.")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", start))
app.add_handler(CommandHandler("set_instagram", set_instagram))
app.add_handler(CommandHandler("set_telegram", set_telegram))


if __name__ == "__main__":
    app.run_polling()