import datetime
import random
# gets the elo.txt file opens it here and set it on the list
def main_write(laptop_dict):
    file = open("elo.txt", "w")
    for indx in laptop_dict.values():
        #print(i)
        file.write(str(indx[0]) + "," + str(indx[1]) + "," + str(indx[2]) + "," + str(indx[3]) + "," + str(indx[4]) + ","+ str(indx[5]) )
        file.write("\n")
    file.close()

#Ask for shippment here and give them bill with shippment
def bill_write_sell(name,address,phone,loop_1,list,random):
    global ship
    shiploop = True
    while shiploop:
        ship = input("Do you want shipment(yes/no): ")
        if ship.lower() == "yes":
            shiploop= False
            cost = 500
        elif ship.lower() == "no":
            shiploop = False
        else:
            print("give valid input ")
        print("Bill no: ", random)
        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
            datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("\t\t\t","Name: ", name, "\n")
        print("Address: ", address, "\t\t\t\tPhone: ", phone)
        total = 0
        print("S.n\t\t", "Laptop Name\t\t", "Brand\t\t\t", "Price\t\t", "Quantity\t\t", "total", )
        for i in range(len(list)):
            print(i+1,"\t\t",list[i][0],"\t\t\t",list[i][1],"\t\t",list[i][2],"\t\t",list[i][3],"\t\t\t\t",list[i][4])
            total = total + int(list[i][4])
        if ship.lower() == "yes":
            print("Shipping fee: ",250)
            total = total + 250
        elif ship.lower() == "no":
            total
        else:
            print("Please comlplie! Enter appropriate value")
        print("\t\t\t\t\t\t\t\t\t\t\tTotal Cost: ", total)
        
        
#Another bill generator for selling
def bill_write_text(name,address,phone,loop_1,list,random):
    if loop_1 != True:
        files = open(f"{random}.txt", "w")
        files.write(f"Bill no: , {random}\n")
        date = datetime.datetime.now().strftime(" %d/%m/%Y")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        files.write(f"Time: {time} \t\t\tDate: {date}\n")

        files.write(f"\t\t\t Name:  {name} \n")
        files.write(f"Address: , {address} \t\t\t\tPhone:  {phone}\n")
        total = 0
        files.write(f"S.n\t\t Laptop Name\t Brand\t\t\t Price\t\t Quantity\t\ttotal \n")
        for i in range(len(list)):
            files.write(f"{i + 1} \t\t {list[i][0]} \t\t\t\t\t\t\t {list[i][1]} \t\t {list[i][2]}\t\t {list[i][3]} \t\t\t\t{list[i][4]}\n")
            total = total + int(list[i][4])
        if ship.lower() == "yes":
            total = total + 250
        elif ship.lower() == "no":
            total
        files.write(f"\t\t\t\t\t\tTotal Cost: , {total}\n")

#Bill generator for purchase
def bill_write_purchhase(name,loop_1,list,random):
    if loop_1 != True:

        print("Bill no: ", random)
        print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"), "\t\t\tDate: ",
            datetime.datetime.now().strftime(" %d/%m/%Y"), "\n")
        print("\t\t\t","Name: ", name, "\n")

        total = 0
        print("S.n\t\t", "Laptop Name\t\t", "Brand\t\t\t", "Price\t\t", "Quantity\t\t", "total", )
        for i in range(len(list)):
            print(i+1,"\t\t",list[i][0],"\t\t\t\t",list[i][1],"\t\t",list[i][2],"\t\t",list[i][3],"\t\t\t\t",list[i][4])
            total = total + int(list[i][4])

        print("\t\t\t\t\t\tTotal Cost: ", total)
        vat = total * (13/100)
        print("\t\t\tVat Amount: ", vat)
        with_vat= total + vat
        print("\t\t\t\t\t\tTotal Cost: ", with_vat)
