import pandas as pd

# csvファイルのimportと一緒にカラムを設定
shake = pd.read_csv('shake.csv', names=['userAccelerate.x', 'userAccelerate.y', 'userAccelerate.z'])
print(accelD)

'''
irisのサンプルでは説明変数1行に対して目的変数が1個だったが、
今回は時系列データなので二次元配列として格納して1個の目的変数をつける
X = shake.data      # 説明変数
Y = shake.target    # 目的変数
'''

import numpy as np

#データの読み込み及び配列に変換
f =

