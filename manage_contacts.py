#!/usr/bin/python3

# import statements
import sqlite3 # incase needed to interact with sqlite database
import sqlalchemy # to interact with database
from sqlalchemy import text # For writing raw SQL statements in case it's needed
import texttable # to display information to screen
import colorama # to color-highlight information for ease of use and clarity
import os # since this is a terminal program, use of terminal commands will be required
import argparse


# color variable escape sequence definitions



# function definitions

# Generate main menu prompt table
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


def print_contacts_table():
    os.system('clear')
    table_object = texttable.Texttable(0)
    table_object.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    table_object.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t"])
    selection_object = contacts.select()
    result = connection_object.execute(selection_object)
    #record = result.fetchone()
    table_object.header(["Id", "Firstname", "Lastname", "Sex", "Phone", "Email", "Address", "Description", "Where met"])
    for row in result:
        table_object.add_row( [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])] )
    # draw and print table
    print(table_object.draw())


# Get single record and generate table for single record

def select_table_single_record(selection_id):
    table_object = texttable.Texttable(0)
    table_object.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    table_object.set_cols_valign(["t", "t", "t", "t", "t", "t", "t", "t", "t"])
    table_object.header(["id", "Firstname", "Lastname", "Sex", "Phone", "Email", "Address", "Description", "Where met"])
    # Create selection object that target desired record called for with parameter
    selection_object = text("SELECT * FROM contacts WHERE contacts.id = :x")
    result = connection_object.execute(selection_object, x = str(selection_id)).fetchone()
    table_object.add_row([result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]])
    print(table_object.draw())


# Main menu entry prompt function
def main_menu():
    inputvar=""
    os.system('clear')
    while inputvar != "0":
        main_menu_table()
        inputvar = input("--> ")
        if inputvar == '0':
            break
        elif inputvar == '1':
            select_record()
        elif inputvar == '2':
            insert_record()
        elif inputvar == '3':
            update_record()
        elif inputvar == '4':
            delete_record()


# CRUD FUNCTION DEFINITIONS


# evaluates each variable to determine if it's a string 0 or not - returns True or False
def insert_return_to_main_menu(variable):
    if variable == "0":
        return False
    else:
        return True

# INSERT
def insert_record():
    run=True
    while run == True:
        print("Enter 0 at any prompt to return to the Main menu")
        firstname = input("Firstname: ")
        run = insert_return_to_main_menu(firstname)
        if run == False:
            break
        lastname = input("Lastname: ")
        run = insert_return_to_main_menu(lastname)
        if run == False:
            break
        sex = input("Sex (m/f): ")
        run = insert_return_to_main_menu(sex)
        if run == False:
            break
        phone = input("Phone #: ")
        run = insert_return_to_main_menu(phone)
        if run == False:
            break
        email = input("Email Address: ")
        run = insert_return_to_main_menu(email)
        if run == False:
            break
        address = input("Physical Address: ")
        run = insert_return_to_main_menu(address)
        if run == False:
            break
        description = input("Description of contact: ")
        run = insert_return_to_main_menu(description)
        if run == False:
            break
        where_met = input("Where you first met: ")
        run = insert_return_to_main_menu(where_met)
        if run == False:
            break

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

        #print("Record dictionary:")
        #print(record_dict)

        # Execute insert statement:
        connection_object.execute(contacts.insert(), record_dict)


# SELECT
def select_record():
    select_all = input("Select all contacts? (y/n)")
    select_all = select_all.upper()
    if select_all == 'Y':
        print_contacts_table()
    elif select_all == 'N':
        pass # add regex search selection statement function here
    else:
        print("Error: Invalid selection...")
        os.system('sleep 2')
# UPDATE
def update_record():
    run = True
    while run == True:
        os.system('clear')
        print_contacts_table()
        print("Type id of record to update (0 to return to main menu)")
        selection_id = input("--> ")
        if selection_id == "0":
            break
        elif int(selection_id) > 0:
            select_table_single_record(selection_id)
            
        else:
            print("Error: Invalid entry")

# DELETE
def delete_record():
    id_selection = 1.5
    while int(id_selection) > 0:
        print_contacts_table()
        id_selection= input("Enter id of record to delete (0 to quit):\n--> ")
        deletion_object = contacts.delete().where(contacts.c.id==id_selection)
        # delete specified record
        connection_object.execute(deletion_object)


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










