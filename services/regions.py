import pandas as pd

from common import ExternalApi
from config import ConnectionDb


class RegionsService:

    @staticmethod
    def create_data_frame(data):
        return pd.DataFrame(data=data)

    @staticmethod
    def main_cycle() -> None:
        conn = ConnectionDb.connect()
        ConnectionDb.create_if_not_exist_table(conn)

        service: ExternalApi = ExternalApi()
        regions = service.get_all_regions()
        collections = service.get_first_country_by_region(regions=regions)

        data_frame = RegionsService.create_data_frame(collections)
        print(data_frame)
        print(f'Time Max: {data_frame["time"].max()} '
              f'Time Min: {data_frame["time"].min()} '
              f'Time Mean: {data_frame["time"].mean()} '
              f'Time Total: {data_frame["time"].sum()}')

        data_frame.to_sql('country', con=conn, if_exists='append', index=False)
        data_frame.to_json('data.json')
