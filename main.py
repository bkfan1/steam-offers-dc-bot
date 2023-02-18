import discord
from discord.ext import commands

from validators import is_valid_alpha2_code
from dispatchers import steam_offers_dispatcher

from config import DISCORD_BOT_TOKEN, COMMAND_PREFIX

from messages import bot_messages

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


@bot.command(name='specials', help="Sends you Steam Specials offers in a specific region or country.")
async def send_steam_specials(ctx, alpha2_code='US'):

    if is_valid_alpha2_code(string=alpha2_code):
        try:
            embed_msg = steam_offers_dispatcher(action_type='SEND_SPECIALS', payload={
                'alpha2_code': alpha2_code})

            await ctx.reply(embed=embed_msg)
        except:
            await ctx.reply(bot_messages['errors']['fetch_data_error'])

    else:
        await ctx.reply(bot_messages['errors']['invalid_alpha-2_code'])


@bot.command(name='top', help="Sends you Steam Top Sellers in a specific region or country.")
async def send_steam_top_sellers(ctx, alpha2_code='US'):
    if is_valid_alpha2_code(string=alpha2_code):
        try:
            embed_msg = steam_offers_dispatcher(action_type='SEND_TOP_SELLERS', payload={
                'alpha2_code': alpha2_code})

            await ctx.reply(embed=embed_msg)
        except:
            await ctx.reply(bot_messages['errors']['fetch_data_error'])

    else:
        await ctx.reply(bot_messages['errors']['invalid_alpha-2_code'])


@bot.command(name='details', help='Sends you info about an app data on Steam.')
async def send_app_details(ctx, app_id, alpha2_code='US'):

    if is_valid_alpha2_code(string=alpha2_code):
        try:
            embed_msg = steam_offers_dispatcher(action_type='SEND_APP_DETAILS', payload={
                'app_id': app_id, 'alpha2_code': alpha2_code})

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