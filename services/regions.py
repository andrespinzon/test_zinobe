from common import ExternalApi


class RegionsService:

    @staticmethod
    def main_cycle():
        service: ExternalApi = ExternalApi()
        service.get_all_regions()
