import discord
from discord.ext import commands
from fetchers import steam_category_offers_fetcher, steam_app_details_fetcher
from formatters import format_embed_offers_msg, format_app_details
from validators import is_valid_alpha2_code
from config import DISCORD_BOT_TOKEN, COMMAND_PREFIX

from messages import bot_messages

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


@bot.command(name='specials', help="Sends you Steam Specials offers in a specific region or country.")
async def send_steam_specials(ctx, alpha2_code='US'):

    result = is_valid_alpha2_code(string=alpha2_code)

    if result == True:
        try:
            specials = steam_category_offers_fetcher(
                category_name='specials', country_code=alpha2_code)

            embed_msg = format_embed_offers_msg(
                'Specials Offers', f'Specials Offers on Steam (:flag_{alpha2_code.lower()}: {alpha2_code.upper()})', specials)

            await ctx.reply(embed=embed_msg)
        except:
            await ctx.reply(bot_messages['errors']['fetch_data_error'])
    else:
        await ctx.reply(bot_messages['errors']['invalid_alpha-2_code'])


@bot.command(name='top', help="Sends you Steam Top Sellers in a specific region or country.")
async def send_steam_top_sellers(ctx, alpha2_code='US'):
    result = is_valid_alpha2_code(string=alpha2_code)

    if result == True:
        try:
            top_sellers = steam_category_offers_fetcher(
                category_name='top_sellers', country_code=alpha2_code)

            embed_msg = format_embed_offers_msg(
                'Top Sellers', f'Top Sellers on Steam (:flag_{alpha2_code.lower()}: {alpha2_code.upper()})', top_sellers)

            await ctx.reply(embed=embed_msg)
        except:
            await ctx.reply(bot_messages['errors']['fetch_data_error'])
    else:
        await ctx.reply(bot_messages['errors']['invalid_alpha-2_code'])


@bot.command(name='details', help='Sends you info about an app data on Steam.')
async def send_app_details(ctx, app_id, alpha2_code='US'):

    result = is_valid_alpha2_code(string=alpha2_code)

    if result == True:
        try:
            app_data = steam_app_details_fetcher(
                app_id, country_code=alpha2_code)
            embed_msg = format_app_details(app_data)
            await ctx.reply(embed=embed_msg)
        except:
            await ctx.reply(bot_messages['errors']['fetch_data_error'])
    else:
        await ctx.reply(bot_messages['errors']['invalid_alpha-2_code'])


@bot.command(name='about', help='Sends you info about the bot and its available commands.')
async def send_about_message(ctx):
    try:
        embed_msg = discord.Embed(title=' ', description=bot_messages['about'])
        await ctx.reply(embed=embed_msg)
    except:
        await ctx.reply(bot_messages['errors']['fetch_data_error'])

bot.run(token=DISCORD_BOT_TOKEN)
