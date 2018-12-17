'''
irisのサンプルでは説明変数1行に対して目的変数が1個だったが、
今回は時系列データなので二次元配列として格納して1個の目的変数をつける
X = shake.data      # 説明変数
Y = shake.target    # 目的変数
'''
import numpy as np
# データの読み込み及び配列に変換
f = np.loadtxt('shake1.csv', delimiter=',')
f2 = np.loadtxt('wave1.csv', delimiter=',')
'''
# 配列の保存
np.save('shake1.npy', f)
np.save('wave1.npy', g)
'''
print(f)

