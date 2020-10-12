import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get("common info","baseurl")
        return url
    @staticmethod
    def getUserName():
        un=config.get("common info","username")
        return un

    @staticmethod
    def getPassWord():
        pwd = config.get("common info", "password")
        return pwd

    @staticmethod
    def getLoginPageTitle():
        title = config.get("common info", "loginpagetitle")
        return title

    @staticmethod
    def getHomePageTitle():
        title = config.get("common info", "homepagetitle")
        return title