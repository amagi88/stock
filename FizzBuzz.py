for num in range(1, 101):
    string = ''

    # ここから記述
    #numが15の倍数なら出力
    if num % 3 == 0 and num % 5 == 0: 
        print('FizzBuzz')
    #numが3の倍数かつ5の倍数ではないとき出力
    elif num % 3 == 0: 
        print('Fizz')
    #numが5の倍数かつ3な倍数ではないとき出力
    elif num % 5 == 0: 
        print('Buzz')
    else:
        print(num)

    # ここまで記述

    print(string)