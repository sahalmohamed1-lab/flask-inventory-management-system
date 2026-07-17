import requests

BASE_URL = "http://127.0.0.1:5000/inventory"

def print_menu():
    print("\n--- Inventory Management System ---")
    print("1. View all items")
    print("2. Add new item (Via OpenFoodFacts Barcode)")
    print("3. Update item price/stock")
    print("4. Delete an item")
    print("5. Exit")

def view_items():
    response = requests.get(BASE_URL)
    items = response.json()
    if not items:
        print("Inventory is empty.")
    else:
        for item in items:
            print(f"ID: {item['id']} | {item['product_name']} ({item['brands']}) - Stock: {item['stock']} - Price: ${item['price']}")

def add_item():
    barcode = input("Enter barcode (or leave blank for manual entry): ")
    if not barcode:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        payload = {"product_name": name, "price": price, "stock": stock}
    else:
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        payload = {"barcode": barcode, "price": price, "stock": stock}
        print("Fetching data from OpenFoodFacts...")

    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Item added successfully:", response.json()['product_name'])
    else:
        print("Failed to add item.")

def update_item():
    item_id = input("Enter the ID of the item to update: ")
    price = input("Enter new price (leave blank to skip): ")
    stock = input("Enter new stock (leave blank to skip): ")
    payload = {}
    if price: payload["price"] = float(price)
    if stock: payload["stock"] = int(stock)
    response = requests.patch(f"{BASE_URL}/{item_id}", json=payload)
    if response.status_code == 200:
        print("Item updated.")
    else:
        print("Error updating item.")

def delete_item():
    item_id = input("Enter the ID of the item to delete: ")
    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("Item deleted.")
    else:
        print("Error deleting item.")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == '1': view_items()
        elif choice == '2': add_item()
        elif choice == '3': update_item()
        elif choice == '4': delete_item()
        elif choice == '5': break
        else: print("Invalid choice.")