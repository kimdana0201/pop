coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print(f"거스름돈 {money - 300}을 드리고 커피를 줍니다.")
        coffee = coffee -1
    else: 
        print("돈이 부족합니다. 커피를 드리지 않습니다.")
        print(f"남은 커피 양은 {coffee -1}개 입니다.")
    if coffee == 0:
        print("남은 커피가 없습니다. 판매를 중지 합니다.")
        break
