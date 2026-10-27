
# รับค่าชื่อจริงจากผู้ใช้ แล้วตัดช่องว่างส่วนเกินที่หัว-ท้ายออกด้วย .strip()
first_name = input("Hey, what's your first name? : ").strip()

# รับค่านามสกุลจากผู้ใช้ แล้วตัดช่องว่างส่วนเกินที่หัว-ท้ายออกด้วย .strip()
last_name = input("And your last name? : ").strip()

# แสดงข้อความต้อนรับโดยนำชื่อจริงและนามสกุลมาต่อกัน
print("Well, pleased to meet you, " + first_name + " " + last_name + ".")


'''
first_name=input("Hey, what's your first name? : ")
last_name=input("And your last name? :")
print("Well, pleased to meet you," + first_name + " " + last_name +".")'''
