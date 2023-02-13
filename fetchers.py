import requests


def steam_offers_fetcher(category):
    try:
        res = requests.get(
            'https://store.steampowered.com/api/featuredcategories')
        data = res.json()

        if category == 'specials':
            specials = data['specials']['items']
            return specials

        if category == 'top_sellers':
            top_sellers = data['top_sellers']['items']
            return top_sellers
    except:
        raise Exception(
            'An error occurred while attempting to fetch offers data.')
