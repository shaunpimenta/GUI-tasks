items = []
class Node():

    def __init__(self,data):
        self.data = data
        self.next = None

class ItemAddedToCart:
    def __init__(self):  
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
    
        else:
            self.head = newNode

    def printCart(self):
        sr = 1
        current = self.head
        grandTotal = 0
        while(current):
            n,q,p = current.data.split("_")
            print("Sr No :",sr,"\tProduct Name :",n,"  Qty :",q,"  Price :",p,"  Total :",int(p)*int(q))
            grandTotal += int(p)*int(q)
            current = current.next
            sr += 1
        print("Grand Total :",grandTotal)
        sr = 1
        return

    def deleteItem(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
 
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        if temp == None:
            return
        prev.next = temp.next
        temp = None
        return

class eShopping:
    obj = ItemAddedToCart()
    def __init__(self):
        print("\n")
        print("1. Oneplus Phone")
        print("2. Ryzen CPU")
        print("3. Regear Headset")
        print("4. 144Hz Monitor")
        print("5. Gaming Mouse")
        print("6. Check Your Cart")
        print("\n")

        ch = int(input("Enter the item number to add in cart:"))
        print("\n")

        

        if ch == 1:
            print("Price : 20000")
            print("Enter E to exit")
            name = "Phones"
            inp = input("Enter Qty:")
            if inp == "e":
                self.__init__()
            str = name+"_"+inp+"_"+"20000"
            items.append(str)
            self.obj.insert(str)
            self.__init__()

        elif ch == 2:
            print("Price : 12000")
            print("Enter E to exit")
            name = "CPU"
            inp = input("Enter Qty:")
            if inp == "e":
                self.__init__()
            str = name+"_"+inp+"_"+"12000"
            items.append(str)
            self.obj.insert(str)
            self.__init__()

        elif ch == 3:
            print("Price : 1000")
            print("Enter E to exit")
            name = "Headset"
            inp = input("Enter Qty:")
            if inp == "e":
                self.__init__()
            str = name+"_"+inp+"_"+"1000"
            items.append(str)
            self.obj.insert(str)
            self.obj.printCart()
            self.__init__()

        elif ch == 4:
            print("Price : 14000")
            print("Enter E to exit")
            name = "Monitor"
            inp = input("Enter Qty:")
            if inp == "e":
                self.__init__()
            str = name+"_"+inp+"_"+"14000"
            items.append(str)
            self.obj.insert(str)
            self.__init__()

        if ch == 5:
            print("Price : 1000")
            print("Enter E to exit")
            name = "Mouse"
            inp = input("Enter Qty:")
            if inp == "e":
                self.__init__()
            str = name+"_"+inp+"_"+"1000"
            items.append(str)
            self.obj.insert(str)
            self.obj.printCart()
            self.__init__()

        if ch == 6:
            self.cart()
    
    def cart(self):
        self.obj.printCart()
        print("Press 'c' for Checkout")
        print("Press 'd' to Delete Item")
        print("Press 'e' for Exit")
        inp = input("Enter : ")
        if inp == 'e':
            self.__init__()
        elif inp == 'r':
            self.editCart()
        elif inp == 'c':
            print("Ordered Placed Successfully")
    
    def editCart(self):
        inp = int(input("Enter Sr No : "))
        self.obj.deleteItem(items[inp-1])
        print("Deleted")
        self.__init__()

em= eShopping()