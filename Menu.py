import datetime

food_menu = [
    {"name": "Shrimp Fried Rice", "price": 60},
    {"name": "Chicken Rice", "price": 50},
    {"name": "Garlic Pork Rice", "price": 55},
    {"name": "Basil Chicken Rice", "price": 55},
    {"name": "Green Curry Rice", "price": 65},
    {"name": "Duck Rice", "price": 70},
    {"name": "Red Pork Rice", "price": 60},
    {"name": "Crab Fried Rice", "price": 70},
    {"name": "Basil Seafood Rice", "price": 65},
    {"name": "Omelet Rice", "price": 45}
]

drink_menu = [
    {"name": "Water", "price": 10},
    {"name": "Coke", "price": 20},
    {"name": "Iced Tea", "price": 25},
    {"name": "Orange Juice", "price": 30},
    {"name": "Iced Coffee", "price": 35}
]

dessert_menu = [
    {"name": "Ice Cream", "price": 30},
    {"name": "Cake", "price": 40},
    {"name": "Cookie", "price": 20},
    {"name": "Donut", "price": 25},
    {"name": "Fruit Salad", "price": 35},
    {"name": "Pudding", "price": 30},
    {"name": "Bread Toast", "price": 25}
]

def show_menu(menu, title):
    h = f"|{title:^39}|"
    head = f'| No.|{'Name':^26}|{'Price':^7}|'
    l = '=' * len(h)
    print('', l, f'|{'':39}|', h, f'|{'':39}|', l, head, l, sep='\n')
    
    i = 1
    for item in menu:
        print(f"|{i:>3} | {item['name']:<25}|{item['price']:^4}.- |")
        i += 1
    print(l)

def choose_items(menu, title):
    show_menu(menu, title)
    choices = input("Enter menu numbers (1,3,5 or Enter to skip) : ")
    selected = []

    if choices.strip() == "":
        return selected

    for choice in choices.split(","):
        try:
            index = int(choice.strip()) - 1
            if 0 <= index < len(menu):
                qty = int(input(f"Quantity for {menu[index]['name']} : "))
                selected.append({
                    "name": menu[index]["name"],
                    "price": menu[index]["price"],
                    "qty": qty
                })
        except ValueError:
            print(f"Invalid input: {choice}")

    return selected

def register_member():
    name = input("Enter member name : ")
    table = input("Enter table number : ")

    with open("member.txt", "a", encoding="utf-8") as f:
        f.write(f"MEMBER : {name} | TABLE : {table}\n")

    print(f"Member '{name}' registered at Table {table}")
    return name, table

def delete_member():
    while True:
        name_to_delete = input("Enter member name to delete (Enter to exit) : ")

        if name_to_delete.strip() == "":
            break

        try:
            with open("member.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            found = False
            new_lines = []

            for line in lines:
                line = line.strip()

                if line.startswith("MEMBER : "):
                    try:
                        member_part = line.split("|")[0].strip()
                        member_name = member_part.replace("MEMBER : ", "").strip()

                        if member_name.lower() == name_to_delete.lower():
                            found = True
                            continue
                    except Exception:
                        pass

                new_lines.append(line + "\n")

            if not found:
                print(f"Member '{name_to_delete}' not found. Please try again.\n")
                continue

            with open("member.txt", "w", encoding="utf-8") as f:
                f.writelines(new_lines)

            print(f"Member '{name_to_delete}' has been removed successfully.\n")
            break

        except FileNotFoundError:
            print("Error: member.txt not found. Please register a member first.\n")
            break

def calculate_total(orders, discount=0):
    total = sum(item["price"] * item["qty"] for item in orders)
    if discount > 0:
        total = total - (total * discount / 100)
    return total

def save_receipt(member_name, table, all_orders, total):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("sales.txt", "a", encoding="utf-8") as f:
        f.write(f"=== TABLE {table} | MEMBER: {member_name} | DATE: {now} ===\n")
        for item in all_orders:
            f.write(f"- {item['name']} x {item['qty']} = {item['price'] * item['qty']} Baht\n")
        f.write(f"Total Price: {total} Baht\n")
        f.write("-----------------------------\n")

# def find_table_sales(table_number):
#     print(f"\n=== SALES FOR TABLE {table_number} ===")
#     found = False

#     with open("sales.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             if f"TABLE {table_number}" in line:
#                 found = True
#             if found:
#                 print(line.strip())
#                 if "-----------------------------" in line:
#                     found = False

def daily_sales_report():
    while True:
        date_input = input("Enter the date to view sales (YYYYMMDD) or press Enter to exit : ").strip()

        if date_input == "":
            return
        
        if len(date_input) != 8 or not date_input.isdigit():
            print("Invalid date format. Please enter in YYYYMMDD format.")
            continue
        
        formatted_date = f"{date_input[:4]}-{date_input[4:6]}-{date_input[6:]}"
        
        total_sales = 0
        current_block_date = None

        try:
            with open("sales.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if "DATE:" in line:
                        date_part = line.split("DATE:")[1].strip().split()[0]
                        current_block_date = date_part
                    
                    if "Total Price:" in line and current_block_date == formatted_date:
                        price = float(line.replace("Total Price:", "").replace("Baht", "").strip())
                        total_sales += price
        except FileNotFoundError:
            print("No sales data found.")
            return

        if total_sales == 0:
            print(f"No sales found for {formatted_date}. Please try again.")
            continue
        else:
            print("\n=== DAILY SALES REPORT ===", f"Date: {formatted_date}", f"Total Sales: {total_sales} Baht", sep='\n')
            break
