# name = "somchai"

# for i in range(0, len(name) + 1):
#     print(name[i:])

# for i in range(1, len(name)+1):
#     print(" " * (len(name)-i) + name[:i])

# for i in range(len(name), 0, -1):
#     print(name[:i])

# for i in range(len(name), 0, -1):
#     print(" " * (len(name)-i) + name[:i])


# ########################################################################


# name = "somchai"
# revers_name = name[::-1]

# for i in range(1, len(revers_name)+1):
#     print(" " * (len(revers_name)-i) + revers_name[:i])

# for i in range(len(revers_name), 0, -1):
#     print(revers_name[:i])

# for i in range(len(revers_name), 0, -1):
#     print(" " * (len(revers_name)-i) + revers_name[:i])


# ########################################################################

# name = input("Enter a string: ")
# reversed_name = name[::-1]

# for i in range(len(name)):
#     left = name[:len(name) - i]
#     right = reversed_name[i:]
#     spaces = " " * (2 * i)
#     print(left + spaces + right)

# name = input("Enter a string: ")
# reversed_name = name[::-1]
# n = len(name)

# # 🔻 ส่วนแรก: ลดลง
# for i in range(n):
#     left = name[:n - i]
#     right = reversed_name[i:]
#     space = " " * (2 * i)
#     print(left + space + right)

# # 🔼 ส่วนที่สอง: เพิ่มขึ้น
# for i in range(n - 2, -1, -1):  # ไล่กลับขึ้น โดยไม่ซ้ำบรรทัดกลาง
#     left = name[:n - i]
#     right = reversed_name[i:]
#     space = " " * (2 * i)
#     print(left + space + right)

# name = input("Enter a string: ")
# n = len(name)

# for i in range((n + 1) // 2):
#     spaces = " " * i
#     middle = name[i : n - i]
#     print(spaces + middle)


# name = input("Enter a string: ")
# n = len(name)
# half = (n + 1) // 2

# for i in range(half - 1, -1, -1):
#     print(" " * i + name[i:n - i])

# print(f"\n>>  Program Calculate Grade <<\n{'=' * 30}\n\nInput Data:")

# credit = 3
# s_points = 0
# total_credit = credit * 6

# for i in range(1, 7):
#     subject = input(f"Enter subject name({i}) : ")
#     score = float(input(f"Enter subject score({i}) : "))

#     if 80 <= score <= 100:
#         grade, gp = "A", 4.0
#     elif 70 <= score <= 79:
#         grade, gp = "B", 3.0
#     elif 60 <= score <= 69:
#         grade, gp = "C", 2.0
#     elif 50 <= score <= 59:
#         grade, gp = "D", 1.0
#     else:
#         grade, gp = "F", 0.0

#     points = gp * credit
#     s_points += points

# print(f":{i:^7}: {subject:<27}:{score:^6}:{grade:^7}:{credit:^6}:{points:>5} :")

# # Footer
# print("=" * 67)
# print(f":{'Total':>37}              :{total_credit:>3}  :{s_points:>5} :")
# print("=" * 67)
# print(f": {'Grade Point Average(GPA) : ':<26}{s_points / total_credit:<37}:")
# print("=" * 67)

##################################################################
# 06
##################################################################

# h = "| Main  Menu |"
# l = "=" * len(h)

# while True:
#     print(l, h, l, " 1. Triangle 1", " 2. Triangle 2", " 3. Triangle 3", " 4. Triangle 4", " 5. Exit", sep='\n')
#     choice = int(input("Enter Choice : "))

#     if choice == 1:
#         noc = int(input("\nEnter number of character : "))
#         print()

#         for i in range(noc):
#             print("*" * (i + 1))
#         print()
    
#     elif choice == 2:
#         noc = int(input("\nEnter number of character : "))
#         print()

#         for i in range(noc, 0, -1):
#             print("*" * i)
#         print()

#     elif choice == 3:
#         noc = int(input("\nEnter number of character : "))
#         print()

#         for i in range(1, noc + 1):
#             print(" " * (noc - i) + "*" * i)
#         print()

#     elif choice == 4:
#         noc = int(input("\nEnter number of character : "))
#         print()

#         for i in range(noc, 0, -1):
#             print(" " * (noc - i) + "*" * i)
#         print()
    
#     elif choice == 5:
#         print("\nExit Program ...")
#         break
#     else:
#         print("\nInput error choice.\n")

########################################################################################

# while True:
#     text = input("Enter text(enter-exit) : ")
#     if text == "":
#         break
    
#     if text.isalpha():
#         print("Text is alphabetic")
        
#     elif text.isdigit():
#         print("Text is digit")
        
#     elif text.isalnum():
#         print("Text is alpha and numeric")
        
#     else:
#         print("Text is string")

########################################################################################

# aeiou = 'aeiou'

# while True:
#     text = input("Enter text(enter-exit) : ")

#     if text == "":
#         break

#     a, e, i, o, u = 0, 0, 0, 0, 0

#     for n in text.lower():
#         if n == 'a':
#             a += 1
#         elif n == 'e':
#             e += 1
#         elif n == 'i':
#             i += 1
#         elif n == 'o':
#             o += 1
#         elif n == 'u':
#             u += 1

#     print(f"Text has 'a' : {a}", f"Text has 'e' : {e}", f"Text has 'i' : {i}", f"Text has 'o' : {o}", f"Text has 'u' : {u}", sep='\n')

########################################################################################

# import random

# head, h = "Main  Menu", "|Grade| Total|"
# line, l = "=" * len(head), "-" * len(h)
# total, count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0, 0

# while True:
#     print(head, line, " 1. Input Number of Score", " 2. Random Score and Check Grade", " 3. Exit", sep='\n')

#     choice = input("Enter Choice : ")

#     if choice == '1':
#         total = int(input("Enter number of score : "))

#     elif choice == '2':
#         count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0

#         print("\nStart Random Score ...\nCheck Grade ...\n")

#         for i in range(total):
#             score = random.randint(40, 90)

#             if score >= 80: count_A += 1
#             elif score >= 70: count_B += 1
#             elif score >= 60: count_C += 1
#             elif score >= 50: count_D += 1
#             else: count_F += 1

#         print(l, h, l, f"|  A  | {count_A:>4} |", f"|  B  | {count_B:>4} |", f"|  C  | {count_C:>4} |", f"|  D  | {count_D:>4} |", f"|  F  | {count_F:>4} |", l, f"|Total| {total:>4} |", l, "\n", sep='\n')

#     elif choice == '3':
#         print("Exit Program")
#         break


########################################################################################

# name = input('Enter your name : ')
# num = 5
# print()
# print(name * num)
# print("Show Triangle")
# print(num * "*")
# print((num - 1) * "*")
# print((num - 2) * "*")
# print((num - 3) * "*")
# print((num - 4) * "*")


# name = input('Enter your name : ')
# num = len(name)
# print()
# print(name * num)
# print("Show Triangle name")
# print(name[:num])
# print(name[:num -1])
# print(name[:num -2])
# print(name[:num -3])
# print(name[:num -4])
# print(name[:num -5])
# print(name[:num -6])

########################################################################################

# import math

# def select_menu():
#     menu = "========\n| Menu |\n========\n"
#     menu += "1. Cricle\n2. Rectangle\n3. Exit\nPlease choice : "
#     choice = input(menu)
#     return(choice)

# def cal_cricle(radius):
#     area = math.pi*radius*radius
#     return(area)

# def cal_rectangle(width, height):
#     area = width * height
#     return(area)

# # Main Program
# print("Program calculate area.")
# choice = ''
# while choice != '3':
#     choice = select_menu()
#     if choice == "1":
#         radius = float(input("Enter radius : "))
#         print("Area of cricle = %7.3f" % cal_cricle(radius))
#     elif choice == "2":
#         width = float(input("Enter width : "))
#         height = float(input("Enter height : "))
#         print("Area of rectangle = %7.3f" % cal_rectangle(width, height))
#     elif choice == "3":
#         print("Exit Program.")

##################################################################
# 07
##################################################################

# def find_max(number):
#     return max(int(digit) for digit in str(number))

# # ทดสอบ
# print(find_max(6378942))  # Output: 9

##################################################################

# def check_palindrome(number):
#     str_num = str(number)
#     return str_num == str_num[::-1]

# # ทดสอบ
# print(check_palindrome(12344321))  # ผลลัพธ์: True

##################################################################

# def num_to_text(number):
#     digit_words = {
#         '0': 'ZERO',
#         '1': 'ONE',
#         '2': 'TWO',
#         '3': 'THREE',
#         '4': 'FOUR',
#         '5': 'FIVE',
#         '6': 'SIX',
#         '7': 'SEVEN',
#         '8': 'EIGHT',
#         '9': 'NINE'
#     }

#     str_num = str(number)
#     word_list = [digit_words[digit] for digit in str_num]
#     return ' '.join(word_list)

# # ทดสอบ
# print(num_to_text(638342))

##################################################################

# def dec_to_bin(number):
#     binary = bin(number)[2:]  # ตัด '0b' ออก
#     # เติม 0 ด้านหน้าให้ครบกลุ่มละ 4 บิต
#     padded = binary.zfill((4 - len(binary) % 4) % 4 + len(binary))
#     # แบ่งเป็นกลุ่มละ 4
#     grouped = ' '.join(padded[i:i+4] for i in range(0, len(padded), 4))
#     return grouped

# # ทดสอบ
# print(dec_to_bin(142))  # ผลลัพธ์: 1000 1110

##################################################################

# from random import randint

# def random_and_save(filename, colum, day):
#     with open(filename, 'w') as file:
#         for i in range(1, colum + 1):
#             for a in range(1, day + 1):
#                 sale = randint(500, 5000)
#                 file.write(str(sale))
#                 if a < day:
#                     file.write(",")
#             file.write("\n")


# def report_sale(filename):
#     with open(filename, 'r') as file:
#         data = file.readlines()

#     first_line = data[0].strip()
#     days = first_line.split(',')
#     day = len(days)
#     colum = len(data)

#     h = "Report of Sales"
#     header = ": No.:"

#     for d in range(1, day + 1):
#         header += f"   Day  {d:<2}   :"
#     header += "   Total    :"

#     line = "-" * len(header)

#     print(f"{h:^{len(header)}}", line, header, line, sep='\n')

#     grand_total = 0  # ยอดรวมทั้งหมด
#     day_totals = [0] * day  # ยอดรวมแต่ละวัน ต้องประกาศก่อนลูป

#     for i in range(colum):
#         line_data = data[i].strip()
#         day_list = line_data.split(',')

#         row = f":{i + 1:>3} :"  # หมายเลขสาขา
#         branch_total = 0  # ยอดรวมของสาขานี้

#         for d in range(day):
#             sale = int(day_list[d])
#             branch_total += sale
#             day_totals[d] += sale
#             row += f"  {sale:>7,}  :"

#         row += f"  {branch_total:>9,}  :"
#         grand_total += branch_total

#         print(row)

#     # แสดงยอดรวมทั้งหมด
#     total_day_row = f"Total:"
#     grand_total_2 = 0
#     for dt in day_totals:
#         total_day_row += f"  {dt:>7,}  :"
#         grand_total_2 += dt
#     total_day_row += f"  {grand_total_2:>9,}  :"

#     print(line)
#     print(total_day_row)

# random_and_save('sale.txt', 5, 7)
# report_sale('sale.txt')



# h = f':{' No.'}:{'Menu':^40}:{'Price':^10}:'
# line = '-' * len(h)
# print(line, h, line, sep='\n')
# food = ["Shrimp Fried Rice","Chicken Rice","Garlic Pork Rice","Basil Chicken Rice","Green Curry Rice","Duck Rice","Red Pork Rice","Crab Fried Rice","Basil Seafood Rice","Omelet Rice"]
# count = 1
# for i in food:
#     print(f": {count:>2} : {i:<39}:")
#     count += 1
# print(line)



############################################################################



# # ========================
# # 1. สร้างเมนูอาหารเก็บใน list ของ dictionary
# # ========================

# # ข้าว 10 อย่าง
# rice_menu = [
#     {"name": "Shrimp Fried Rice", "price": 60},
#     {"name": "Chicken Rice", "price": 50},
#     {"name": "Garlic Pork Rice", "price": 55},
#     {"name": "Basil Chicken Rice", "price": 55},
#     {"name": "Green Curry Rice", "price": 65},
#     {"name": "Duck Rice", "price": 70},
#     {"name": "Red Pork Rice", "price": 60},
#     {"name": "Crab Fried Rice", "price": 80},
#     {"name": "Basil Seafood Rice", "price": 75},
#     {"name": "Omelet Rice", "price": 50}
# ]

# # น้ำ 5 อย่าง
# drink_menu = [
#     {"name": "Water", "price": 10},
#     {"name": "Orange Juice", "price": 30},
#     {"name": "Thai Iced Tea", "price": 35},
#     {"name": "Iced Coffee", "price": 35},
#     {"name": "Coconut Water", "price": 25}
# ]

# # อาหารว่าง/ขนม 7 อย่าง
# dessert_menu = [
#     {"name": "Fried Banana", "price": 20},
#     {"name": "Thai Coconut Pancakes", "price": 25},
#     {"name": "Layered Sweet Cake", "price": 30},
#     {"name": "Mango Sticky Rice", "price": 50},
#     {"name": "Roti with Condensed Milk", "price": 25},
#     {"name": "Waffle", "price": 30},
#     {"name": "Chocolate Cake", "price": 40}
# ]

# # ========================
# # 2. ฟังก์ชันแสดงเมนู
# # ========================
# def show_menu(menu):
#     count = 1
#     for item in menu:
#         print(f"{count}. {item['name']} - {item['price']} Baht")
#         count += 1

# # ========================
# # 3. ฟังก์ชันให้ผู้ใช้เลือกได้หลายอย่าง
# # ========================
# def choose_multiple(menu):
#     print("Enter menu numbers (separate with commas, e.g. 1,3,5):")
#     show_menu(menu)
#     selected_items = []

#     while True:
#         choices = input("Your choices: ").split(",")
#         try:
#             for choice in choices:
#                 c = int(choice.strip())
#                 if 1 <= c <= len(menu):
#                     selected_items.append(menu[c - 1])
#                 else:
#                     print(f"Menu {c} not found, ignored.")
#             break
#         except ValueError:
#             print("Please enter only numbers separated by commas.")
#     return selected_items

# # ========================
# # 4. โปรแกรมหลัก
# # ========================
# print("=== RICE MENU ===")
# selected_rice = choose_multiple(rice_menu)

# print("\n=== DRINK MENU ===")
# selected_drink = choose_multiple(drink_menu)

# print("\n=== DESSERT MENU ===")
# selected_dessert = choose_multiple(dessert_menu)

# # รวมเมนูทั้งหมด
# all_selected = selected_rice + selected_drink + selected_dessert
# total = sum(item["price"] for item in all_selected)

# # ------------------------
# # บันทึกลงไฟล์ .txt
# # ------------------------
# filename = "sales.txt"

# with open(filename, "a", encoding="utf-8") as file:  # ใช้โหมด 'a' เพื่อเพิ่มข้อมูลต่อท้ายไฟล์
#     file.write("=== ORDER SUMMARY ===\n")
#     for item in all_selected:
#         file.write(f"- {item['name']} ({item['price']} Baht)\n")
#     file.write(f"Total Price: {total} Baht\n")
#     file.write("-----------------------------\n")

# print(f"\n✅ Receipt saved to '{filename}' successfully!")



# ========================
# 1. สร้างเมนูอาหาร
# ========================

# menu = [
#     {"name": "Shrimp Fried Rice", "price": 60},
#     {"name": "Chicken Rice", "price": 50},
#     {"name": "Garlic Pork Rice", "price": 55},
#     {"name": "Basil Chicken Rice", "price": 55},
#     {"name": "Green Curry Rice", "price": 65}
# ]

# # ========================
# # 2. แสดงเมนู
# # ========================
# def show_menu():
#     print("=== FOOD MENU ===")
#     count = 1
#     for item in menu:
#         print(f"{count}. {item['name']} - {item['price']} Baht")
#         count += 1

# # ========================
# # 3. เลือกอาหารหลายอย่าง
# # ========================
# def choose_food():
#     show_menu()
#     print("Enter menu numbers (e.g. 1,3,5):")
#     choices = input("Your choices: ").split(",")
#     selected = []
#     for choice in choices:
#         try:
#             number = int(choice.strip())
#             if 1 <= number <= len(menu):
#                 selected.append(menu[number - 1])
#             else:
#                 print(f"Menu {number} not found, ignored.")
#         except ValueError:
#             print(f"'{choice}' is not a number, ignored.")
#     return selected

# # ========================
# # 4. บันทึกใบเสร็จตามหมายเลขโต๊ะ
# # ========================
# def save_receipt(table_number, orders):
#     filename = f"receipt_table{table_number}.txt"
#     total = sum(item["price"] for item in orders)

#     with open(filename, "a", encoding="utf-8") as file:
#         file.write(f"=== RECEIPT - TABLE {table_number} ===\n")
#         for item in orders:
#             file.write(f"- {item['name']} ({item['price']} Baht)\n")
#         file.write(f"Total Price: {total} Baht\n")
#         file.write("-----------------------------\n")

#     print(f"\n✅ Receipt saved for Table {table_number}")
#     print(f"Total: {total} Baht\n")

# # ========================
# # 5. โปรแกรมหลัก
# # ========================
# print("=== WELCOME TO OUR RESTAURANT ===")
# table = input("Enter table number: ")

# orders = choose_food()
# save_receipt(table, orders)


# h = f':{'Menu (Food)':^32}:'
# line = '-' * len(h)
# print(line, h, line, sep='\n')

# food = [
#     {"name": "Shrimp Fried Rice", "price": 60},
#     {"name": "Chicken Rice", "price": 50},
#     {"name": "Garlic Pork Rice", "price": 55},
#     {"name": "Basil Chicken Rice", "price": 55},
#     {"name": "Green Curry Rice", "price": 65},
#     {"name": "Duck Rice", "price": 70},
#     {"name": "Red Pork Rice", "price": 60},
#     {"name": "Crab Fried Rice", "price": 80},
#     {"name": "Basil Seafood Rice", "price": 75},
#     {"name": "Omelet Rice", "price": 50}
# ]

# for i in food:
#     print(f': {i["name"]:<25}:{i["price"]:^5}:')
    # print("Name:", i["name"], "Age:", i["price"])


# head = f'|{'Register Member':^30}|'
# print(f'-' * len(head), head, f'-' * len(head), sep='\n')


# h = f':{'WELCOME TO RESTAURANT':^30}:'
# line = '-' * len(h)
# ch = f": {'1. Food':<29}:\n: {'2. Drink':<29}:\n: {'3. Snack':<29}:"
# print('', line, h, line, ch, line, sep='\n')


from ModuleTest import *

# def main():
#     head = f'|{'WELCOME TO RESTAURANT':^40}|'
#     line = '=' * len(head)
#     ch = f": {'1. Register Member':<39}:\n: {'2. Delete Member':<39}:\n: {'3. Menu':<39}:\n: {'4. Table sales summary':<39}:\n: {'5. Daily sales summary':<39}:\n: {'6. Exit program':<39}:"
#     print(line, head, line, ch, line, sep='\n')

#     try:
#         choice = int(input('Enter choice : '))

#         if choice == 1:
#             register_member()
#         elif choice == 2:
#             delete_member()
#         elif choice == 3:
#             filename = "menu.txt"
#             menus = read_menu_from_file(filename)
#             all_orders = []

#             for category, menu_items in menus.items():
#                 orders = select_from_category(category, menu_items)
#                 all_orders.extend(orders)
#             show_receipt(all_orders)
#         elif choice == 4:
#             find_table_sales()
#         elif choice == 5:
#             daily_sales_report()
#         else:
#             print("Please enter only 1 or 6.\n")
#     except ValueError:
#         print('Please enter only 1 or 6.\n')

# if __name__ == "__main__":
#     main()

def main():
    member_info = None

    while True:
        head = f"|{'WELCOME TO RESTAURANT':^40}|"
        line = '=' * len(head)
        ch = f": {'1. Register Member':<39}:\n: {'2. Delete Member':<39}:\n: {'3. Menu':<39}:\n: {'4. Summary of member totals':<39}:\n: {'5. Daily sales summary':<39}:\n: {'6. Exit program':<39}:"
        print(line, head, line, ch, line, sep='\n')

        try:
            choice = int(input('Enter choice : '))

            if choice == 1:
                member_info = register_member()

            elif choice == 2:
                delete_member()

            elif choice == 3:
                if not member_info:
                    print("\nPlease sign in before ordering!\n")
                    continue

                filename = "menu.txt"
                menus = read_menu_from_file(filename)
                all_orders = []

                for category, menu_items in menus.items():
                    orders = select_from_category(category, menu_items)
                    all_orders.extend(orders)

                while True:
                    discount_input = input("Enter discount (%) or Enter if no discount : ").strip()
                    if discount_input == "":
                        discount = 0
                        break
                    elif discount_input.isdigit() and 0 <= int(discount_input) <= 100:
                        discount = int(discount_input)
                        break
                    else:
                        print("Please enter a number 0-100 or Enter if no discount.")

                show_receipt(all_orders, member_info, discount)

            elif choice == 4:
                report_sales_by_member()

            elif choice == 5:
                daily_sales_report()

            elif choice == 6:
                print("Exiting program.")
                break

            else:
                print("Please enter a valid choice (1-6).\n")

        except ValueError:
            print('Please enter numbers only (1-6).\n')

        back = input("\nDo you want to go back to the main menu? (Y/N): ").strip().lower()
        if back != 'y':
            break

if __name__ == "__main__":
    main()
