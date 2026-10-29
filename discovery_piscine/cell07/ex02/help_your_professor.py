#!/usr/bin/env python3

def average(scores_dict):
    if not scores_dict:     # ตรวจสอบก่อนว่า dictionary ไม่ว่าง เพื่อป้องกันข้อผิดพลาด ZeroDivisionError
        return 0.0
    
    total_score = sum(scores_dict.values())             # 1. รวมคะแนนทั้งหมดใน dictionary
    number_of_students = len(scores_dict)               # 2. นับจำนวนนักเรียนทั้งหมดใน dictionary
    class_average = total_score / number_of_students    # 3. คำนวณค่าเฉลี่ย

    return class_average

# --- ส่วนทดสอบโค้ดตามโจทย์ (สามารถคัดลอกไปวางเพื่อรันดูผลลัพธ์ได้) ---
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")





'''
========================== การสร้าง  ==========================

• Syntax: scores_dict.values()
	• คำอธิบาย: .values() เป็น Method ของข้อมูลประเภท Dictionary 
      ใช้สำหรับดึง "ค่า (Values)" ทั้งหมดออกมา (ในที่นี้คือ ดึงเฉพาะตัวเลขคะแนนออกมา 
      เช่น [18, 15, 8, 9] โดยไม่เอาชื่อนักเรียนมาด้วย)

• Syntax: sum(...)
	• คำอธิบาย: sum เป็นฟังก์ชันสำเร็จรูป (Built-in function) ของ Python 
      ย่อมาจาก Summary / Summation (การบวกผลรวม)
	• การใช้งาน: นำไปครอบสิ่งที่ต้องการบวก เช่น sum(scores_dict.values()) 
      จะทำหน้าที่นำคะแนนของทุกคนในคลาสมาบวกกันทั้งหมดทันที

• Syntax: if not ตัวแปร: เพื่อเช็กความว่างเปล่าได้ในรูปแบบเดียวกันเลยครับ
    หมายความว่า var นั้น มีข้อมูลหรือไม่ ไม่ว่าจะเป็น datatype ไหนก็ตาม 
    




==============================================================================
'''


