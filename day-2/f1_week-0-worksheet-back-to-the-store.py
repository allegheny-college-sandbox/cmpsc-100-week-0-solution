#!/usr/bin/env python3

shopping_list = [
    "screwdriver", 
    "wire", 
    "wall plug",
    "spark plug", 
    "candy bar"
]

store_inventory = {
    "screwdriver": {
        "quantity": 20, 
        "price": 2.25
    },
    "wire": {
        "quantity": 12, 
        "price": .79
    },
    "wall plug": {
        "quantity": 10, 
        "price": 1.00
    },
    "spark plug": {
        "quantity": 49, 
        "price": .50
    },
    "candy bar": {
        "quantity": 12, 
        "price": .99
    }
}

tax = .08
total = 0

total = 0

for item in shopping_list:
    total += store_inventory[item]["price"]
    store_inventory[item]["quantity"] -= 1
    
print("Subtotal:",total)
print("Total:",total + total * tax)

for item in store_inventory:
    print(item+" -",store_inventory[item]["quantity"])