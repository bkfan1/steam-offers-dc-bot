import discord


def format_embed_offers_msg(embed_title, embed_description, offers_list):
    embed_msg = discord.embeds.Embed(
        title=embed_title, description=embed_description)

    for offer in offers_list:
        title = f':small_blue_diamond: **{offer.get("name")}**'
        og_price = f'{offer.get("price_overview").get("initial_formatted")}'
        discount = f'{offer.get("price_overview").get("discount_percent")}'
        final_price = f'{offer.get("price_overview").get("final_formatted")}'

        price_info = f'~~{og_price}~~ - **{final_price}** __**({discount}% OFF)**__'

        embed_msg.add_field(name=title, value=price_info, inline=False)

    return embed_msg
