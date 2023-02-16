import requests

CUSTOM_HEADERS = {
    # to simulate that we are requesting data from a steam client
    'User-Agent': 'Mozilla/5.0 (Linux; U; X11; en-US; Valve Steam Client/default/1675997500; ) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}


def steam_app_details_fetcher(app_id: str, country_code=str) -> dict:

    try:
        APP_DETAILS_URL = f'https://store.steampowered.com/api/appdetails/?appids={app_id}&cc={country_code}'

        res = requests.get(url=APP_DETAILS_URL,
                           headers=CUSTOM_HEADERS)
        res_dict = res.json()

        success = res_dict.get(app_id).get('success')

        if success == True:
            app_data = res_dict.get(app_id).get('data')
            return app_data

    except Exception as e:
        raise e


def steam_category_offers_fetcher(category_name=str, country_code=str) -> list:

    try:

        FEATURED_CATEGORIES_URL = f'https://store.steampowered.com/api/featuredcategories?cc={country_code}'

        res = requests.get(url=FEATURED_CATEGORIES_URL,
                           headers=CUSTOM_HEADERS)
        res_dict = res.json()

        category_offers_data = res_dict.get(category_name).get('items')
        offers_list = []

        for category_offer_data in category_offers_data:

            try:
                app_id = str(category_offer_data.get('id'))

                app_data = steam_app_details_fetcher(app_id, country_code)

                offers_list.append(app_data)

            except Exception as e:
                raise e

        return offers_list

    except Exception as e:
        raise e
