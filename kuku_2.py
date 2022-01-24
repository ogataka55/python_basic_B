number_i = int(input("行数を入力してください: "))
number_j = int(input("列数を入力してください: "))

for i in range(1, number_i + 1):
    for j in range(1, number_j + 1):
        print(i * j, end=' ')
    print()
