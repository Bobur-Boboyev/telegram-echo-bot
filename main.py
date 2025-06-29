import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤖 *Hello!*\n"
        "Welcome to the *Echo Bot!*\n\n"
        "🗨️ Just send me any message -\n"
        "and I'll send it right back to you like a mirror.\n\n"
        "✨ Perfect for testing, fun, or just chatting with a bot.\n\n"
        "Have fun! 😄"
    )
    await update.message.reply_text(text, parse_mode='markdown')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.text and not msg.text.startswith("/"):
        await msg.reply_text(msg.text)
    elif msg.sticker:
        await msg.reply_sticker(msg.sticker.file_id)
    elif msg.photo:
        await msg.reply_photo(msg.photo[-1].file_id)
    elif msg.video:
        await msg.reply_video(msg.video.file_id)
    elif msg.animation:
        await msg.reply_animation(msg.animation.file_id)
    elif msg.voice:
        await msg.reply_voice(msg.voice.file_id)
    elif msg.audio:
        await msg.reply_audio(msg.audio.file_id)
    elif msg.document:
        await msg.reply_document(msg.document.file_id)
    else:
        await msg.reply_text("❗ I can't return this type of message.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, echo))

print("The bot is working...")
app.run_polling()

