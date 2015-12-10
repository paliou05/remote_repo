import pymongo
import os


class FileDownloader:
    def __init__(self):# The init functions calls the connect_to_db that connects to the client 
        self.db = self.connect_to_db('test') #in our 'test' db and puts it in db attribute
        
    def connect_to_db(self,db_name):#This function makes the connection to the mongo client
        client = pymongo.MongoClient()#and returns the client and the db
        return client[db_name]
    
    def print_db(self):    
        print self.db
    
    def update_value(self,query,selector,upsert,multi):#Updates the age value
        value = self.db.nettuts.update(query,selector,upsert,multi)
    
    def find_users(self,query,selector):#returns the dicts we have in our nettuts collection
        all_users = self.db.nettuts.find(query,selector)#and returns the users
        return all_users
    
    def create_file(self,all_users, file_directory):#Creates the file
        print all_users.count()
        aa = [i for i in all_users]#puts all the collection in an attribute
        print aa

        with open (file_directory, 'wb') as f:#opens the file in the directory and the name given 
            for user in aa:#by the user and writes the collection while changing it to string from
                f.write(str(user))#dict form
                f.write("\n")