def title():
    print("\n")
    print("| ===================================================================================== |")
    print("\t \t \t  Bespoke Laptops")
    print("| ===================================================================================== |")
    print("\t \t  \t Balkot,Bhaktapur")
    print("\t \t \t   9848000010")
    print("| ===================================================================================== |")
    print("\t \t Welcome to our store")
    print("\t Unleash your potential with our powerful laptops")
    print("| ===================================================================================== |")

#displays a table with all the information ragarding the laptop 
def tabel():
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N\t\tName\t\t\tComapny Name\t\tPrice\t   Quantity\t\tProcessor\t\tGraphics")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------")
    file = open("D:\Coursework\Sem-2\FOC\code\elo.txt","r")
    a = 1
    for line in file:
        print(a,"\t\t",line.replace(",", "\t\t"))
        a=a+1
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

#Empty dictinoary is set here to read 
def laptopfile(laptop_dict):
    dict_path = open('D:\Coursework\Sem-2\FOC\code\elo.txt', 'r')
    products = dict_path.readlines()
    for i in range(len(products)):
        a = products[i].strip().split(",") #print (a)
        laptop_dict[i + 1] = a

    return laptop_dict