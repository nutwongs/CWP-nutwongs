#!/usr/bin/env python3
import sys

# sys.argv[0] คือชื่อไฟล์ ดังนั้นพารามิเตอร์จริงคือนับจากตำแหน่งที่ 1 เป็นต้นไป
if len(sys.argv) < 3:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)