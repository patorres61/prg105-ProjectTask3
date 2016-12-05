# Phyllis Torres
# Task 3 Assignment

# This program will expand the code from Task 1 and Task 2. This task adds code for a returning customer.
# A user will select option 1, indicating they are a returning customer. Then, the user will be asked to enter
# their customer id number. The program will read a file of customers and will select the customer information
# if the customer id matches a customer id in the file. If the customer id does not match an id in the file, an
# error message will be displayed. If the customer id matches a record in the file, the customer information will
# be displayed and the customer will be asked to confirm if this is the correct information. If the customer
# indicates the information is correct, a welcome message is displayed. If the customer indicates the information
# is incorrect, the customer will be prompted to enter the customer id again.

# Due: 12/9/16

# import the datetime module
from datetime import datetime

# print the assignment information
print 'Task 3'
print 'Phyllis Torres'
print 'Due: 12/9/16\n\n'

# define the input file
fileIn = 'customerList.txt'

# get the current date
today = datetime.today()

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# print the title for the display
print color.BOLD + '\n To Bean or Not to Bean...\n\n' + color.END,
print('                              Proprietor: Phyllis Torres\n\n'),
# print the curent day of the week in the following format: day of the week, month, day and year
print ('                           Today is: ' + today.strftime("%A, %b %d, %Y\n\n"))

selection = 0

# define main menu function
def main_menu():
    print color.BOLD + '<<=====================================================>>' + color.END
    print color.BOLD + '<<===                                               ===>>' + color.END
    print color.BOLD + '\n<<===             1. Returning Customer             ===>>' + color.END
    print color.BOLD + '\n<<===             2. New Customer                   ===>>' + color.END
    print color.BOLD + '\n<<===             3. Guest Customer                 ===>>' + color.END
    print color.BOLD + '\n<<===                                               ===>>' + color.END
    print color.BOLD + '<<=====================================================>>' + color.END

# define order menu function
def brew_menu():
    print color.BOLD + '<<=====================================================>>' + color.END
    print color.BOLD + '<<===                                               ===>>' + color.END
    print color.BOLD + '\n<<===             1. Coffee Brews                   ===>>' + color.END
    print color.BOLD + '\n<<===             2. Teas                           ===>>' + color.END
    print color.BOLD + '\n<<===             3. Hot Chocolate                  ===>>' + color.END
    print color.BOLD + '\n<<===                                               ===>>' + color.END
    print color.BOLD + '<<=====================================================>>' + color.END

# define function to accept a user input id to look up a returning guest
def get_customer():
    customer = raw_input('\nPlease enter your customer id: ')
    return customer

# define the function open the file, store the customer information in a list and to look up a
# customer by customer id in the input file
def find_customer(customer):
    try:
        with open(fileIn, 'r') as f:
            customer_list = f.readlines()
            for item in customer_list:
                record = item.split(',')
                if customer == record[0]:
                    return record
        return 'none'
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror) + ': ' + fileIn

# define function to confirm customer information is correct
def confirm_customer():
    confirm = raw_input('\nPlease confirm if this information is correct (Y/N): ')
    return confirm.upper()

# define function to handle the selection for a returning customer
def returning_customer():
    my_customer = get_customer()     # call get_customer to accept user input for customer id
    record = find_customer(my_customer)     # call find_customer to look up the customer id in the customer list

    if record == 'none':

        print '\nThere is no record of the customer id you entered, please try again.\n'
        returning_customer()     # call the returning_customer function

    else:

        phone = record[7]      # move phone number from customer list to a variable
        print '\nYour information is as follows: \n'
        print 'Customer Id: ' + record[0]     # display the customer id
        print record[1], record[2]            # display the customer first and last name
        print record[3]                       # display the customer street address
        print record[4] + ', ' + record[5] + '  ' + record[6]     # display the customer city, state, and zip code
        print '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:10]     # format the phone number in a user friendly display

        response = confirm_customer()     # call the confirm_customer function

        if response == 'Y':

            # display the welcome message
            print color.BOLD + "\nWelcome to 'To Bean or Not to Bean!...where the best brews are bubbling in our cauldrons!" + color.END
            print "\nNow, let's get to work on your order! "
            print "\n\nHere is our Brew Menu: \n"

            brew_menu()    # call the function to display the brew menu

        else:

            print "\nOk, this is not the correct customer information, let's try that again."
            returning_customer()     # call returning_customer function to allow user to input another id
    return

# define function to handle the selection for a new guest
def new_customer():
    print color.BOLD + "\nWelcome to 'To Bean or Not to Bean!...where the best brews are bubbling in our cauldrons!" + color.END
    return

# define function to handle the selection for a guest
def guest_customer():
    print color.BOLD + "\nWelcome to 'To Bean or Not to Bean!...where the best brews are bubbling in our cauldrons!" + color.END
    return

# define function to handle when the selection is not 1, 2, or 3
def wrongnumber():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return

# prompt the user to enter a selection and validate the data entered before determining which function to call
while selection >= 0:

    main_menu()       # display the main menu for the customer

    try:
        selection = int(raw_input('\n\nPlease make the appropriate customer selection: '))

    except ValueError:
        print("\nSorry, I didn't understand that entry.\n")     # this will handle if a user just hits enter or spacebar
        continue     # continue through the loop

    else:

        if selection < 1 or selection > 3:
            selection = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

        if selection == 1:
            print '\nYou have selected the Returning Customer Option.'
            returning_customer()     # call returning_customer function
            selection = - 1

        elif selection == 2:
            print '\nYou have selected the New Customer Option.'
            new_customer()     # call the new_customer function
            selection = - 1

        elif selection == 3:
            print '\nYou have selected the Guest Customer Option.'
            guest_customer()     # call the guest_customer function
            selection = - 1

        else:
            wrongnumber()     # call the wrongnumber function if the user entered an invalid number selection
