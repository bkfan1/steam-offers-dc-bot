from fetchers import steam_category_offers_fetcher, steam_app_details_fetcher
from formatters import format_embed_offers_msg, format_app_details


def steam_offers_dispatcher(action_type, payload):

    if action_type == 'SEND_SPECIALS':

        country_code = payload.get('alpha2_code')

        specials = steam_category_offers_fetcher('specials', country_code)

        embed_msg = format_embed_offers_msg(
            'Special Offers', f'Special Offers on Steam {country_code}', specials)

        return embed_msg

    if action_type == 'SEND_TOP_SELLERS':
        country_code = payload.get('alpha2_code')

        specials = steam_category_offers_fetcher('top_sellers', country_code)

        embed_msg = format_embed_offers_msg(
            'Top Sellers', f'Top Sellers on Steam {country_code}', specials)

        return embed_msg

    if action_type == 'SEND_APP_DETAILS':

        app_id = payload.get('app_id')
        country_code = payload.get('alpha2_code')

        app_data = steam_app_details_fetcher(app_id, country_code)

        embed_msg = format_app_details(app_data)

        return embed_msg
