import pymongo
import os
import json


class FileUploader:
    
    def __init__(self):#handles the connection
        self.db = self.connect_to_db('test')

    
    def connect_to_db(self,db_name):#handles the connection
        client = pymongo.MongoClient()
        return client[db_name]
    

    def txt_read(self, file_directory):#Reads the txt file to write it in our database
        with open (file_directory, 'r') as f:#opens the file
            print type(f)
            for line in f:#for every line
                print type(line)
                print line
                line = line.replace("u'", '"')#Replaces the u from our file's line so it can read it as json file
                line = line.replace("'", '"')
                print line
                dict_line = json.loads(line)#keeps the line in an attribute (dict form)
                print dict_line
                self.db.users.insert(dict_line)#inserts the dictionary into our database