import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def send_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    movie_text = (
        "🍿 **Here is your Requested File / Movie** 🎬\n\n"
        "[ File Link / Details Here ]\n\n"
        "🚨 **AUTO-DELETE WARNING** 🚨\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "⏳ **Time Left:** 5 Minutes\n"
        "⚠️ **Reason:** Copyright Protection\n\n"
        "👉 *Delete hone se pehle isey FORWARD / SAVE kar lein!*"
    )

    sent_message = await context.bot.send_message(
        chat_id=chat_id, 
        text=movie_text, 
        parse_mode="Markdown"
    )

    # 5 Minutes wait (300 seconds)
    await asyncio.sleep(300)

    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=sent_message.message_id)
    except Exception as e:
        print(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("movie", send_movie))
    print("Bot Active Hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
