import pymongo
import os


class FileDownloader:
    def __init__(self):
        self.db = self.connect_to_db('test')
        
    def connect_to_db(self,db_name):
        client = pymongo.MongoClient()
        return client[db_name]
    
    def print_db(self):    
        print self.db
    
    def update_value(self,query,selector,upsert,multi):
        value = self.db.nettuts.update(query,selector,upsert,multi)
    
    def find_users(self,query,selector):
        all_users = self.db.nettuts.find(query,selector)
        return all_users
    
    def create_file(self,all_users, file_directory):
        print all_users.count()
        aa = [i for i in all_users]
        print aa

        with open (file_directory, 'wb') as f:
            for user in aa:
                f.write(str(user))
                f.write("\n")