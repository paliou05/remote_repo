import pymongo
import os
from db2txt import FileDownloader
from txt2db import FileUploader
from random import randint


def choose_file():#user gives directory and file name(while all .txt file printed)
    directory = input("Type your file's directory:")#and returns directory and file name in a file att
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(file)
    file_name = input("Type the file name you want:")
    file = directory+file_name
    return file

def get_users(query,selector):#it returns the dict selected by selector in a ascending form by age
    all_users = filedownloader.find_users(query,selector).sort([("age",pymongo.ASCENDING)])
    return all_users

def update_age(all_users):#set a random age in every user in our dictionary
    for user in all_users:
        user_id = user["_id"]
        query0 = {"_id": user_id}
        selector0 = {"$set" : {"age" : randint(80,90)}}
        filedownloader.update_value(query0,selector0,False,False)

def upload_file():
    file = choose_file()
    fileuploader.txt_read(file+'.txt')
    
def download_file(all_users,query,selector): 
    filedownloader.print_db()
    users = get_users(query,selector,)
    return users

def make_file(users):
    file = choose_file()
    filedownloader.create_file(users,file+'.txt')
    

if __name__ == '__main__':
    
    option = input("1.To upload your database press 1\n2.To download your database press 2\n")
    
    if option == 1:
        fileuploader = FileUploader()
        upload_file()
        #file = choose_file()
        #fileuploader.txt_read(file+'.txt')
        
    elif option == 2:
        filedownloader = FileDownloader()
        query = {}
        selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":1}
        all_users = get_users(query,selector,)
        download_file(all_users,query,selector)
        ##filedownloader.print_db()
        #query = {}
        #selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":1}
        
        
        update = input("Want to update age?Y/N\n")
    
        if update == "Y":
            update_age(all_users)
            print "\nUpdated\n"
            query = {}
            selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":0}
            users = get_users(query,selector)
            make_file(users)
            #file = choose_file()
            #filedownloader.create_file(all_users,file+'.txt')
            
        elif update == "N":
            make_file(all_users)
            #file = choose_file()
            #filedownloader.create_file(all_users,file+'.txt')
            
        else:
            exit()

    else:
        print "wrong option"
        exit()
        