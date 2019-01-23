# -*- coding: utf-8 -*-

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
train_ft = np.ravel(train_label)
test_ft = np.ravel(test_label)
# データセットの準備完了
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import coremltools
clf = RandomForestClassifier() #random_state=0がいるかわからん

clf.fit(train_data, train_ft) # train_ft作らなきゃダメかも

pre = clf.predict(test_data)

#予測結果の正解率
ac_score = metrics.accuracy_score(test_ft, pre)
print u'正解率',ac_score*100,'%'

#mlmodelに変換

coreml_model = coremltools.converters.sklearn.convert(clf, input_features=None, output_feature_names='gesture')
coreml_model.save('accelD.mlmodel')

# チェック

loaded_model = coremltools.models.MLModel('accelD.mlmodel')

#print loaded_model.get_spec()

