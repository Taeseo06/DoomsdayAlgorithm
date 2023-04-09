# 이 파일은 콘웨이의 둠스데이 알고리즘을 파이썬으로 구현한 소스코드입니다.
import sys
y, m, d = map(int, sys.stdin.readline().rstrip().split())

dic = {'1': 0, '2': 0, '3': 21, '4': 4, '5': 9, '6': 6, '7': 11, '8': 8, '10': 10, '11': 7, '9': 5, '12': 12 }
dic2 = {1: "월요일", 2: "화요일", 3: "수요일", 4: "목요일", 5: "금요일", 6: "토요일", 7: "일요일", 0: "일요일"}

if (y % 4 == 0) and (y % 100 == 0): # 윤년
    print("윤년")
    dic['1'] = 4; dic['2'] = 29
else: # 평년
    print("평년")
    dic['1'] = 3; dic['2'] = 28

if y >= 2100:
    print("일요일")
    std = 7
elif y >= 2000:
    print("화요일")
    std = 2
elif y >= 1900:
    print("수요일")
    std = 3
elif y >= 1800:
    print("금요일")
    std = 5
dooms = (std + ((y % 100) // 12) + ((y % 100) % 12) + ((y % 100) % 12 // 4)) % 7 # (기준일 + A + B + C) % 7

same_d = dic.get(str(m))

Day = d - same_d

print(f'{y}년 {m}월 {d}일은 {dic2.get((dooms + Day) % 7)} 입니다.')
