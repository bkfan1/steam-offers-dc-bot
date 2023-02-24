from config import COMMAND_PREFIX
bot_messages = {
    'about': f'**About this bot:**\nSteamOffersBot is a Discord Bot to get the current offers (specials and top sellers) on Steam.\n\n**How it works:**\n1. Every time the commands **{COMMAND_PREFIX}specials** or **{COMMAND_PREFIX}top** are used, the bots fetch data from the API endpoint: https://store.steampowered.com/api/featuredcategories.\n\n2. The data is formatted in a readable way and sent back to the user as a reply message from the bot.\n\n3. The steps 1 and 2 keeps repeating while the bot is running.\n\n**Available Commands:**\n**{COMMAND_PREFIX}specials (alpha-2 country code)** - To get the special offers (games with discount) on steam in a specific region or country. **Example:** Use {COMMAND_PREFIX}specials US to get the specials on the United States).\n\n**{COMMAND_PREFIX}top (alpha-2 country code)** - To get the top sellers on steam in a specific region or country. **Example:** Use {COMMAND_PREFIX}top US to get the top sellers on the United States.\n\n**details (steam app ID) (alpha-2 country code)** - To view detailed information of a specific app on Steam in a specific region or country. **Example:** Use .details 500 AR to see details about Left 4 Dead 1 in Argentina.\n\n**{COMMAND_PREFIX}about** - Shows helpful information about the bot.',
    'errors': {
        'unknown_command': f'Invalid or unknown command. Please use {COMMAND_PREFIX}help to see the available commands. ',
        'fetch_data_error': 'An error ocurred while attempting to fetch the requested data. Try again or contact the developer.',
        'invalid_alpha-2_code': 'You need to provide a valid country Alpha-2 code. (You can visit https://www.iban.com/country-codes to get a valid alpha-2 code for an specific country).'
    }

}
