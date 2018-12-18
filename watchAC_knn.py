'''
irisのサンプルでは説明変数1行に対して目的変数が1個だったが、
今回は時系列データなので二次元配列として格納して1個の目的変数をつける
X = shake.data      # 説明変数
Y = shake.target    # 目的変数
'''
import numpy as np

# データの読み込み及び配列に変換
f = np.loadtxt('shake1.csv', delimiter=',', dtype='int32')
g = np.loadtxt('wave1.csv', delimiter=',', dtype='int32')

# 配列の保存
np.save('shake1.npy', f)
np.save('wave1.npy', g)

# print(f)
# print(g)
# npyの表示はpythonのインタラクティブエディタで確認済

# 0または1の配列を作成
# 0 : shake
# 1 : wave
a = np.full((4, 1), 0, dtype='int32')
b = np.full((4, 1), 1, dtype='int32')

# 作成した配列とf,gを結合させる(0または1の配列を4行目に追加する)
shake = np.hstack((f, a))
wave = np.hstack((g, b))

#shakeとwaveを一つのdatasetにまとめる
dataset = shake
dataset = np.append(dataset, wave, axis=0)
# これってdataset = np.append(shake, waveと同義じゃないの？

#datasetをランダムに並び替える
np.random.shuffle(dataset)

# trainとtestに分割(train_data = 7, test_data = 3)
train = dataset[:7]
test = dataset[7:]

# dataとlabelに分割
