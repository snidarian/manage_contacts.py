#!/usr/bin/python3

# import statements
import sqlite3 # incase needed to interact with sqlite database
import sqlalchemy # to interact with database
import texttable # to display information to screen
import colorama # to color-highlight information for ease of use and clarity
import os # since this is a terminal program, use of terminal commands will be required

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
        






# Executions

if __name__=="__main__":
    print("mark0")
    main_menu()










