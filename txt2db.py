import pymongo
import os
import json


class FileUploader:
    
    def __init__(self):
        self.db = self.connect_to_db('test')

    
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    

    def txt_read(self, file_directory):
        with open (file_directory, 'r') as f:
            print type(f)
            for line in f:
                print type(line)
                print line
                line = line.replace("u'", '"')
                line = line.replace("'", '"')
                print line
                dict_line = json.loads(line)
                print dict_line
                self.db.users.insert(dict_line)