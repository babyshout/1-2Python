# sys2.py
import sys
args = sys.argv[1:]
for i in args:
    # upper() -> , 같은 특수문자는 무시함 신기
    print(i.upper(), end=' ')
