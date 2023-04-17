import configparser

path = '/home/myroslava/programs/my_second rep/Pytest/homework_17/configurations_1/configuration.ini'
config = configparser.RawConfigParser()
config.read(path)


def get_application_url():
    return config.get('app_data', 'app_url')


def get_user_creds():
    return (config.get('user_data', 'email'), config.get('user_data', 'password'))


def get_browser_id():
    return config.get('browser_data', 'browser_id')
