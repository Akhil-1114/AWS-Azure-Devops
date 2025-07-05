#python with function + global variable 

coffee = 2.5  
tea = 1.8     
cake = 3.0    

def get_menu():
    return {
        "coffee": coffee,
        "tea": tea,
        "cake": cake
    }

print(get_menu())

