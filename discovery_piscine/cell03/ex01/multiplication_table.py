#!/usr/bin/env python3
import sys

def main():
                                    # 1. ตรวจสอบจำนวน Parameter ที่ส่งเข้ามา (sys.argv)
                                    # sys.argv[0] คือชื่อไฟล์ ดังนั้นถ้าส่ง string มา 1 ตัว len(sys.argv) ต้องเท่ากับ 2
    if len(sys.argv) != 2:
        print("none")
        return

                                    # 2. ดึงข้อความจาก parameter ตัวแรกมาใช้งาน
    input_string = sys.argv[1]
    
                                    # 3. นับจำนวนตัวอักษร 'z' (พิมพ์เล็กเท่านั้นตามตัวอย่างโจทย์)
    z_count = input_string.count('z')
    
                                    # 4. แสดงผลลัพธ์ตามเงื่อนไข
    if z_count == 0:
        print("none")
    else:
                                    # พิมพ์ตัว 'z' ซ้ำกันตามจำนวนที่นับได้ (เช่น 'z' * 3 จะได้ 'zzz')
        print('z' * z_count)

if __name__ == '__main__':
    main()





'''
for i in range(0,10):
    print(f"{multiplier} x {num_input} = {multiplier * num_input}")

'''



'''
print(num_input)
while i<=9:
    print(f"{multiplier} x {num_input}, = , {multiplier * num_input}")
    i+1
'''


