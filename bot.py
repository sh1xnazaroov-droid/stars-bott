import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

8729433457:AAETg6P9KcYBlaYZkIAyjxvYQYn-aDIIIyM = os.getenv(")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))


def menu(user_id):
    buttons = [
        [InlineKeyboardButton("⭐ Stars sotib olish", callback_data="buy")],
        [
            InlineKeyboardButton("💰 Balans", callback_data="balance"),
            InlineKeyboardButton("🎁 Stars yuborish", callback_data="send"),
        ],
        [
            InlineKeyboardButton("👤 Profil", callback_data="profile"),
            InlineKeyboardButton("📊 Statistika", callback_data="stats"),
        ],
    ]

    if user_id == 7657455283:
        buttons.append([
            InlineKeyboardButton("⚙️ Admin panel", callback_data="admin")
        ])

    return InlineKeyboardMarkup(buttons)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        "⭐ Stars botga xush kelibsiz!",
        reply_markup=menu(user.id),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user

    if query.data == "buy":
        await query.message.reply_text(
            "⭐ Stars sotib olish\n\n"
            "Bu bo‘lim keyingi bosqichda Telegram Stars to‘loviga ulanadi."
        )

    elif query.data == "balance":
        await query.message.reply_text("💰 Balansingiz: ⭐ 0")

    elif query.data == "send":
        await query.message.reply_text(
            "🎁 Stars yuborish\n\n"
            "Bu bo‘lim keyingi bosqichda ulanadi."
        )

    elif query.data == "profile":
        username = user.username or "yo‘q"

        await query.message.reply_text(
            f"👤 Profil\n\n"
            f"🆔 ID: {user.id}\n"
            f"👤 Username: @{username}"
        )

    elif query.data == "stats":
        await query.message.reply_text(
            "📊 Statistika\n\n"
            "👥 Foydalanuvchilar: 1"
        )

    elif query.data == "admin":
        if user.id != ADMIN_ID:
            await query.message.reply_text("❌ Siz admin emassiz.")
            return

        keyboard = [
            [InlineKeyboardButton(
                "✏️ Tugmalar va matnlar",
                callback_data="edit"
            )],
            [InlineKeyboardButton(
                "💵 Narxlarni o‘zgartirish",
                callback_data="prices"
            )],
            [InlineKeyboardButton(
                "📢 Reklama yuborish",
                callback_data="broadcast"
            )],
            [InlineKeyboardButton(
                "👥 Foydalanuvchilar",
                callback_data="users"
            )],
        ]

        await query.message.reply_text(
            "⚙️ ADMIN PANEL",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "edit":
        await query.message.reply_text(
            "✏️ Tugmalar va matnlarni o‘zgartirish bo‘limi."
        )

    elif query.data == "prices":
        await query.message.reply_text(
            "💵 Narxlarni o‘zgartirish bo‘limi."
        )

    elif query.data == "broadcast":
        await query.message.reply_text(
            "📢 Reklama yuborish bo‘limi."
        )

    elif query.data == "users":
        await query.message.reply_text(
            "👥 Foydalanuvchilar bo‘limi."
        )


def main():
    if not 8729433457:AAETg6P9KcYBlaYZkIAyjxvYQYn-aDIIIyM:
        raise RuntimeError("8729433457:AAETg6P9KcYBlaYZkIAyjxvYQYn-aDIIIyM Environment Variable topilmadi.")

    print("🤖 Bot ishga tushmoqda...")

    app = Application.builder().token(8729433457:AAETg6P9KcYBlaYZkIAyjxvYQYn-aDIIIyM).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ BOT ISHLADI!")

    app.run_polling()


if __name__ == "__main__":
    main()
