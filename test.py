import pandas as pd
import numpy as np
import csv
import os
os.chdir("wave")
with open('shake_1.csv') as fp:
    sh = list(csv.reader(fp))
with open('shake_2.csv') as fp:
    sh2 = list(csv.reader(fp))
with open('shake_3.csv') as fp:
    sh3 = list(csv.reader(fp))
with open('shake_4.csv') as fp:
    sh4 = list(csv.reader(fp))
with open('shake_5.csv') as fp:
    sh5 = list(csv.reader(fp))
with open('shake_6.csv') as fp:
    sh6 = list(csv.reader(fp))
with open('shake_7.csv') as fp:
    sh7 = list(csv.reader(fp))
with open('shake_8.csv') as fp:
    sh8 = list(csv.reader(fp))
with open('shake_9.csv') as fp:
    sh9 = list(csv.reader(fp))
with open('shake_10.csv') as fp:
    sh10 = list(csv.reader(fp))
with open('shake_11.csv') as fp:
    sh11 = list(csv.reader(fp))
with open('shake_12.csv') as fp:
    sh12 = list(csv.reader(fp))
with open('shake_13.csv') as fp:
    sh13 = list(csv.reader(fp))
with open('shake_14.csv') as fp:
    sh14 = list(csv.reader(fp))
with open('shake_15.csv') as fp:
    sh15 = list(csv.reader(fp))
with open('shake_16.csv') as fp:
    sh16 = list(csv.reader(fp))
with open('shake_17.csv') as fp:
    sh17 = list(csv.reader(fp))
with open('shake_18.csv') as fp:
    sh18 = list(csv.reader(fp))
with open('shake_19.csv') as fp:
    sh19 = list(csv.reader(fp))
with open('shake_20.csv') as fp:
    sh20 = list(csv.reader(fp))
with open('shake_21.csv') as fp:
    sh21 = list(csv.reader(fp))
with open('shake_22.csv') as fp:
    sh22 = list(csv.reader(fp))
with open('shake_23.csv') as fp:
    sh23 = list(csv.reader(fp))
with open('shake_24.csv') as fp:
    sh24 = list(csv.reader(fp))
with open('shake_25.csv') as fp:
    sh25 = list(csv.reader(fp))
with open('shake_26.csv') as fp:
    sh26 = list(csv.reader(fp))
with open('shake_27.csv') as fp:
    sh27 = list(csv.reader(fp))
with open('shake_28.csv') as fp:
    sh28 = list(csv.reader(fp))
with open('shake_29.csv') as fp:
    sh29 = list(csv.reader(fp))
with open('shake_30.csv') as fp:
    sh30 = list(csv.reader(fp))
with open('shake_31.csv') as fp:
    sh31 = list(csv.reader(fp))
with open('shake_32.csv') as fp:
    sh32 = list(csv.reader(fp))
with open('shake_33.csv') as fp:
    sh33 = list(csv.reader(fp))
with open('shake_34.csv') as fp:
    sh34 = list(csv.reader(fp))
with open('shake_35.csv') as fp:
    sh35 = list(csv.reader(fp))
with open('shake_36.csv') as fp:
    sh36 = list(csv.reader(fp))
with open('shake_37.csv') as fp:
    sh37 = list(csv.reader(fp))
with open('shake_38.csv') as fp:
    sh38 = list(csv.reader(fp))
with open('shake_39.csv') as fp:
    sh39 = list(csv.reader(fp))
with open('shake_40.csv') as fp:
    sh40 = list(csv.reader(fp))
with open('shake_41.csv') as fp:
    sh41 = list(csv.reader(fp))
with open('shake_42.csv') as fp:
    sh42 = list(csv.reader(fp))
with open('shake_43.csv') as fp:
    sh43 = list(csv.reader(fp))
with open('shake_44.csv') as fp:
    sh44 = list(csv.reader(fp))
with open('shake_45.csv') as fp:
    sh45 = list(csv.reader(fp))
with open('shake_46.csv') as fp:
    sh46 = list(csv.reader(fp))
with open('shake_47.csv') as fp:
    sh47 = list(csv.reader(fp))
with open('shake_48.csv') as fp:
    sh48 = list(csv.reader(fp))
with open('shake_49.csv') as fp:
    sh49 = list(csv.reader(fp))
with open('shake_50.csv') as fp:
    sh50 = list(csv.reader(fp))
with open('wave_1.csv') as fp:
    wa = list(csv.reader(fp))
with open('wave_2.csv') as fp:
    wa2 = list(csv.reader(fp))
with open('wave_3.csv') as fp:
    wa3 = list(csv.reader(fp))
with open('wave_4.csv') as fp:
    wa4 = list(csv.reader(fp))
with open('wave_5.csv') as fp:
    wa5 = list(csv.reader(fp))
with open('wave_6.csv') as fp:
    wa6 = list(csv.reader(fp))
with open('wave_7.csv') as fp:
    wa7 = list(csv.reader(fp))
with open('wave_8.csv') as fp:
    wa8 = list(csv.reader(fp))
with open('wave_9.csv') as fp:
    wa9 = list(csv.reader(fp))
with open('wave_10.csv') as fp:
    wa10 = list(csv.reader(fp))
with open('wave_11.csv') as fp:
    wa11 = list(csv.reader(fp))
with open('wave_12.csv') as fp:
    wa12 = list(csv.reader(fp))
with open('wave_13.csv') as fp:
    wa13 = list(csv.reader(fp))
with open('wave_14.csv') as fp:
    wa14 = list(csv.reader(fp))
with open('wave_15.csv') as fp:
    wa15 = list(csv.reader(fp))
with open('wave_16.csv') as fp:
    wa16 = list(csv.reader(fp))
with open('wave_17.csv') as fp:
    wa17 = list(csv.reader(fp))
with open('wave_18.csv') as fp:
    wa18 = list(csv.reader(fp))
with open('wave_19.csv') as fp:
    wa19 = list(csv.reader(fp))
with open('wave_20.csv') as fp:
    wa20 = list(csv.reader(fp))
with open('wave_21.csv') as fp:
    wa21 = list(csv.reader(fp))
with open('wave_22.csv') as fp:
    wa22 = list(csv.reader(fp))
with open('wave_23.csv') as fp:
    wa23 = list(csv.reader(fp))
with open('wave_24.csv') as fp:
    wa24 = list(csv.reader(fp))
with open('wave_25.csv') as fp:
    wa25 = list(csv.reader(fp))
with open('wave_26.csv') as fp:
    wa26 = list(csv.reader(fp))
with open('wave_27.csv') as fp:
    wa27 = list(csv.reader(fp))
with open('wave_28.csv') as fp:
    wa28 = list(csv.reader(fp))
with open('wave_29.csv') as fp:
    wa29 = list(csv.reader(fp))
with open('wave_30.csv') as fp:
    wa30 = list(csv.reader(fp))
with open('wave_31.csv') as fp:
    wa31 = list(csv.reader(fp))
with open('wave_32.csv') as fp:
    wa32 = list(csv.reader(fp))
with open('wave_33.csv') as fp:
    wa33 = list(csv.reader(fp))
with open('wave_34.csv') as fp:
    wa34 = list(csv.reader(fp))
with open('wave_35.csv') as fp:
    wa35 = list(csv.reader(fp))
with open('wave_36.csv') as fp:
    wa36 = list(csv.reader(fp))
with open('wave_37.csv') as fp:
    wa37 = list(csv.reader(fp))
with open('wave_38.csv') as fp:
    wa38 = list(csv.reader(fp))
with open('wave_39.csv') as fp:
    wa39 = list(csv.reader(fp))
with open('wave_40.csv') as fp:
    wa40 = list(csv.reader(fp))
with open('wave_41.csv') as fp:
    wa41 = list(csv.reader(fp))
with open('wave_42.csv') as fp:
    wa42 = list(csv.reader(fp))
with open('wave_43.csv') as fp:
    wa43 = list(csv.reader(fp))
with open('wave_44.csv') as fp:
    wa44 = list(csv.reader(fp))
with open('wave_45.csv') as fp:
    wa45 = list(csv.reader(fp))
with open('wave_46.csv') as fp:
    wa46 = list(csv.reader(fp))
with open('wave_47.csv') as fp:
    wa47 = list(csv.reader(fp))
with open('wave_48.csv') as fp:
    wa48 = list(csv.reader(fp))
with open('wave_49.csv') as fp:
    wa49 = list(csv.reader(fp))
with open('wave_50.csv') as fp:
    wa50 = list(csv.reader(fp))
    
# wa~wa50, sh~sh50まで配列が完成
    
sh = np.array(sh)
sh2 = np.array(sh2)
sh3 = np.array(sh3)
sh4 = np.array(sh4)
sh5 = np.array(sh5)
sh_flat = sh.ravel()
sh2_flat = sh2.ravel()
sh3_flat = sh3.ravel()
sh4_flat = sh4.ravel()
sh5_flat = sh5.ravel()
shake = np.vstack((sh_flat, sh2_flat, sh3_flat, sh4_flat, sh5_flat))
#print(sh)
#print(sh_flat)
print(shake)
