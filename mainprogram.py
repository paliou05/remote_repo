import pymongo
import os
from db2txt import FileDownloader
from txt2db import FileUploader
from random import randint


def choose_file():
    directory = input("Type your file's directory:")
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(file)
    file_name = input("Type the file name you want:")
    file = directory+file_name
    return file

def get_users(query,selector):
    all_users = filedownloader.find_users(query,selector)
    return all_users

def update_age(all_users):
    for user in all_users:
        user_id = user["_id"]
        query0 = {"_id": user_id}
        selector0 = {"$set" : {"age" : randint(80,90)}}
        filedownloader.update_value(query0,selector0,False,False)
        
def upload_file():
    file = choose_file()
    fileuploader.txt_read(file+'.txt')
    
def download_file():
    filedownloader.print_db()
    query = {}
    selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":1}
    all_users = get_users(query,selector)
    
def update_file():
    update_age(all_users)
    print "\nUpdated\n"
    
def create_file(users):
    file = choose_file()
    filedownloader.create_file(users,file+'.txt')

if __name__ == '__main__':
    
    option = input("1.To upload your database press 1\n2.To download your database press 2\n")
    
    if option == 1:
        fileuploader = FileUploader()
        upload_file()
        
    elif option == 2:
        filedownloader = FileDownloader()
        download_file()
        
        update = input("Want to update age?Y/N\n")
    
        if update == "Y":
            query = {}
            selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":0}
            users = get_users(query,selector)
            update_age(all_users)
            update_file(users)
            create_file(users)
            
        elif update == "N":
            query = {}
            selector = {"first":1,"last":1,"age":1,"dod":1,"gender":1,"hair_colour":1,"occupation":1,"nationality":1,"_id":0}
            users = get_users(query,selector)
            create_file(users)
            
        else:
            exit()

    else:
        print "wrong option"
        exit()
        