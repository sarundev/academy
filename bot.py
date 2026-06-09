import logging
import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = (
        "Welcome to BizGrow Academy!\n\n"
        "We help entrepreneurs and professionals master Business & Marketing — "
        "from strategy to digital sales.\n\n"
        "/lessons — Browse course modules\n"
        "/enroll — Join the course today\n"
        "/schedules — View live sessions\n"
        "/faq — Common questions\n"
        "/contact — Reach our team\n\n"
        "Tap any command to get started.\n\n"
        "Use /off to pause your subscription."
    )
    
    # Create the custom keyboard at the bottom
    keyboard = [
        [KeyboardButton("Enrollment info"), KeyboardButton("Course modules")],
        [KeyboardButton("Live sessions"), KeyboardButton("Frequently asked questions")],
        [KeyboardButton("Support")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Define handlers for each command
async def lessons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Here are our course modules...")

async def enroll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Let's get you enrolled! Please visit our website.")

async def schedules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Here are the upcoming live sessions...")

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Here are some frequently asked questions...")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Reach our team at support@bizgrowacademy.com")

async def off(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Your subscription has been paused. Type /start to resume.")

# Handle regular text messages (for the custom keyboard buttons)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text == "Enrollment info":
        enrollment_message = (
            "Ready to grow your business?\n\n"
            "Course: Business & Marketing Mastery\n"
            "Duration: 6 weeks\n"
            "Format: Video lessons + live Q&A\n"
            "Certificate: Yes, upon completion\n\n"
            "To enroll:\n"
            "1. Visit: https://t.me/ai2academy\n"
            "2. Choose your plan\n"
            "3. Complete secure payment\n"
            "4. Get instant access to all modules\n\n"
            "Questions? Use /faq or /contact."
        )
        await update.message.reply_text(enrollment_message)
    elif text == "Course modules":
        modules_message = (
            "Our Business & Marketing Course — 6 Modules:\n\n"
            "Module 1 — Business Foundations\n"
            "Build your business model and value proposition.\n\n"
            "Module 2 — Marketing Strategy\n"
            "Target audiences, positioning, and brand identity.\n\n"
            "Module 3 — Digital Marketing\n"
            "SEO, social media, email marketing, and paid ads.\n\n"
            "Module 4 — Sales & Conversion\n"
            "Turn leads into loyal paying customers.\n\n"
            "Module 5 — Analytics & Growth\n"
            "Track KPIs and scale your business efficiently.\n\n"
            "Module 6 — Entrepreneurship Mindset\n"
            "Leadership, productivity, and long-term success.\n\n"
            "Use /enroll to join the course now."
        )
        await update.message.reply_text(modules_message)
    elif text == "Live sessions":
        live_sessions_message = (
            "Upcoming Live Sessions:\n\n"
            "Monday — Marketing Strategy Q&A\n"
            "Wednesday — Digital Ads Workshop\n"
            "Friday — Business Open Clinic\n\n"
            "Time: 7:00 PM (GMT+7)\n"
            "Platform: Zoom — link sent to enrolled students\n\n"
            "All sessions are recorded and available within 24 hours.\n\n"
            "Not enrolled? Use /enroll to join."
        )
        await update.message.reply_text(live_sessions_message)
    elif text == "Frequently asked questions":
        faq_message = (
            "Frequently Asked Questions:\n\n"
            "Q: Do I need prior experience?\n"
            "A: No. This suits complete beginners and those leveling up.\n\n"
            "Q: How long do I have access?\n"
            "A: Lifetime access — learn at your own pace.\n\n"
            "Q: Is there a certificate?\n"
            "A: Yes. Awarded after completing all 6 modules.\n\n"
            "Q: What is the refund policy?\n"
            "A: Full refund within 7 days if unsatisfied.\n\n"
            "Q: How do I access lessons after enrolling?\n"
            "A: You receive a private channel invite with all materials.\n\n"
            "More questions? Use /contact."
        )
        await update.message.reply_text(faq_message)
    elif text == "Support":
        support_message = (
            "Need help? We are here for you.\n\n"
            "Support hours: Mon–Sat, 9 AM – 6 PM (GMT+7)\n\n"
            "Contact us:\n"
            "Telegram: @YourSupportUsername\n"
            "Email: support@yourdomain.com\n\n"
            "We reply within 24 hours.\n\n"
            "Check /faq first — your answer may already be there."
        )
        await update.message.reply_text(support_message)
    else:
        await update.message.reply_text(f"I didn't understand: {text}")

def main():
    # Load the bot token from the .env file
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN not found in environment. Please add it to your .env file.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lessons", lessons))
    app.add_handler(CommandHandler("enroll", enroll))
    app.add_handler(CommandHandler("schedules", schedules))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("off", off))
    
    # Register message handler for keyboard buttons
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running! Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
