from services import RegionsService


def zinobe(oauth_token: str):
    RegionsService.main_cycle()


if __name__ == '__main__':
    zinobe('PyCharm')

