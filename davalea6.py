from typing import Union    

def commission_decorator(func):
    def wrapper(balance: Union[int, float], amount: Union[int, float]):
        commission = 1
        totoal_deduction = amount + commission


        if balance < totoal_deduction:
          return  "შეცდომა: ანგარიშზე არ არის საკმარისი თანხა ტრანზაქციისა და საკომისიოსთვის!"
        
         
        updated_balance = func(balance, amount)

        return func(updated_balance, amount)
    
    return wrapper

commission_decorator
def process_transaction(balance: Union[int, float], amount: Union[int, float]) -> str:
   
   final_balance = balance - amount 
   return f"ტრანზაქცია წარმატებით შესრულდა! დარჩენილი ბალანსი: {final_balance:.2f} ლარი."

print(process_transaction(50, 20))

print(process_transaction(10, 10))

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
  
    def __init__(self):
        self.head = None

    def append(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
       
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "სია ცარიელია")

    def search_and_delete(self, key):
       
        current = self.head
        
        if current is None:
            print(f"ელემენტი {key} ვერ მოიძებნა (სია ცარიელია).")
            return False

        if current.data == key:
            self.head = current.next  
            current = None           
            return True

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

     
        if current is None:
            print(f"ელემენტი {key} სიაში ვერ მოიძებნა.")
            return False

        
        prev.next = current.next
        current = None  # ვშლით კვანძს
        return True




llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

print("საწყისი სია:")
llist.display() 

print("\n1. ვშლით შუა ელემენტს (30):")
llist.search_and_delete(30)
llist.display()  

print("\n2. ვშლით პირველ ელემენტს (10):")
llist.search_and_delete(10)
llist.display()  

print("\n3. ვცდილობთ წავშალოთ არარსებული ელემენტი (100):")
llist.search_and_delete(100)