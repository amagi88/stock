def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    # ここから記述
    
    #探索範囲の始まりの位置
    low = 0 
    #探索範囲の末尾
    high = len(sorted_array) - 1 
    #探索範囲が0になるまで処理を繰り返す
    while low <= high: 
        mid = (low + high) // 2
        num = sorted_array[mid] #探索範囲の真ん中の値
        #値が探索対象と一致したらそのインデックスを返す
        if num == target_number: 
            return mid
        #探索対象が真ん中の値より小さいので探索範囲の末尾を変更            
        elif num > target_number: 
            high = mid-1 
        #探索対象が真ん中の値より大きいので探索範囲の始まりの位置を変更
        else: 
            low = mid + 1 

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()