import pandas as pd

from common import ExternalApi
from config import ConnectionDb, Variables


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

        if 'LOCAL' == Variables.get_env_deploy():
            data_frame.to_sql('country', con=conn, if_exists='append', index=False)
            print('Save in sqlite')
        else:
            data_dict = data_frame.to_dict('records')
            conn.insert_many(data_dict)
            print('Save in mongo')
        data_frame.to_json('data.json')
