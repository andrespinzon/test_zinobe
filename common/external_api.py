from typing import List, Dict, Optional
from requests import Response, Request, request
import json


class ExternalApi:
    rapidapi_url: str = 'https://restcountries-v1.p.rapidapi.com/'
    restapi_url: str = 'https://restcountries.eu/'

    @staticmethod
    def __get(url, headers = None) -> str:
        response: Response = request(method='GET', url=url, headers=headers) \
            if headers else request(method='GET', url=url)

        if not response.ok:
            return 'Bad response Api'
        return response.text

    def get_all_regions(self) -> Optional[List]:
        all_countries_url: str = self.rapidapi_url + 'all'
        headers: Dict = {
            'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
            'x-rapidapi-key': "0672ac679fmsh169cc707d5a624fp1e9ccdjsnb635125fbe7a"
        }

        countries: str = ExternalApi().__get(url=all_countries_url, headers=headers)
        countries = json.loads(countries)

        regions: List = []
        for country in countries:
            if country['region'] not in regions:
                regions.append(country['region'])

        return regions

    @staticmethod
    def get_first_country_by_region(regions: List):
        pass
