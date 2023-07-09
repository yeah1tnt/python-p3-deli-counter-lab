import ipdb

def line(arr):
    if len(arr) == 0:
        print("The line is currently empty.")
        return
    location = []
    for i, j in enumerate(arr):
        location.append(f"{i + 1}. {j}")
    print(f"The line is currently: {' '.join(location)}")

def take_a_number(arr, name):
    arr.append(name)
    index = len(arr)
    print(f"Welcome, {name}. You are number {index} in line.")
    
def now_serving(arr):
    if(len(arr)==0):
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {arr[0]}.")
        arr.pop(0)

# deli =[]
# take_a_number(deli, "Ada")
# take_a_number(deli, "Gracie")
# print(deli)