"""
classを使った画面設計

"""
from tk_class import *

def main():
    main_s = MainScreen("メイン画面",300,250)
    bt_lis = []
    for i in range(3):
        bt_lis.append(main_s.bt_set(f"ボタン{i+1}",75,50+50*i,20))

    for i, bt in enumerate(bt_lis, 1):
        main_s.set_action(bt, lambda a=i:print(a))  #iを引数に直接入れるとiの最大値が表示されるため、一旦aに代入する

    # for i, bt in enumerate(bt_lis, 1):
    #     main_s.set_action(bt, test(i))  #上記ループと同じ、ただ下記クロージャも書く必要があるので、lambdaで書いたほうが短い

def test(a):
    def inner():
        print(a)
    return inner



main()
mainloop()