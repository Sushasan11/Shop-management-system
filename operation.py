#Update dictionary here
def dictionaryupdate(laptop_dict,product_no,stock):
    quantity = int(laptop_dict[product_no][3])
    laptop_dict[product_no][3] = quantity - stock

#Purchase function here
def purchase(laptop_dict,product_no,stock):
    quant = int(laptop_dict[product_no][3])
    laptop_dict[product_no][3] = quant + stock
    
    #Ask to continue
def loop(a):
    options = True
    while options:
        ask = input("Do you want to continue(yes/no):  ")
        if ask.lower() == "no":
            a = False
            options = False
            return a
        elif ask.lower() == "yes":
            a = True
            options = False
            return a
        else:
            print("Enter proper values")
            
    #Add to list here for bill
def add_list(laptop_dict,product_no,stock,tally):
    name = laptop_dict[product_no][2]
    company_name = laptop_dict[product_no][1]
    price = int(laptop_dict[product_no][2].replace("$", ""))
    total_price = int(price * stock)
    # list=[name, c_name, price, stock, t_price]
    tally.append([name, company_name, price, stock, total_price])



