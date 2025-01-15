import logging
import requests
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# API Keys
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command and display menu options."""
    keyboard = [
        [InlineKeyboardButton("🎬 Movies", callback_data="movies")],
        [InlineKeyboardButton("📺 Series", callback_data="series")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to Sheikh Talal Zaki's Media Bot!\nChoose an option:",
        reply_markup=reply_markup
    )

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle menu selection for Movies or Series."""
    query = update.callback_query
    await query.answer()

    if query.data == "movies":
        await query.edit_message_text(
            "Send the TMDb ID of the movie using the command: \n/movie <ID>"
        )
    elif query.data == "series":
        await query.edit_message_text(
            "Send the TMDb ID, season, and episode of the series using the command: \n/series <ID> <Season> <Episode>"
        )

async def fetch_movie_info(movie_id: str) -> dict:
    """Fetch movie details from OMDB or TMDb."""
    try:
        if movie_id.startswith("tt"):
            response = requests.get(f"https://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}")
        else:
            response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching movie info: {e}")
        return {"Error": "Failed to fetch movie info"}

async def fetch_series_info(series_id: str) -> dict:
    """Fetch series details from OMDB or TMDb."""
    try:
        if series_id.startswith("tt"):
            response = requests.get(f"https://www.omdbapi.com/?i={series_id}&apikey={OMDB_API_KEY}")
        else:
            response = requests.get(f"https://api.themoviedb.org/3/tv/{series_id}?api_key={TMDB_API_KEY}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching series info: {e}")
        return {"Error": "Failed to fetch series info"}

async def movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /movie command."""
    if len(context.args) < 1:
        await update.message.reply_text("Please provide a movie ID.")
        return

    movie_id = context.args[0]
    movie_info = await fetch_movie_info(movie_id)

    if "Error" in movie_info:
        await update.message.reply_text("Movie not found. Please check the ID.")
        return

    embed_urls = [
        f"https://vidsrc.to/embed/movie/{movie_id}",
        f"https://vidsrc.xyz/embed/movie/{movie_id}",
        f"https://www.2embed.cc/embed/{movie_id}",
    ]

    details = (
        f"?? *{movie_info.get('Title', movie_info.get('original_title', 'Unknown Title'))}*\n"
        f"?? *Plot:* {movie_info.get('Plot', movie_info.get('overview', 'No plot available.'))}\n"
        f"?? *Release Date:* {movie_info.get('Released', movie_info.get('release_date', 'N/A'))}\n"
        f"? *Rating:* {movie_info.get('imdbRating', movie_info.get('vote_average', 'N/A'))}\n"
    )

    buttons = [
        [InlineKeyboardButton(f"Server {i + 1}", url=url)]
        for i, url in enumerate(embed_urls)
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(details, reply_markup=reply_markup, parse_mode="Markdown")

async def series_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /series command."""
    if len(context.args) < 3:
        await update.message.reply_text("Please provide a series ID, season, and episode.")
        return

    series_id, season, episode = context.args[:3]
    series_info = await fetch_series_info(series_id)

    if "Error" in series_info:
        await update.message.reply_text("Series not found. Please check the ID.")
        return

    embed_urls = [
        f"https://vidsrc.to/embed/tv/{series_id}/{season}/{episode}",
        f"https://vidsrc.xyz/embed/tv/{series_id}/{season}-{episode}",
        f"https://www.2embed.cc/embedtv/{series_id}&s={season}&e={episode}",
    ]

    details = (
        f"🎬 *{series_info.get('Title', series_info.get('name', 'Unknown Title'))}*\n"
        f"📝 *Plot:* {series_info.get('Plot', series_info.get('overview', 'No plot available.'))}\n"
        f"📅 *First Air Date:* {series_info.get('Released', series_info.get('first_air_date', 'N/A'))}\n"
        f"⭐ *Rating:* {series_info.get('imdbRating', series_info.get('vote_average', 'N/A'))}\n"
    )

    buttons = [
        [InlineKeyboardButton(f"Server {i + 1}", url=url)]
        for i, url in enumerate(embed_urls)
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(details, reply_markup=reply_markup, parse_mode="Markdown")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_query))
    application.add_handler(CommandHandler("movie", movie_command))
    application.add_handler(CommandHandler("series", series_command))

    application.run_polling()

if __name__ == "__main__":
    main()
