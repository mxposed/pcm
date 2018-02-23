import configparser
import pickle


class Dbm:
    def __init__(self, database_file=None):
        config = configparser.ConfigParser()
        config.read('configuration.ini')
        if database_file is None:
            self.database_file = config["DEFAULT"]["database_file"]
        else:
            self.database_file = database_file

    def write_database(self, db_contents):
        with open(self.database_file, 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(db_contents, f, pickle.HIGHEST_PROTOCOL)

    def read_database(self):
        with open(self.database_file, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            return pickle.load(f)
