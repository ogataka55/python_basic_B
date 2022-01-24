# 二重ループ
# endはデータを出力した後(末尾)に出力するものを指定 ※' 'は改行無しで出力

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print()  # iループの値が1増える毎に改行
