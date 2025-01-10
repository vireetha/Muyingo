costprice = int(input("Enter the cp: "))
sellingprice = int(input("Enter the sp:"))
if(sellingprice > costprice):
    print("Profit")
    pt = sellingprice - costprice
    print(pt)
else:
    print("No profit")