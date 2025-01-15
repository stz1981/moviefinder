# Movie and Series Finder Bot

## Overview
This Python-based Telegram bot allows users to quickly find information about movies and TV series by integrating with the OMDB and TMDb APIs. Users can search for movies and series by ID, view plot summaries, release dates, ratings, and easily access streaming links.

### Key Features
- Fetch movie details using TMDb or OMDB API.
- Fetch series information by specifying season and episode.
- Generate streaming links using popular embedding services.
- Interactive Telegram bot interface.

---

## Requirements
- `python-telegram-bot`
- `requests`
- `python-dotenv`

Ensure you have these dependencies listed in your `requirements.txt`:
```plaintext
python-telegram-bot==20.3
requests
python-dotenv
```

---

## How to Run

### Docker Setup
This bot is available as a Docker image for easy deployment.

#### Pull the Docker Image
```bash
docker pull talalzaki/moviefinder
```

#### Run the Bot
```bash
docker run -d --name moviefinder \
  -e TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
  -e OMDB_API_KEY=your_omdb_api_key \
  -e TMDB_API_KEY=your_tmdb_api_key \
  talalzaki/moviefinder
```
Replace `your_telegram_bot_token`, `your_omdb_api_key`, and `your_tmdb_api_key` with your actual API keys.

---

## Usage
1. Start a conversation with your bot on Telegram.
2. Use `/start` to see available options.
3. For movies, use:
   ```
   /movie <TMDb or IMDB ID>
   ```
4. For series, use:
   ```
   /series <TMDb or IMDB ID> <Season> <Episode>
   ```

### Example Commands
- `/movie 550` – Fetches details for the movie with ID 550.
- `/series 1399 1 1` – Fetches details for the first episode of the first season of the series with ID 1399.

---

## Bot Commands Overview
- **/start**: Displays a menu with options for Movies and Series.
- **/movie**: Fetches and displays movie information.
- **/series**: Fetches and displays series information with season and episode.

---

## License
GNU GENERAL PUBLIC LICENSE

---

For any issues or contributions, feel free to open an issue on the repository or contact the developer (Me)!

