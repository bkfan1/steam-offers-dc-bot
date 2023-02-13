# Steam Offers Discord Bot
A Discord Bot to get the current offers (specials and top sellers) on Steam. Created with Python (flask, discord.py, requests).

## How it works:
1. Everytime the commands **specials** or **top** are used, the bots fetch data from the API endpoint: https://store.steampowered.com/api/featuredcategories.
2. The data is formatted in a readable way and sent back to the user as a reply message from the bot.
3. The steps 1 and 2 keeps repeating while the bot is running.

## How to add this bot to your server:
1. Open this link: https://discord.com/api/oauth2/authorize?client_id=1074709878116982784&permissions=414464854080&scope=bot
2. Select the server where you want to add the bot.
3. Click on "Authorize" button.
4. Go to server where bot is located and type .about to see available commands and info about the bot.
5. Try the specified commands from the about message.