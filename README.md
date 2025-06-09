# Braves Score Bot

This project is a Discord bot that provides real-time score updates for Atlanta Braves games. The bot responds to the `/score` command with the latest Braves game information.

## Project Structure

```
BravesBot/
├── braves_score_bot/
│   └── src/
│       ├── bot.py            # Main logic for the Discord bot
│       ├── braves_score.py   # Functions to fetch and process Braves scores
│       └── utils.py          # Utility functions (if needed)
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd BravesBot
   ```

2. **Install dependencies:**
   Make sure you have Python 3.8 or higher installed. Then, run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure the bot:**
   - Create a new Discord application and bot at the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy your bot token and set it in `braves_score_bot/src/bot.py` (replace the placeholder).
   - Set your Discord channel ID in `braves_score_bot/src/bot.py`.

4. **Run the bot:**
   ```sh
   python3 braves_score_bot/src/bot.py
   ```

## Usage Guidelines

- Use the `/score` command in your Discord server to get the latest Atlanta Braves score.
- The bot will announce when it is online in the configured channel.
- To change the channel for announcements, update the `CHANNEL_ID` in `bot.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.

---
**Note:**  
You must install the required dependencies with:
```sh
pip install -r requirements.txt
```
and, for Discord.py:
```sh
pip install discord.py
```
