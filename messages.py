from config import COMMAND_PREFIX
bot_messages = {
    'about': f'**About:**\n SteamOffersBot is a Discord Bot to get the current offers (specials and top sellers) on Steam.\n\n**How it works:**\n1. Everytime the commands **{COMMAND_PREFIX}specials** or **{COMMAND_PREFIX}top** are used, the bots fetch data from the API endpoint: https://store.steampowered.com/api/featuredcategories.\n\n2. The data is formatted in a readable way and sent back to the user as a reply message from the bot.\n\n3. The steps 1 and 2 keeps repeating while the bot is running.\n\n**Available Commands:**\n**{COMMAND_PREFIX}specials** - To get the special offers (games with discount) on steam.\n**{COMMAND_PREFIX}top** - To get the top sellers on steam.\n**{COMMAND_PREFIX}about** - To known more about the bot and its usage.',
    'errors': {
        'unknown_command': f'Invalid or unknown command. Please use {COMMAND_PREFIX}help to see the available commands. ',
        'fetch_data_error': 'An error ocurred while attempting to fetch the requested data.',
        'invalid_alpha-2_code': 'You need to provide a valid country Alpha-2 code.'
    }

}
