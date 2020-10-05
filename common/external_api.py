from typing import List, Dict
from requests import Response, Request, request
import hashlib
import json
from time import time


class ExternalApi:
    rapidapi_url: str = 'https://restcountries-v1.p.rapidapi.com/'
    restapi_url: str = 'https://restcountries.eu/rest/v2/'

    @staticmethod
    def __encrypt_languages(languages: List):
        new_languages: bytes = json.dumps(languages).encode('utf-8')
        return hashlib.sha1(new_languages).hexdigest()

    @staticmethod
    def __get(url, headers=None) -> str:
        response: Response = request(method='GET', url=url, headers=headers) \
            if headers else request(method='GET', url=url)

        if not response.ok:
            return 'Bad response Api'
        return response.json()

    def get_all_regions(self):
        all_countries_url: str = f'{self.rapidapi_url}all'
        headers: Dict = {
            'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
            'x-rapidapi-key': "0672ac679fmsh169cc707d5a624fp1e9ccdjsnb635125fbe7a"
        }

        countries: str = ExternalApi().__get(url=all_countries_url, headers=headers)
        if countries == 'Bad response Api':
            return countries

        regions: List = []
        for country in countries:
            if country['region'] not in regions and country['region'] != '':
                regions.append(country['region'])

        return regions

    def get_first_country_by_region(self, regions: List):
        collections: List = []
        for region in regions:
            initial_time = time()
            countries_by_region_url: str = f'{self.restapi_url}region/{region}'
            countries = self.__get(url=countries_by_region_url)
            country: str = countries[0]['name']
            languages: List = [language['name'] for language in countries[0]['languages']]

            collections.append({
                'region': region,
                'country': country,
                'language': ExternalApi.__encrypt_languages(languages),
                'time': round(time() - initial_time, 2)
            })

        return collections





