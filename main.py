#Imports were done to connect to other module
import read
import operation
import write
import random
#main function of the module 
def main():
    global name, address, phone
    read.title()
    loop = True
    while loop :
        print("------------------------------------------------------------------------------------")
        print("You can choose your own option")
        print("------------------------------------------------------------------------------------")
        print("\n")
        print("Press 1 to Sell Laptops")
        print("Press 2 to Purchase Laptops")
        print("Press 3 Exit")
        print("\n")
        print("------------------------------------------------------------------------------------")
        print("\n")
        #Given Choice 
        choice_test = True
        while choice_test:
            try:
                choice = int(input("Enter the option to continue: "))
            except ValueError as ex:

                print("Enter numeric value")
            else:
                choice_test = False
        print("\n")
        print("\n")
        #Given fields to input
        if choice == 1:

            nametest = True
            while nametest:
                name = input("Enter your full name: ")
                try:
                    if name.isalpha():
                        break
                    else:
                        raise ValueError("")
                except ValueError as ex:
                    print(f"{ex}")

            addresstest = True
            while addresstest:
                address = input("Enter your current address: ")
                try:
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("")
                except ValueError as ex:
                    print(f" {ex}")
            phonetest = True
            while phonetest:
                try:
                    phone = int(input("Enter your phone number: "))
                except ValueError as ex:
                    print(""
                          "")
                else:
                    phonetest = False
            # Setting laptop files and how to access them
            loop_1 = True
            list=[]
            laptop_dict={}
            while loop_1:
                a=True
                laptop_dict = read.laptopfile(laptop_dict)
                read.tabel()
                loop_2=True
                while loop_2:
                    try:
                        product_no = int(input("Enter your serial number: "))
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if 0 < product_no <= len(laptop_dict):
                            loop_2 = False
                if int(laptop_dict[product_no][3])  ==0:
                    print("Out of stocks")
                    a=operation.loop(loop_2)
                    if a :
                        loop_2=True
                    else:
                        loop_2=False
                if a == False:
                    break
                else:
                    stock = int(input("Enter your ordered quantity: "))
                    while stock <= 0:
                        print("Invalid number")
                    operation.dictionaryupdate(laptop_dict, product_no,stock)
                    write.main_write(laptop_dict)
                    loop_1 =operation.loop(loop_1)
                    operation.add_list(laptop_dict,product_no,stock,list)
            if len(list) != 0:
                random_int = random.randint(0, 100)
                write.bill_write_sell(name, address, phone, loop_1,list,random_int)
                write.bill_write_text(name, address, phone, loop_1, list, random_int)
                print("Thankyou for buying laptops")
                print("\n")
        elif choice == 2:
            nametest = True
            while nametest:
                full_name = input("Enter your full name: ")
                try:
                    if full_name.isalpha():
                        break
                    else:
                        raise ValueError("It contains numeric values")
                except ValueError as ex:
                    print(f"Error: {ex}")
            loop_1 = True
            list = []
            laptop_dict={}
            while loop_1:
                laptop_dict = read.laptopfile(laptop_dict)
                read.tabel()
                loop_2 = True
                while loop_2:
                    try:
                        product_no = int(input("Enter your serial number: "))
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if product_no > 0 and product_no <= len(laptop_dict):
                            loop_2 = False
                loop_3 = True
                while loop_3:
                    try:
                        quantity = int(input("Enter your ordered quantity:  "))
                    except ValueError as ex:
                        print("Enter numeric value")
                    else:
                        if quantity > 0:
                            loop_3 = False
                operation.purchase(laptop_dict,product_no,quantity)
                write.main_write(laptop_dict)
                loop_1 = operation.loop(loop_1)
                operation.add_list(laptop_dict, product_no, quantity, list)
                random_int= random.randint(0, 100)
                write.bill_write_purchhase(full_name, loop_1, list, random)
            print("Thankyou for ordering laptops")
            print("\n")
        elif choice == 3:
            loop = False
            print("Thankyou for using our system")
            print("\n")
        else:
            print("Your option",choice,
              "does not seemto match as per our requirement")
            print("\n")
main()
