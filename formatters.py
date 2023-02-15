import discord


def format_app_details(app_data: dict):

    embed_msg = discord.embeds.Embed(
        title='App details', description='Details about this app.')

    app_dict = {
        'name': app_data.get('name'),
        'pricing': {
            'original_price_formatted': app_data.get('price_overview').get('initial_formatted'),
            'final_price_formatted': app_data.get('price_overview').get('final_formatted')
        },
        'developers': app_data.get('developers'),
        'publishers': app_data.get('publishers'),
        'platforms': app_data.get('platforms')
    }

    for key in app_dict.keys():

        txt = ''

        if key == 'pricing':
            embed_msg.add_field(name='Original Price:', value=app_dict.get(
                key).get('original_price_formatted'), inline=False)

            embed_msg.add_field(name='Final Price:', value=app_dict.get(
                key).get('final_price_formatted'), inline=False)

        elif key == 'developers' or key == 'publishers':
            for company_name in app_data.get(key):
                txt += f'{company_name}\n'
            embed_msg.add_field(
                name=f'{key.capitalize()}:', value=txt, inline=False)

        elif key == 'platforms':

            for platform_key in app_data.get(key).keys():

                if app_data.get(key).get(platform_key) == True:
                    txt += f'{platform_key.capitalize()} '

            embed_msg.add_field(name="Platforms:", value=txt, inline=False)

        else:
            embed_msg.add_field(
                name=f'{key.capitalize()}:', value=app_dict.get(key), inline=False)

    return embed_msg


def format_embed_offers_msg(embed_title: str, embed_description: str, offers_list: list):
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
