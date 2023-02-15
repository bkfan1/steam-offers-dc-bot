import requests

CUSTOM_HEADERS = {
    # to simulate that we are requesting data from a steam client
    'user-agent': 'Mozilla/5.0 (Linux; U; X11; en-US; Valve Steam Client/default/1675997500; ) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


def steam_app_details_fetcher(app_id: str, country_code='US'):

    try:
        APP_DETAILS_URL = f'https://store.steampowered.com/api/appdetails/?appids={app_id}&cc={country_code}'

        res = requests.get(url=APP_DETAILS_URL, headers=CUSTOM_HEADERS)
        res_dict = res.json()

        success = res_dict.get(app_id).get('success')

        if success == True:
            app_data = res_dict.get(app_id).get('data')
            return app_data
        else:
            raise Exception(
                'An error ocurred while attempting to fetch the app details.')
    except requests.exceptions.RequestException as e:
        raise e


def steam_category_offers_fetcher(category_name='', country_code='US'):

    try:

        FEATURED_CATEGORIES_URL = f'https://store.steampowered.com/api/featuredcategories?cc={country_code}'

        res = requests.get(url=FEATURED_CATEGORIES_URL, headers=CUSTOM_HEADERS)
        res_dict = res.json()

        category_offers_data = res_dict.get(category_name).get('items')
        offers_list = []

        for category_offer_data in category_offers_data:

            try:
                app_id = str(category_offer_data.get('id'))

                APP_DETAILS_URL = f'https://store.steampowered.com/api/appdetails/?appids={app_id}&cc={country_code}'

                res = requests.get(url=APP_DETAILS_URL)
                res_dict = res.json()

                success = res_dict.get(app_id).get('success')

                if success == True:
                    app_data = res_dict.get(app_id).get('data')
                    offers_list.append(app_data)

            except requests.exceptions.RequestException as e:
                raise e

        return offers_list

    except requests.exceptions.RequestException as e:
        raise e
