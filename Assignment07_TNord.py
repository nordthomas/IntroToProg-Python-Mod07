# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demo script that illustrates the usage of pickling
#              and file exception handling
# ChangeLog (Who,When,What):
#   TNord,8.22.2022,Generate Demo-selection menu and skeleton of overall demo
#   TNord,8.23.2022,Complete pickling demo, start exception demo
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
str_main_choice = ""  # Captures the user's main menu selection
str_pickle_choice = "" # Captures the user's pickle menu selection
FILENAME = "AppData.dat" # File name
obj_file = None  # An object that represents a file
lst_pickle_data = []


# Processing  --------------------------------------------------------------- #
class Processing():
    """  Performs Processing tasks """

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """ Writes data from a list of rows to a File

        :param file_name: (string) with name of file:
        :param list_of_data: (list) you want filled with file data:
        """
        objFile = open(file_name, "wb")
        pickle.dump(list_of_data, objFile)
        objFile.close()

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads binary data from a file

        :param file_name: (string) with name of file:
        """
        objFile = open(FILENAME, "rb")
        objFileData = pickle.load(objFile)  # load() only loads one row of data.
        print(objFileData)
        objFile.close()


# Presentation (Input/Output)  -------------------------------------------- #


class IO():
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_demo():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Pickling Demo
        2) Exception Handling Demo      
        3) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_main_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1-3]: ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_menu_pickle():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Pickle Data
        2) Un-pickle Data      
        3) Return to Main Menu
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_pickle_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1-3]: ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_pickle_data():
        """ Gets user data to be pickled

        :return: list
        """
        strFirstName = str(input("What is your First Name? "))
        strLastName = str(input("What is your Last Name? "))
        lstName = [strFirstName, strLastName]
        return lstName

# Error Handling  -------------------------------------------- #

class NotALetter(Exception):
    """  Check to see if entry is a letter.  """
    def __str__(self):
        return 'Entry is not a letter.'


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - Present user with a menu to select which demo they would like to try
while (True):
    IO.output_menu_demo()  # Shows menu
    str_main_choice = IO.input_main_menu_choice()  # Get menu option

    # Step 2 - Process user's menu choice
    if str_main_choice.strip() == '1':  # Pickling Demo

        while (True):
            IO.output_menu_pickle()  # Shows menu
            str_pickle_choice = IO.input_pickle_menu_choice()  # Get menu option

            if str_pickle_choice.strip() == '1':  # Pickle Data

                # Gather some data to pickle
                print("First, we'll need some data to pickle.")
                lst_pickle_data = IO.input_pickle_data()

                # Thank user and ask them to initiate pickling
                print("\nThank you, " + lst_pickle_data[0] + " " + lst_pickle_data[1] + ".")
                input("Press the Enter key to begin pickling your data.\n")

                # Pickle that data and present it back to the user in its pickled form
                Processing.save_data_to_file(FILENAME, lst_pickle_data)
                print("Your data has been pickled:")
                obj_file = open(FILENAME, "r")
                for i in obj_file:
                    print(i)
                obj_file.close()

            if str_pickle_choice.strip() == '2':  # Un-pickle Data
                print("Here is the data from your file:\n")
                Processing.read_data_from_file(FILENAME)
                print("\nYour data has been un-pickled!")

            elif str_pickle_choice == '3':  # Return to Main Menu
                break  # by exiting loop


    if str_main_choice.strip() == '2':  # Exception Handling Demo

        print(
        """
        Let's look at some exception handling. First, we'll try a 
        basic try-except block to catch our error. If you enter a
        letter the loop will continue, but if you enter any other
        input, such as a number, an error will appear. Go ahead and 
        give it a try!
        """)

        while(True):
            try:
                str_letter = input("Please enter a letter: ")
                if str_letter.isalpha():
                    continue
                else:
                    print("\nThat's not a letter!")

            except:
                print("\nPlease only use letters.")

            break

        print(
        """
        Good. Now let's try it agin, but this time we'll
        provide a little more feedback to the user when we
        encounter an error.
        """)
        input("Press the Enter key to continue.\n")

        while(True):
            try:
                str_letter = input("Please enter a letter: ")
                if str_letter.isalpha():
                    continue
                else:
                    raise Exception

            except Exception as e:
                print("\nThere was a user error!")
                print("Built-in Python error info: ")
                print(e)
                print(type(e))
                print(e.__doc__)
                print(e.__str__())

            break

        print("\nYou're doing great!")
        input("Press the Enter key to continue.")

        print(
        """
        \nOk, let's do this one more time. Now when you 
        encounter an error it will trigger our custom
        exception class.
        """)

        while(True):
            try:
                str_letter = input("Please enter a letter: ")
                if str_letter.isalpha():
                    continue
                else:
                    raise NotALetter()

            except Exception as e:
                print("\nThere was a user error!")
                print("Custom Python error info: ")
                print(e)
                print(type(e))
                print(e.__doc__)
                print(e.__str__())

            break

        input("\nCongratulations! You completed the demo! Press the Enter key to return to the main menu.")
        continue

    elif str_main_choice == '3':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop