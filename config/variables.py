import os


class Variables:

    @staticmethod
    def get_env_deploy():
        return os.getenv('ENV_DEPLOY')

    @staticmethod
    def get_mongo_connection():
        return os.getenv('DB_PORT_27017_TCP_ADDR')
