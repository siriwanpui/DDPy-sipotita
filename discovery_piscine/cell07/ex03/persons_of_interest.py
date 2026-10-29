#!/usr/bin/env python3

class Scientist:                                # 1. สร้างคลาสสำหรับเป็นพิมพ์เขียวของข้อมูลนักวิทยาศาสตร์
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

class PersonsOfInterest:                        # 2. สร้างคลาสหลักสำหรับจัดการข้อมูลและการแสดงผลตามโจทย์
    def famous_births(self, figures_dict):
        if not figures_dict:                    # หากไม่มีข้อมูลใน dictionary ให้จบการทำงาน
            return

        scientists_list = []                    # แปลงข้อมูลจาก Dictionary ย่อยให้กลายเป็น Object ของคลาส Scientist
        for key, info in figures_dict.items():  # สร้าง object จากข้อมูล name และ date_of_birth
            scientist = Scientist(info["name"], info["date_of_birth"])
            scientists_list.append(scientist)

                                                                    # เรียงลำดับข้อมูลตามวันเกิด (date_of_birth) จากน้อยไปมาก
                                                                    # ใช้ int() ช่วยแปลงข้อความปี ค.ศ. เช่น "1815" ให้เป็นตัวเลขก่อนนำไปเรียง
        scientists_list.sort(key=lambda x: int(x.date_of_birth))

        for s in scientists_list:                                   # แสดงผลลัพธ์ตามรูปแบบที่โจทย์กำหนด
            print(f"{s.name} is a great scientist born in {s.date_of_birth}.")

                                                                    # --- ส่วนทดสอบโค้ดตามโจทย์ (สามารถคัดลอกไปวางเพื่อรันดูผลลัพธ์ได้) ---
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

manager = PersonsOfInterest()                   # สร้าง Object จากคลาสหลักและเรียกใช้งาน Method
manager.famous_births(women_scientists)




'''
========================== การสร้าง  ==========================

อธิบายการทำงานและ Syntax โดยละเอียด

1. การสร้างคลาส (class และ __init__)

• Syntax: class Scientist:
	• คำอธิบาย: class คือการสร้าง "พิมพ์เขียว (Blueprint)" หรือแม่แบบ 
      เพื่อระบุว่าวัตถุ (Object) ที่เราจะสร้างขึ้นมานั้นต้องมีคุณสมบัติอะไรบ้าง

• Syntax: def __init__(self, name, date_of_birth):
	• คำอธิบาย: __init__ ย่อมาจาก Initialize (แปลว่า การกำหนดค่าเริ่มต้น) 
      มันคือฟังก์ชันพิเศษที่จะทำงานทันทีที่เราสร้างวัตถุชิ้นใหม่ขึ้นมา
	• คำอธิบาย: self ย่อมาจาก ตัวมันเอง ใช้เพื่ออ้างอิงถึงวัตถุตัวนั้น ๆ 
      เช่น self.name = name หมายถึงการนำข้อมูลชื่อที่ส่งเข้ามา ไปบันทึกเก็บไว้ในตัวของวัตถุชิ้นนั้น

2. การดึงข้อมูลออกมาแกะกล่อง (.items())

• Syntax: figures_dict.items()
	• คำอธิบาย: .items() เป็นคำสั่งดึงข้อมูลใน Dictionary ออกมาทีละคู่พร้อมกัน ทั้ง คีย์ (Key) และ มูลค่า (Value)
	• การใช้งาน: ในลูป for key, info in ... ตัวแปร key จะเก็บคำสั้น ๆ (เช่น "ada") 
      ส่วน info จะเก็บ Dictionary ย่อยข้างในทั้งหมด (เช่น { "name": "Ada Lovelace", ... }) 
      ทำให้เราเอาไปสร้างเป็นตัวแปรแบบ Class ได้ง่าย

3. การเรียงลำดับด้วย Lambda (.sort(key=lambda x: ...))

• Syntax: .sort()
	• คำอธิบาย: ย่อมาจาก Sorting (การจัดเรียงลำดับ) 
      เป็นคำสั่งสำหรับจัดเรียงข้อมูลใน List จากน้อยไปมาก

• Syntax: key=lambda x: int(x.date_of_birth)
	• คำอธิบาย: lambda ย่อมาจาก Lambda Function 
      คือการเขียนฟังก์ชันสั้น ๆ แบบบรรทัดเดียว (Anonymous Function) โดยไม่ต้องตั้งชื่อฟังก์ชัน
	• การใช้งาน: ในที่นี้เราบอกคอมพิวเตอร์ว่า 
      "เวลาจะเรียงลำดับวัตถุแต่ละชิ้น (x) ให้นำตัวแปรวันเกิด (x.date_of_birth) 
      แปลงเป็นตัวเลขด้วย int() แล้วใช้ตัวเลขปี ค.ศ. นั้นเป็นเกณฑ์ในการเรียงจากปีที่เก่าที่สุดไปหาปีล่าสุด"







==============================================================================
'''


