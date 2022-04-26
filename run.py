#!/usr/bin/env python3.9

from users import User

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


