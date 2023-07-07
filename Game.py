import random
import pyjokes
from art import *
import emoji
from prettytable import PrettyTable
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

def display_menu(update, context):
    menu = "Вітаю! Я розважальний чат-бот.\n\n" \
           "Оберіть, що вас цікавить:\n" \
           "1. /movies - Рекомендації фільмів\n" \
           "2. /music - Рекомендації музики\n" \
           "3. /games - Рекомендації ігор\n" \
           "4. /joke - Анекдоти\n" \
           "5. /story - Цікаві історії\n" \
           "6. /play - Гра - Камінь-ножиці-папір\n" \
           "7. /exit - Вийти з програми"
    update.message.reply_text(menu)

def recommend_movies(update, context):
    movies = "Ось кілька рекомендацій фільмів:\n" \
             "- Інтерстеллар\n" \
             "- Хороший, поганий, злий\n" \
             "- Володар перснів: Братство кільця"
    update.message.reply_text(movies)

def recommend_music(update, context):
    music = "Ось кілька рекомендацій музики:\n" \
            "- Bohemian Rhapsody - Queen\n" \
            "- Shape of My Heart - Stin\n" \
            "- Hey Jude - The Beatles"
    update.message.reply_text(music)

def recommend_games(update, context):
    games = "Ось кілька рекомендацій ігор:\n" \
            "- The Witcher 3: Wild Hunt\n" \
            "- Animal Crossing: New Horizons\n" \
            "- Among Us"
    update.message.reply_text(games)

def tell_joke(update, context):
    joke = pyjokes.get_joke()
    update.message.reply_text(joke)

def tell_story(update, context):
    story = "У маленькому містечку затишного краю жив кузен-інженер по імені Джек. Він завжди був цікавий світом машин та технологій. Одного дня, коли Джек перебував у своїй майстерні, він знайшов старовинний пристрій, що виглядав як магічна кришталева куля. Надихнений своїми уявленнями про подорожі у часі, Джек вирішив розібрати пристрій та відновити його роботу. Після безлічі досліджень і випробувань він нарешті зрозумів, як активувати пристрій. Раптово, куля розповіла Джеку, що може транспортувати його в будь-яку епоху часу. Заповнений хвилюванням, Джек вирішив побачити світ майбутнього та занурився у пригоду, яка змінила його життя назавжди."
    update.message.reply_text(story)


def play_rock_paper_scissors(update: Update, context: CallbackContext):
    options = ["камінь", "ножиці", "папір"]
    user_choice = update.message.text.strip().lower()

    if user_choice not in options:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Будь ласка, введіть дійсний варіант: камінь, ножиці або папір.")
        return

    bot_choice = random.choice(options)

    if user_choice == bot_choice:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Нічия! Ми обирали одне й те ж.")
    elif (
        (user_choice == "камінь" and bot_choice == "ножиці")
        or (user_choice == "ножиці" and bot_choice == "папір")
        or (user_choice == "папір" and bot_choice == "камінь")
    ):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ви виграли!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ви програли!")

def exit_program(update, context):
    update.message.reply_text("Дякую за використання чат-бота. До зустрічі!")
    updater.stop()

def main():
    updater = Updater("5871255348:AAHdc5OqKsoBvusFObxVQ7gWdHHuR4hF7_k", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", display_menu))
    dispatcher.add_handler(CommandHandler("movies", recommend_movies))
    dispatcher.add_handler(CommandHandler("music", recommend_music))
    dispatcher.add_handler(CommandHandler("games", recommend_games))
    dispatcher.add_handler(CommandHandler("joke", tell_joke))
    dispatcher.add_handler(CommandHandler("story", tell_story))
    dispatcher.add_handler(CommandHandler("play", play_rock_paper_scissors))
    dispatcher.add_handler(CommandHandler("exit", exit_program))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()