def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    L = [] #基準値より小さい値を格納
    R = [] #基準値より大きい値を格納
    start = 0 #前からの探索位置
    end = len(array) - 1 #後ろからの探索位置
    #探索位置が交差していないなら処理を続ける
    while start < end:
        #探索対象が基準値より小さいならばLに格納し探索位置を進める
        while array[start] < pivot:
            L.append(array[start])
            start += 1
        #同様に基準値より大きいならばRに格納し探索位置を進める
        while array[end] > pivot:
            R.append(array[end])
            end -= 1
        #前からの探索で見つかった基準値以上の対象と
        # 後ろからの探索で見つかった基準値以下の値を交換
        if start < end: 
            array[start], array[end] = array[end], array[start]
            L.append(array[start])
            R.append(array[end])
            start += 1
            end -= 1
        #探索位置が交差したときその探索対象をLとRどちらに格納するのかの判定
        if start == end:
            if array[end] >= pivot:
                R.append(array[end])
            else:
                L.append(array[end])
    #リストが０でエラーにならないように長さ０以上の時に処理を実行
    if len(L) > 0:
       L = sort(L)
    if len(R) > 0:
       R = sort(R)
   
    return L + R

    # ここまで記述

if __name__ == '__main__':
    main()