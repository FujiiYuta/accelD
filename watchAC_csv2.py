import pandas as pd
 
# csvファイルのimportと一緒にカラムを設定                                                                                                                  
shake = pd.read_csv('shake1.csv', names=['userAccelerate.x', 'userAccelerate.y', 'userAccelerate.z'])
print(shake)