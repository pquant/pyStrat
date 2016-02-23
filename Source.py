
import os


class CSV:
    def __init__(self, repo):
        if not os.path.isdir(repo):
            ValueError("Input directory {} is invalid".format(repo))
        self.repo = repo
        self.fileName = None


class Quandl:
    def __init__(self, authtoken):
        self.authtoken = authtoken


class MarketDataService:
    pass




