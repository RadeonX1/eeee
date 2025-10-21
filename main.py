from Menu import * 

def main():
    while True:
        head = f'|{'Register Member':^30}|'
        line = '-' * len(head)
        ch = f": {'1. Register Member':<29}:\n: {'2. Delete Member':<29}:\n: {'3. Exit program':<29}:"
        print(line, head, line, ch, line, sep='\n')

        try:
            choice = int(input('Enter choice : '))

            if choice == 1:
                member_name, table = register_member()
            elif choice == 2:
                delete_member()
            elif choice == 3:
                return
            else:
                print("Please enter only 1 or 2.\n")
                continue
        except ValueError:
            print('Please enter a valid number (1 or 2).\n')
            continue

        while True:
            h = f':{'WELCOME TO RESTAURANT':^30}:'
            line = '-' * len(h)
            ch = f": {'1. Menu':<29}:\n: {'2. Daily sales summary':<29}:\n: {'3. Exit program':<29}:"
            print('', line, h, line, ch, line, sep='\n')

            try:
                choice = int(input('Please select 1 - 2 (3 to exit) : '))

                if choice == 1:
                    food = choose_items(food_menu, "FOOD MENU")
                    drink = choose_items(drink_menu, "DRINK MENU")
                    dessert = choose_items(dessert_menu, "DESSERT MENU")

                    all_orders = food + drink + dessert
                    
                    discount = 0
                    ans = input("\nApply member discount? (y/n) : ")
                    if ans.lower() == "y":
                        try:
                            discount = int(input("Enter discount percentage : "))
                        except ValueError:
                            discount = 0
                            print("Invalid input. No discount applied.")
                
                    total = calculate_total(all_orders, discount)

                    print(f'\n=== ORDER SUMMARY ===')
                    for item in all_orders:
                        print(f"{item['name']} x {item['qty']} = {item['price'] * item['qty']} .-")
                    print('-' * 21, f"Discount : {discount:<3}%{'':29}", f"Total : {total:>4,.2f} .-", sep='\n')

                    save_receipt(member_name, table, all_orders, total)

                elif choice == 2:
                    daily_sales_report()

                elif choice == 3:
                    print('Exit program.')
                    return

                else:
                    print('Please enter a valid number (1 - 3).')
                    continue
                        
                again = input('\nWould you like to order food again? (y/n) : ').strip().lower()
                if again != 'y':
                    print('Thank you! Goodbye!\n')
                    break
            except ValueError:
                print('Please enter a valid number (1 - 3).')
                continue

if __name__ == "__main__":
    main()