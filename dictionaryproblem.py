Question :--


#WAP that repeatedly asks the user to enter product names and prices. 
#Store all of them in a dictionary whose keys are product names and values 
#are prices. And also write a code to search an item from the dictionary.



dictnory = { }
while True :
    product = input('Enter the name of product (enter X for quit the program :- )= ')
    if product == "x" or product == "X":
        print("-------------------------------------------------------------------------------------------------------------")#for exter line
        break
    else :
        price = int(input('Enter the MRP of the product :- '))
        dictnory [ product ] = price
while True :
    p_name = input("Enter the name of product those you have entered (enter X for quit the program :- )= ")
    if p_name == "x" or p_name == "X" :
        break
    else :
        if p_name not in dictnory :
            print("No such product Exist accordin to prvious record ! ")
            print("-------------------------------------------------------------------------------------------------------------")#for exter line
        else :
            print("Cost of your product = ",dictnory[p_name])
            print("-------------------------------------------------------------------------------------------------------------")#for exter line
