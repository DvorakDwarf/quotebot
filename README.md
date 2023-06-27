How to use:
1. Create a bot through discord developer portal
2. Give the bot priveleged intents in the portal
3. Invite bot to server
4. `git clone https://github.com/DvorakDwarf/quotebot.git`
5. Create a `.env` file inside of `src`and fill in all variables used inside `main.py`. Here is a template
```
TOKEN = ""

#Not needed anymore, can ignore this one
PREFIX = $

MAX_QUOTE_LENGTH = 500
SQL_USERNAME = ""
SQL_PASSWORD = ""
SQL_DATABASE = "quotes_db"
SQL_TABLE = "quotes"
```
5. Install all packages with `python -m pip install -r requirements.txt`
6. Run the bot with `python main.py`
7. Check the bot works by using a slash command `/addquote`
8. ???
9. PROFIT
