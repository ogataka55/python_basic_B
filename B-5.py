# split()関数は文字列を指定した内容でリスト分割
# inputの入力値はstr型 ⇒ map関数で型変換(int型へ)
# その後list()関数でmapオブジェクトをリスト化
input_n = list(map(int, input("データを入力してください(スペース区切り) > ").split()))


def sum_val():
    sum_n = 0
    for n in input_n:
        sum_n += n
    return sum_n


def max_val():
    max_n = input_n[0]
    for n in input_n:
        if n > max_n:
            max_n = n
    return max_n


def min_val():
    min_n = input_n[0]
    for n in input_n:
        if n < min_n:
            min_n = n
    return min_n


def ave_val():
    ave = sum_val() / len(input_n)
    return format(ave, '.2f')  # 小数点第2位まで表示


print(f"合計値: {sum_val()}")
print(f"最大値: {max_val()}")
print(f"最小値: {min_val()}")
print(f"平均値: {ave_val()}")
