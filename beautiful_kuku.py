number_i = int(input("行数を入力してください: "))
number_j = int(input("列数を入力してください: "))

for i in range(1, number_i + 1):
    for j in range(1, number_j + 1):
        print(f"{j} ✕ {i} = {str(i * j).rjust(2)}", end=' | ')  # 右寄せ.rjust(文字数)は文字列のみ、数値は文字列に変換要
    print()
