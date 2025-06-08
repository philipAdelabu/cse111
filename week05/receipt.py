# For creativity, a function is defined to print out the remaining days before (Jan 1) for a 
# The function definition starts from line 81 

import csv 
from datetime import datetime, date

def main():
    
    PRODUCT_ID = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2
    TAX_RATE = .06

    STORE_NAME = "Inkom Emporium"
    print(STORE_NAME)
   
    product_list = read_dictionary('products.csv', PRODUCT_ID)
    print("All products")
    print(product_list) 
    ordered_items = 0
    sub_total = 0
    print("\nRequested Items")
    try:
        with open('request.csv', "r", encoding="utf-8") as file:
            request_file = csv.reader(file)
            next(request_file)
            for line in request_file:
                product = product_list[line[PRODUCT_ID]]
                ordered_items += int(line[1])
                sub_total +=float(product[PRODUCT_PRICE]) * int(line[1])
                print(f"{product[PRODUCT_NAME]} {line[1]} @ {product[PRODUCT_PRICE]}")
    except FileNotFoundError as file_not_found:
        print("File not found:" , file_not_found)
        return 
    except PermissionError as permission_error:
        print("Access deny: "+ permission_error)
        return
    except KeyError as key_error:
        print("Dictionary Illegal Key: ", key_error)
    
    
    tax = sub_total * TAX_RATE
    total = tax + sub_total
    print_receipt(ordered_items, tax, sub_total, total, STORE_NAME)
    



def read_dictionary(filename, key_column_index):
    products = {}
    try:
        with open(filename, 'r', encoding="utf-8") as product_file:
            file = csv.reader(product_file)
            next(file)
            for line in file:
                if len(line) > 0:
                    products[line[key_column_index]] = line

    except FileNotFoundError as file_not_found:
        print("File not found:" , file_not_found)
        return
    except PermissionError as permission_error:
        print("Access deny: "+ permission_error)
        return 
    except KeyError as key_error:
        print("Dictionary Illegal Key: ", key_error)

    return products


def print_receipt(ordered_items, tax, sub_total, total, shop_name):
   
    print("Number of Items: ", ordered_items)
    print("Subtotal: ", round(sub_total,2))
    print("Sales Tax: ", round(tax, 2))
    print("Total: ", round(total, 2))
    print("Thank you for shopping at the ", shop_name)
    now = datetime.now()
    formatted_time = now.strftime("%a %b %e %H:%M:%S %Y")
    print(formatted_time)
    print(remainder_of_days())



def remainder_of_days():
    today = date.today()
    next_year = today.year + 1
    new_year_sale_date = date(next_year, 1, 1)
    days_remaining = (new_year_sale_date - today).days
    return f"Reminder: There are {days_remaining} days until the New Year's (Jan 1) Sale begins!"


        


if __name__ == "__main__":
    main()
