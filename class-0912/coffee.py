# coffee.py

coffee = 10
while True:
    try:
        money = int(input("돈을 넣어주세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee -= 1
        elif money > 300:
            print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
            coffee -= 1
        else:
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print("남은 커피의 양은 %d개 입니다." % coffee)
        if not coffee:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break
    except:
        print("돈이 잘못 들어왔어요...")

# if __name__ == '__main__':
