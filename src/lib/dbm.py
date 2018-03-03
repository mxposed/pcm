import configparser
import pickle

import sys


class Library:
    def __init__(self):
        self.version = 2
        self.tags = set()
        self.entries = []


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
        """

        :return: library database
        :rtype lib.dbm.Library
        """
        with open(self.database_file, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            db = pickle.load(f)
            db = self.ensure_version(db)
            return db

    def ensure_version(self, db):
        if isinstance(db, list):
            print("Updating your database to version 2", file=sys.stderr)
            return self.migrate_1_to_2(db)
        return db

    @staticmethod
    def migrate_1_to_2(db):
        new_db = Library()
        new_db.entries = db
        return new_db



