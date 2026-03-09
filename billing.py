# ~ 3. Billing System for Retail Store
# Scan products, apply discounts, generate bills, and record transactions.

product=[]
def add_product():
    name=input("enter product name:")
    price=input("enter product price:")
    product.append({"name":name,"price":price})
    print("product added")

def apply_dicounts():
    for p in product:
        if p["price"]>100:
            p["price"]=p["price"]-p["price"]*0.1
            print("discount applied")
        else:
            print("no discount") 

def generate_bill():
    total=0
    for p in product:
        total+=int(p["price"])
    print("total bill:",total)

def record_transaction():
    for p in product:
        print(p)
    

def show_product():
    for p in product:
        print(p)

def main():
    while True:
        print("\n1.Add Product 2.Show Product 3.Apply Discounts 4.Generate Bill 5.Record Transaction 6.Exit")
        ch=int(input("enter choice:"))
        if ch==1:
            add_product()
        elif ch==2:
            show_product()
        elif ch==3:
            apply_dicounts()
        elif ch==4:
            generate_bill()
        elif ch==5:
            record_transaction()
        elif ch==6:
            break
        else:
            print("invalid choice")
main()
