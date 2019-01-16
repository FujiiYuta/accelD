import numpy as np
# accelD_dataset.pyから配列だけ持ってくる
import accelD_dataset
wave_raw = accelD_dataset.wave
shake_raw = accelD_dataset.shake
none_raw = accelD_dataset.none
# print(shake)

# 0または1,2の配列を作成
# 0 : none
# 1 : shake
# 2 : wave

a = np.full((50, 1), 0, dtype = 'int32')
b = np.full((50, 1), 1, dtype = 'int32')
c = np.full((50, 1), 2, dtype = 'int32')

# 作成した配列と生データの配列を結合(0,1,2のどれかを4列めに追加する)
# これがラベル付け
none = np.hstack((none_raw, a))
shake = np.hstack((shake_raw, b))
wave = np.hstack((wave_raw, c))

# none, shake, waveを一つのdatasetにまとめる
# appendでもいいと思うけど、vstackしたほうが早いんじゃない？
dataset = np.vstack((none, shake, wave))

# datasetをランダムにシャッフル
np.random.shuffle(dataset)

# trainとtestに分割(train_data : test_data = 7 : 3)
# 50*3*7/10 =105
train = dataset[:105]
test = dataset[105:]

# trainとtestに分割(縦方向に分割 -> axis=1)
train_data, train_label = np.split(train, [-1], axis=1)
test_data, test_label = np.split(test, [-1], axis=1)

# datasetの保存
x = (train_data, train_label, test_data, test_label)
np.save('dataset.npy', x)

# dataの数をそれぞれ出力
print("train_data", "test_data")
print(len(train_data), len(test_data))

# 次回呼び出し
# train_data, train_label, test_data, test_label = np.load('dataset.npy')

# データセットの準備完了

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
'''
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(train_data, train_label)
clf.score(test_data, test_label)
'''

train_data = train_data.astype(np.float64)
train_label = train_label.astype(np.float64)
test_data = test_data.astype(np.float64)
test_label = test_label.astype(np.float64)
# エラー出たからtrain_labelとtest_labeを整形
print(train_label)
train_ft = np.ravel(train_label)
print(train_ft)
test_ft = np.ravel(test_label)
accurate = []
k_range = []

for k in range(1, 90):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_data, train_ft)
    score = knn.score(test_data, test_ft)
    accurate.append(score)
    k_range.append(k)
    plt.plot(k_range, accurate)

plt.show()
