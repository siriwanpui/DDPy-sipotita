#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามีการใส่ Argument เพิ่มเติมเข้ามาหรือไม่ ถ้ามีให้พิมพ์ "none"
    if len(sys.argv) > 1:
        print("none")
        return

    i = 0
    while i <= 10:                         # ลูปนอก: ควบคุมแม่สูตรคูณ (จาก 0 ถึง 10)
        line = f"Table de {i}:"
        
        j = 0
        while j <= 10:                      # ลูปใน: ควบคุมตัวคูณตั้งแต่ 0 ถึง 10
            line += f" {i * j}"
            j += 1
            
        print(line)
        i += 1

if __name__ == "__main__":
    main()