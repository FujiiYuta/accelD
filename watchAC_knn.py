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
'''
print("----------------")
print("train_label")
print(train_label)
print("----------------")
print("test_label")
print(test_label)
print("----------------")
'''
# 次回呼び出し
# train_data, train_label, test_data, test_label = np.load('dataset.npy')

# ここまででデータセットの準備は終了
# やっと機械学習のフェーズへ
# sklearnを用いて、knnで機械学習
# その前にカラーマップ

import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib.colors import ListedColormap
from sklearn import neighbors, metrics

# カラーマップの作成
cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

# 変数の設定
h = 0.1 # とりあえずメッシュサイズは0.1でいこう
k_list = [1, 5, 10, 30] # いろんなkの数で試す
weights_list = ['uniform', 'distance']
'''
uniform : データ間の距離に寄らず一様な重みを与える。デフォルト
distance : 距離が近いデータほどその影響が大きくなるよう、距離に反比例して重みが与えられる
他にも変数はあるらしい
'''
score = np.zeros((len(k_list)*2, 5)) # scoreってなんだ

# 学習
train_ft = np.ravel(train_label)
test_ft = np.ravel(test_label)
test_dt = np.ravel(test_data)

print("----------------")
print("train_ft")
print(train_ft)
print("----------------")
print("test_ft")
print(test_ft)
print("----------------")
print("test_dt")
print(test_dt)
print("----------------")

plt.figure(figsize=(8*len(k_list), 12))
i = 1 #subplot用
for weights in weights_list:
    for k in k_list:
        clf = neighbors.KNeighborsClassifier(k, weights = weights)
        
        clf.fit(test_data, test_ft)
        x1_min, x1_max = train_data[:, 0].min() - 1, train_data[:, 0].max() + 1 # train_dataの1次元目の最小と最大を取得
        x2_min, x2_max = train_data[:, 1].min() - 1, train_data[:, 1].max() + 1 # train_dataの2次元目の最小と最大を取得
        x3_min, x3_max = train_data[:, 2].min() - 1, train_data[:, 2].max() + 1 # train_dataの3次元目の最小と最大を取得

        # x1_min から x1_maxまで、x2_min から x2_maxまで、x3_min からx3_maxまでのh刻みの等間隔な格子状配列を生成
        xx1, xx2, xx3 = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h), np.arange(x3_min, x3_max, h))

        # メッシュ状の各点に対して予測 / .ravel()で1次元配列に変換し、np.c_[]でxx1, xx2, xx3を結合
        Z = clf.predict(np.c_[xx1.ravel(), xx2.ravel(), xx3.ravel()])
        Z = Z.reshape(xx1.shape) # 配列形式変更
        plt.subplot(2, len(k_list), i) #2行 x k_list列のグラフのi番目のグラフに
        plt.pcolormesh(xx1, xx2, xx3, Z, cmap=cmap_light) # 学習結果をプロット
        plt.scatter(train_data[:, 0], train_data[:, 1], train_data[:, 2], c=train_ft, cmap=cmap_bold) #教師データをプロット
        plt.scatter(test_data[:, 0], test_data[:, 1], test_data[:, 2], c=test_ft, cmap=cmap_light) #テストデータをプロット
        plt.xlim(xx1.min(), xx2.min(), xx3.min())
        plt.ylim(xx1.max(), xx3.max(), xx3.max())
        plt.title("k = %i, weights = '%s'" % (k, weights), fontsize=30)
        score[i-1,3] = k
        score[i-1,0] = metrics.f1_score(test_label, clf.predict(test_data), average='weighted')
        score[i-1,1] = metrics.precision_score(test_label, clf.predict(test_data))
        score[i-1,2] = metrics.recall_score(test_label, clf.predict(test_data))
        i = i + 1
plt.show()

# これは参考文献が難しすぎたからぼつ
