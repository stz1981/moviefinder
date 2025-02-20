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
- `python-telegram-bot==21.10`
- `requests==2.32.3`
- `python-dotenv==1.0.1`

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
This bot helps you find information about movies and series. Here are some commands to get you started: 
 
- **/movie 550 (for TMDb ID)**
- **/movie tt0111161 (for IMDb ID)**
- **/series 1399 1 1 (for TMDb ID, season 1, episode 1)**
- **/series tt0944947 1 1 (for IMDb ID, season 1, episode 1)**

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

