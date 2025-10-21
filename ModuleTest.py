import datetime

# ----------------------------- #
# ลงทะเบียนสมาชิก
# ----------------------------- #
def register_member():
    name = input("Enter member name : ")
    table = input("Enter table number : ")

    with open("member.txt", "a", encoding="utf-8") as f:
        f.write(f"MEMBER : {name} | TABLE : {table}\n")

    print(f"Member '{name}' registered at Table {table}")
    return name, table


# ----------------------------- #
# ลบสมาชิก
# ----------------------------- #
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


# ----------------------------- #
# อ่านเมนูจากไฟล์
# ----------------------------- #
def read_menu_from_file(filename):
    menus = {}
    category = None

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith("===") and line.endswith("==="):
                category = line.replace("=", "").strip()
                menus[category] = []
                continue

            if line.startswith("-"):
                continue

            if category and "," in line:
                parts = line.split(",")
                if len(parts) == 3:
                    no = parts[0].strip()
                    name = parts[1].strip()
                    price = float(parts[2].strip())
                    menus[category].append({
                        "no": no,
                        "name": name,
                        "price": price
                    })
    return menus


# ----------------------------- #
# แสดงเมนูตามหมวดหมู่
# ----------------------------- #
def show_menu_by_category(category, menu_items):
    print(f"\n=== {category} ===")
    print(f"{'No.':<5}{'รายการ':<25}{'ราคา (บาท)':>15}")
    print("-" * 45)
    for item in menu_items:
        print(f"{item['no']:<5}{item['name']:<25}{item['price']:>15,.2f}")
    print("-" * 45)


# ----------------------------- #
# เลือกเมนู
# ----------------------------- #
def select_from_category(category, menu_items):
    orders = []
    show_menu_by_category(category, menu_items)
    selected = input("\nSelect a menu (1,3,5 or Enter to skip): ").strip()

    if selected == "":
        return orders

    selected_numbers = [num.strip() for num in selected.split(",") if num.strip()]

    for num in selected_numbers:
        found = False
        for item in menu_items:
            if item["no"] == num:
                qty = input(f"Enter the number of '{item['name']}': ")
                if qty.isdigit():
                    qty = int(qty)
                    total = item["price"] * qty
                    orders.append({
                        "category": category,
                        "name": item["name"],
                        "price": item["price"],
                        "qty": qty,
                        "total": total
                    })
                else:
                    print("Please enter the quantity in numbers.")
                found = True
                break
        if not found:
            print(f"No menu number found: {num}")

    return orders


# ----------------------------- #
# คำนวณราคารวม
# ----------------------------- #
def calculate_total(orders, discount=0):
    total = sum(item["price"] * item["qty"] for item in orders)
    if discount > 0:
        total -= total * discount / 100
    return total


# ----------------------------- #
# แสดงใบเสร็จ (สวยงาม)
# ----------------------------- #
def show_receipt(all_orders, member_info, discount=0):
    name, table = member_info
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 60)
    print(f"  TABLE {table} | MEMBER: {name} | DATE: {date_str}")
    print("=" * 60)
    print(f"{'รายการ':<25}{'จำนวน':>8}{'ราคา/หน่วย':>14}{'รวม':>13}")
    print("-" * 60)

    total_price = 0
    for order in all_orders:
        total = order['price'] * order['qty']
        total_price += total
        print(f"{order['name']:<25}{order['qty']:>8}{order['price']:>14,.2f}{total:>13,.2f}")

    print("-" * 60)

    if discount > 0:
        discount_amount = total_price * discount / 100
        total_price -= discount_amount
        print(f"{'ส่วนลด':<25}{'':>8}{'-':>14}{discount_amount:>13,.2f}")

    print(f"{'รวมทั้งหมด':<25}{'':>8}{'':>14}{total_price:>13,.2f}")
    print("=" * 60)
    print("💰 ขอบคุณที่ใช้บริการครับ 💰\n")

    # เขียนลงไฟล์
    with open("sales.txt", "a", encoding="utf-8") as f:
        f.write(f"=== TABLE {table} | MEMBER: {name} | DATE: {date_str} ===\n")
        f.write(f"{'รายการ':<25}{'จำนวน':>8}{'ราคา/หน่วย':>14}{'รวม':>13}\n")
        f.write("-" * 60 + "\n")

        for order in all_orders:
            total = order['price'] * order['qty']
            f.write(f"{order['name']:<25}{order['qty']:>8}{order['price']:>14,.2f}{total:>13,.2f}\n")

        if discount > 0:
            f.write(f"{'ส่วนลด':<25}{'':>8}{'-':>14}{discount_amount:>13,.2f}\n")

        f.write(f"{'รวมทั้งหมด':<25}{'':>8}{'':>14}{total_price:>13,.2f}\n")
        f.write("=" * 60 + "\n\n")


# ----------------------------- #
# รายงานยอดขายตามสมาชิก (สวย)
# ----------------------------- #
def report_sales_by_member():
    try:
        with open("sales.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        sales_data = {}
        current_member = None

        for line in lines:
            line = line.strip()
            if line.startswith("=== TABLE"):
                parts = line.split("|")
                for p in parts:
                    if "MEMBER:" in p:
                        current_member = p.split(":")[1].strip()
                        if current_member not in sales_data:
                            sales_data[current_member] = {"food": 0.0, "snack": 0.0, "drink": 0.0, "total": 0.0}
            elif line.startswith("- "):
                item_part = line.split("=")
                name = item_part[0].split("x")[0].replace("-", "").strip()
                price = float(item_part[1].replace("Baht", "").strip())

                if any(word.lower() in name.lower() for word in ["tea", "water", "coke", "coffee", "juice", "milk", "smoothie"]):
                    sales_data[current_member]["drink"] += price
                elif any(word.lower() in name.lower() for word in ["cookie", "cake", "fries", "donut", "snack", "bread", "toast"]):
                    sales_data[current_member]["snack"] += price
                else:
                    sales_data[current_member]["food"] += price
            elif line.startswith("Total Price:"):
                total = float(line.replace("Total Price:", "").replace("Baht", "").strip())
                sales_data[current_member]["total"] += total

        # === กำหนดความกว้างคอลัมน์แบบ Excel ===
        max_name_len = max(len(name) for name in sales_data.keys())
        name_col_width = max(10, max_name_len + 2)
        num_col_width = 12

        # === สร้าง header ===
        header = f"| {'สมาชิก':<{name_col_width}}  | {'อาหาร':>{num_col_width}} | {'ของว่าง':>{num_col_width}}  | {'เครื่องดื่ม':>{num_col_width}}     | {'รวม':>{num_col_width}} |"
        separator = f"|{'-'*(name_col_width+2)}|{'-'*(num_col_width+2)}|{'-'*(num_col_width+2)}|{'-'*(num_col_width+2)}|{'-'*(num_col_width+2)}|"

        print(header)
        print(separator)

        # === แสดงข้อมูลสมาชิก ===
        for member, data in sales_data.items():
            print(f"| {member:<{name_col_width}} | {data['food']:>{num_col_width},.2f} | {data['snack']:>{num_col_width},.2f} | {data['drink']:>{num_col_width},.2f} | {data['total']:>{num_col_width},.2f} |")

        # === สรุปยอดรวม ===
        total_food = sum(d["food"] for d in sales_data.values())
        total_snack = sum(d["snack"] for d in sales_data.values())
        total_drink = sum(d["drink"] for d in sales_data.values())
        total_all = sum(d["total"] for d in sales_data.values())

        print(separator)
        print(f"| {'รวมทั้งหมด':<{name_col_width}}   | {total_food:>{num_col_width},.2f} | {total_snack:>{num_col_width},.2f} | {total_drink:>{num_col_width},.2f} | {total_all:>{num_col_width},.2f} |")
        print(separator)

    except FileNotFoundError:
        print(" ไม่พบไฟล์ sales.txt")


# ----------------------------- #
# รายงานยอดขายรายวัน (สวย)
# ----------------------------- #
def daily_sales_report():
    while True:
        date_input = input("Enter the date (YYYYMMDD) or Enter to exit : ").strip()

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
            print(" No sales data found.")
            return
        else:
            print("\n" + "=" * 50)
            print(f" DAILY SALES REPORT")
            print(f"Date: {formatted_date}")
            print(f"Total Sales: {total_sales:,.2f} Baht")
            print("=" * 50)
            break
