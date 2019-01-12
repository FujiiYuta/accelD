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
a = np.full((522, 1), 0, dtype='int32')
b = np.full((332, 1), 1, dtype='int32')

# 作成した配列とf,gを結合させる(0または1のカラムを4行目に追加する)
shake = np.hstack((f, a))
wave = np.hstack((g, b))

#shakeとwaveを一つのdatasetにまとめる
dataset = shake
dataset = np.append(dataset, wave, axis=0)
# これってdataset = np.append(shake, waveと同義じゃないの？

#datasetをランダムに並び替える
np.random.shuffle(dataset)

# trainとtestに分割(train_data : test_data = 7 : 3)
# つまり, (522+332)*7/10 = (about)598
train = dataset[:588]
test = dataset[598:]

# dataとlabelに分割
# [-1]は「最後の要素」という意味
# axisはなんかよくわからなかった
# 座標軸、ということらしい
# 1は横方向(つまり二次元配列を縦線で割るということ
train_data, train_label = np.split(train, [-1], axis=1)
test_data, test_label = np.split(test, [-1], axis=1)

# datasetの保存

x = (train_data, train_label, test_data, test_label)
np.save('dataset.npy', x)

#dataの数をそれぞれ出力
print("train_data", "test_data")
print(len(train_data), len(test_data))
# print("train_label", "test_label")
# print(train_label,test_label)
# 次回呼び出し
# train_data, train_label, test_data, test_label = np.load('dataset.npy')

# ここまででデータセットの準備は終了
# やっと機械学習のフェーズへ
# sklearnを用いて、knnで機械学習
# その前にカラーマップ
import pandas as pd
from pandas.plotting import scatter_matrix
import mglearn
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib.colors import ListedColormap
from sklearn import neighbors, metrics
'''
# カラーマップの作成
cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

# 変数の設定
h = 0.1 # とりあえずメッシュサイズは0.1でいこう
k_list = [1, 5, 10, 30] # いろんなkの数で試す
weights_list = ['uniform', 'distance']
'''
'''
uniform : データ間の距離に寄らず一様な重みを与える。デフォルト
distance : 距離が近いデータほどその影響が大きくなるよう、距離に反比例して重みが与えられる
他にも変数はあるらしい
'''
'''
score = np.zeros((len(k_list)*2, 5)) # scoreってなんだ

# 学習

plt.figure(figsize=(8*len(k_list), 12))
i = 1 #subplot用
for weights in weights_list:
    for k in k_list:
        clf = neighbors.KNeighborsClassifier(k, weights = weights)
        clf.fit(test_data, test_label)
        x1_min, x1_max = 
'''
print(train_data.shape)
print(test_data.shape)
accelD_dataframe = pd.DataFrame(train_data)
print(accelD_dataframe.head(30))
# print(train_label)
print(np.ravel(train_label))
train_ft = np.ravel(train_label)
grr = pd.plotting.scatter_matrix(accelD_dataframe, figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=8, cmap=mglearn.cm3, c=train_ft)
plt.show()
