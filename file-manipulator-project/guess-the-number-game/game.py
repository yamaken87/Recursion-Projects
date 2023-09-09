import random

def check_answer(answer, r):
    if answer == r:
        print("正解です！")
        exit()
    elif answer > r:
        print("答えはもっと小さいです。")
    elif answer < r:
        print("答えはもっと大きいです。")

print("Welcome to the Guess the Number Game!")
print("最小値と最大値を入力し、その間で数字をあててください。")
minimum_input = int(input("まず、最小値を入力してください: "))
maximum_input = int(input("次に、最大値を入力してください: "))

if minimum_input > maximum_input:
    print("最小値は最大値よりも小さくなければなりません。")
    exit()

r = random.randint(minimum_input, maximum_input)

print("10回まで回答できます。")
for i in range(1, 11):
    check_answer(int(input(f"{i}回目: ")), r)