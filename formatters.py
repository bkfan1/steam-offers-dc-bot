import discord


def format_embed_offers_msg(category, offers):

    title = ''
    description = ''

    if category == 'specials':
        title = 'Special Offers:'
        description = 'Specials Offers on Steam'
    if category == 'top_sellers':
        title = 'Top Sellers:'
        description = 'Top Sellers on Steam'

    embed_msg = discord.Embed(title=title, description=description)

    for offer in offers:

        title = f':small_blue_diamond: {offer["name"]}'

        currency = ''
        if offer["currency"] == 'USD':
            currency = '$'
        if offer["currency"] == 'EUR':
            currency = '€'

        price = f'~~{currency}{offer["original_price"]}~~ - **{currency}{offer["final_price"]}** __**({offer["discount_percent"]}% OFF)**__'

        embed_msg.add_field(
            name=title, value=f'{price}\n', inline=False)

    return embed_msg
