def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    from statistics import mean
    all_temp = [temp['temperature'] for temp in weather_information]  # リスト内包表記
    print(mean(all_temp))  # 標準ライブラリstatisticsのmean関数

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_sta = [sta['station'] for sta in weather_information if sta['prefecture'] == '大阪府']  # リスト内包表記+条件指定
    print(*osaka_sta, sep=',')  # sepオプションは区切り文字を設定

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    from statistics import mean
    fukuoka_temp = [temp['temperature'] for temp in weather_information if temp['prefecture'] == '福岡県']
    print(mean(fukuoka_temp))


if __name__ == '__main__':
    # 「モジュールを直接実行したい時だけ、実行したいコード」をifブロックの中に記述
    main()
