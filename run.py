#!/usr/bin/env python3.9

from users import User

from credentials import Credentials 

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_user(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(username)

def display_user():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()

def create_credentials(account,username,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds a credentials by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credentials exists with that account and return a Boolean
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
# password:str
def main():
    print("Hey welcome to your account list. what is your name?")
    username = input()
    print(f"Hey {username}. How can help?")
    print('\n')
    
    while True:
        print ("use the following short codes:cc- create a new account,dc- display account,dac- display accounts credentials,fc- find an account,cnc-create new credential,fac-find account credentials, ex- exit the account list")
        short_code =input().lower()
        
        if short_code=='cc':
            print("New Account")
            print ("-"*10)
            
            print("username......")
            username=input()
            
            print("password......")
            password=input()
            
            save_user(create_user(username,password))# create and save new user 
            print ('\n')
            print (f"New Account {username}{password} created")
            print ('\n')
            
        elif short_code == 'dc':
            if display_user():
                print("Here is a list of all your accounts")
                print('\n')

                for user in display_user():
                 print(f"{user.username},{user.password}")
                 print('\n')
            
            else: 
                print('\n')
                print("You dont seem to have any accounts saved yet")
                print('\n')
        
        elif short_code == 'fc':
            print("Enter the username you want to search for")
            search_username = input()
            if check_existing_user(search_username):
            
                search_username = find_user(search_username)
                print(f"{search_username.username}")
                print('-' * 20)

                print(f"account.......{search_username.username}")
        
            else:
                print("That account does not exist")
                print('\n')
        
        # elif short_code=='cnc':
        #     if create_credentials(account,username,password):
        #        print("New credentials")
        #        print ("-"*10)
            
        #        print("account name......")
        #        account=input()
        #        print("username......")
        #        username=input()
            
        #        print("password......")
        #        password=input()
            
        #        save_credentials(create_credentials(account,username,password))# create and save new credentials
        #        print ('\n')
        #        print (f"New credentials {account}{username}{password} created")
        #        print ('\n')
        
        # elif short_code == 'fac':
        #     print("Enter the account credentials you want to search for")
        #     search_account = input()
        #     if check_existing_user(search_account):
            
        #         search_account = find_credentials(search_account)
        #         print(f"{search_account.account}")
        #         print('-' * 20)

        #         print(f"account.......{search_account.account}")
        
        # elif short_code == 'dac':
        #     if display_user():
        #         print("Here is a list of all your credentials")
        #         print('\n')

        #         for credentials in display_credentials():
        #             print(f"{credentials.account},{credentials.username},{credentials.password}")
        #             print('\n')
            
        # else: 
        #         print('\n')
        #         print("You dont seem to have any account credentials saved yet")
        #         print('\n')
        
        #     else:
        #         print("That account does not exist")
        # print('\n')
        
        elif short_code == "ex":
                print("Bye and have a lovely day .......")
        
        else:
            print("I really didn't get that. Please use the short codes")
        
if __name__ == '__main__':
               main()

        
            