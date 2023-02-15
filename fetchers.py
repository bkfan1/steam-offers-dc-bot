import requests


def steam_category_offers_fetcher(category_name="", country_code='US'):

    FEATURED_CATEGORIES_URL = f'https://store.steampowered.com/api/featuredcategories?cc={country_code}'
    res = requests.get(url=FEATURED_CATEGORIES_URL)
    res_dict = res.json()

    category_offers_data = res_dict.get(category_name).get('items')

    offers_list = []

    for category_offer_data in category_offers_data:

        app_id = str(category_offer_data.get('id'))

        APP_DETAILS_URL = f'https://store.steampowered.com/api/appdetails/?appids={app_id}&cc={country_code}'
        
        res = requests.get(url=APP_DETAILS_URL)
        res_dict = res.json()

        success = res_dict.get(app_id).get('success')

        if success == True:
            app_data = res_dict.get(app_id).get('data')
            offers_list.append(app_data)

    return offers_list
