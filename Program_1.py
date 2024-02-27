class Add:
    def __call__(self, list1):
        return sum(list1)

def list_input():
    list1=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        item=input("Enter the item : ")
        while(not item.isdigit()):
            item=input("Invalid Item!\nEnter the item : ")
        list1.append(int(item))
        ch=input("Add another item?(y/n) : ")
    return list1

print("-- Make a list of numbers --")
list1 = list_input()

add = Add()
total = add(list1)

print(f"Sum of numbers : {total}")