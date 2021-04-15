#!/usr/bin/python3

# import statements
import sqlite3 # incase needed to interact with sqlite database
import sqlalchemy # to interact with database
import texttable # to display information to screen
import colorama # to color-highlight information for ease of use and clarity
import os # since this is a terminal program, use of terminal commands will be required
import argparse


# color variable escape sequence definitions



# function definitions

# generate main menu prompt table
def main_menu_table():
    table_object = texttable.Texttable(0) # zero specifies variable width
    table_object.set_cols_align(["c", "c"])
    table_object.set_cols_valign(["t", "t"])
    table_object.add_rows([
        ["Operation", "Enter Value"],
        ["Exit program", "0"],
        ["View Contact(s)", "1"],
        ["Create Contact(s)", "2"],
        ["Update contact(s)", "3"],
        ["Delete Contact(s)", "4"]])
    print(table_object.draw())


# main entry prompt

def main_menu():
    inputvar=""
    while inputvar != "0":
        os.system('clear')
        main_menu_table()
        inputvar = input("--> ")
        


# CRUD FUNCTION DEFINITIONS


# INSERT
def insert_record():
    run=True
    while run == True:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        sex = input("Sex (m/f): ")
        phone = input("Phone #: ")
        email = input("Email Address: ")
        address = input("Physical Address: ")
        description = input("Description of contact: ")
        where_met = input("Where you first met: ")
        
        # take values and generate contact-entry dictionary
        record_dict = { 
            'firstname' : str(firstname), 
            'lastname' : str(lastname), 
            'sex' : str(sex), 
            'phone' : str(phone),
            'email' : str(email),
            'address' : str(address),
            'description' : str(description),
            'where we met' : str(where_met)
            }

        print("Record dictionary:")
        print(record_dict)

        # Execute insert statement:
        connection_object.execute(contacts.insert(), record_dict)

        
        

# SELECT
def select_record():
    pass
# UPDATE
def update_record():
    pass
# DELETE
def delete_record():
    pass


# ---------------------------------------------------------------------------------
# PROGRAM SETUP


# Set up and parse database arguement

parser = argparse.ArgumentParser(description="Manages contacts from encrypted persistent DB file")
# program takes one arguemnt - filepath to database file to manage
args = parser.add_argument("database", help="SQLite database file path", type=str)

# prepare argument for use
args = parser.parse_args()



# Initiate connection with database 

# create engine
from sqlalchemy import create_engine
engine = create_engine("sqlite:///{}".format(args.database), echo=False)


# generate connection object - creates database in question if not already created
connection_object = engine.connect()


# Set up Metadata class
from sqlalchemy import MetaData
# alias for Metadataclass class
Meta = MetaData()

# set up primary Table 'contacts'
from sqlalchemy import Table, Column, Integer, String

# set up contacts table
contacts = Table(
    'contacts', Meta,
    Column('id', Integer, primary_key = True),
    Column('firstname', String),
    Column('lastname', String),
    Column("sex", String),
    Column('phone', String),
    Column('email', String),
    Column('address', String),
    Column('description', String),
    Column('where we met', String)
)

# Execute the creation of the Table 'contacts'
Meta.create_all(engine)



# -------------------------------------------------------------------------------------
# EXECUTIONS


if __name__=="__main__":
    print("mark0")
    main_menu()
    print(args.database) # database
    insert_record()










