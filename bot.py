import discord
from discord.ext import commands
from fetchers import steam_offers_fetcher
from formatters import format_embed_offers_msg

from config import DISCORD_BOT_TOKEN, COMMAND_PREFIX

from messages import bot_messages

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


@bot.command(name='specials', help="Sends you Steam Specials offers.")
async def sendSteamSpecials(ctx):
    try:
        specials = steam_offers_fetcher(category='specials')
        embed_msg = format_embed_offers_msg(
            category='specials', offers=specials)

        await ctx.reply(embed=embed_msg)
    except:
        await ctx.reply(bot_messages['errors']['fetch_data_error'])


@bot.command(name='top', help="Sends you Steam Top Sellers offers.")
async def sendSteamTopSellers(ctx):
    try:
        top_sellers = steam_offers_fetcher(category='top_sellers')
        embed_msg = format_embed_offers_msg(
            category='top_sellers', offers=top_sellers)
        await ctx.reply(embed=embed_msg)
    except:
        await ctx.reply(bot_messages['errors']['fetch_data_error'])


@bot.command(name='about', help='Sends you info about the bot and its available commands.')
async def sendAboutMessage(ctx):
    try:
        embed_msg = discord.Embed(title=' ', description=bot_messages['about'])
        await ctx.reply(embed=embed_msg)
    except:
        await ctx.reply(bot_messages['errors']['fetch_data_error'])

bot.run(token=DISCORD_BOT_TOKEN)
