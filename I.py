def show_menu(menu_type, menu):
    print(f"\n{menu_type}เมนู:")
    for key, value in menu.items():
        print(f"{key}. {value['name']} - {value['price']} บาท")

def get_selection(menu, menu_type):
    choice = input(f"\nเลือก {menu_type}เมนู (พิมพ์เลข): ")
    if choice in menu:
        return menu[choice]
    else:
        print(f"{menu_type}เมนูไม่ถูกต้อง")
        return None

# เมนูอาหารและเครื่องดื่ม
food_menu = {
    "1": {"name": "ข้าวผัด", "price": 45},
    "2": {"name": "ผัดไทย", "price": 50}
}

drink_menu = {
    "1": {"name": "น้ำเปล่า", "price": 10},
    "2": {"name": "ชาเขียว", "price": 25}
}

# เริ่มต้นโปรแกรม
order_food = input("ต้องการสั่งอาหารหรือไม่ (y/n): ").lower()

if order_food == "y":
    # เลือกอาหาร
    show_menu("อาหาร", food_menu)
    food = get_selection(food_menu, "อาหาร")
    food_price = food['price'] if food else 0

    # ถามเรื่องเครื่องดื่ม
    order_drink = input("\nต้องการเครื่องดื่มหรือไม่ (y/n): ").lower()
    drink_price = 0
    if order_drink == "y":
        show_menu("เครื่องดื่ม", drink_menu)
        drink = get_selection(drink_menu, "เครื่องดื่ม")
        if drink:
            drink_price = drink['price']

    total = food_price + drink_price
    print(f"\nยอดรวม: {total} บาท")

    # ระบบสมาชิก
    is_member = input("คุณเป็นสมาชิกหรือไม่ (y/n): ").lower()
    if is_member == "y":
        member_code = input("กรอกรหัสสมาชิก (รหัสคือ 1234): ")
        if member_code == "1234":
            discount = total * 0.10
            total -= discount
            print(f"คุณได้รับส่วนลด 10% = {discount:.2f} บาท")
        else:
            print("รหัสสมาชิกไม่ถูกต้อง")
    print(f"\nยอดสุทธิที่ต้องชำระ: {total:.2f} บาท")
else:
    print("ขอบคุณที่ใช้บริการ")
