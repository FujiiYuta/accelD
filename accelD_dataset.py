# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import os
os.chdir("shake")
with open('shake_01.csv') as fp:
    sh = list(csv.reader(fp))
with open('shake_02.csv') as fp:
    sh2 = list(csv.reader(fp))
with open('shake_03.csv') as fp:
    sh3 = list(csv.reader(fp))
with open('shake_04.csv') as fp:
    sh4 = list(csv.reader(fp))
with open('shake_05.csv') as fp:
    sh5 = list(csv.reader(fp))
with open('shake_06.csv') as fp:
    sh6 = list(csv.reader(fp))
with open('shake_07.csv') as fp:
    sh7 = list(csv.reader(fp))
with open('shake_08.csv') as fp:
    sh8 = list(csv.reader(fp))
with open('shake_09.csv') as fp:
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
os.chdir('../wave')
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

os.chdir('../none')
with open('none_1.csv') as fp:
    no= list(csv.reader(fp))
with open('none_2.csv') as fp:
    no2 = list(csv.reader(fp))
with open('none_3.csv') as fp:
    no3 = list(csv.reader(fp))
with open('none_4.csv') as fp:
    no4 = list(csv.reader(fp))
with open('none_5.csv') as fp:
    no5 = list(csv.reader(fp))
with open('none_6.csv') as fp:
    no6 = list(csv.reader(fp))
with open('none_7.csv') as fp:
    no7 = list(csv.reader(fp))
with open('none_8.csv') as fp:
    no8 = list(csv.reader(fp))
with open('none_9.csv') as fp:
    no9 = list(csv.reader(fp))
with open('none_10.csv') as fp:
    no10 = list(csv.reader(fp))
with open('none_11.csv') as fp:
    no11 = list(csv.reader(fp))
with open('none_12.csv') as fp:
    no12 = list(csv.reader(fp))
with open('none_13.csv') as fp:
    no13 = list(csv.reader(fp))
with open('none_14.csv') as fp:
    no14 = list(csv.reader(fp))
with open('none_15.csv') as fp:
    no15 = list(csv.reader(fp))
with open('none_16.csv') as fp:
    no16 = list(csv.reader(fp))
with open('none_17.csv') as fp:
    no17 = list(csv.reader(fp))
with open('none_18.csv') as fp:
    no18 = list(csv.reader(fp))
with open('none_19.csv') as fp:
    no19 = list(csv.reader(fp))
with open('none_20.csv') as fp:
    no20 = list(csv.reader(fp))
with open('none_21.csv') as fp:
    no21 = list(csv.reader(fp))
with open('none_22.csv') as fp:
    no22 = list(csv.reader(fp))
with open('none_23.csv') as fp:
    no23 = list(csv.reader(fp))
with open('none_24.csv') as fp:
    no24 = list(csv.reader(fp))
with open('none_25.csv') as fp:
    no25 = list(csv.reader(fp))
with open('none_26.csv') as fp:
    no26 = list(csv.reader(fp))
with open('none_27.csv') as fp:
    no27 = list(csv.reader(fp))
with open('none_28.csv') as fp:
    no28 = list(csv.reader(fp))
with open('none_29.csv') as fp:
    no29 = list(csv.reader(fp))
with open('none_30.csv') as fp:
    no30 = list(csv.reader(fp))
with open('none_31.csv') as fp:
    no31 = list(csv.reader(fp))
with open('none_32.csv') as fp:
    no32 = list(csv.reader(fp))
with open('none_33.csv') as fp:
    no33 = list(csv.reader(fp))
with open('none_34.csv') as fp:
    no34 = list(csv.reader(fp))
with open('none_35.csv') as fp:
    no35 = list(csv.reader(fp))
with open('none_36.csv') as fp:
    no36 = list(csv.reader(fp))
with open('none_37.csv') as fp:
    no37 = list(csv.reader(fp))
with open('none_38.csv') as fp:
    no38 = list(csv.reader(fp))
with open('none_39.csv') as fp:
    no39 = list(csv.reader(fp))
with open('none_40.csv') as fp:
    no40 = list(csv.reader(fp))
with open('none_41.csv') as fp:
    no41 = list(csv.reader(fp))
with open('none_42.csv') as fp:
    no42 = list(csv.reader(fp))
with open('none_43.csv') as fp:
    no43 = list(csv.reader(fp))
with open('none_44.csv') as fp:
    no44 = list(csv.reader(fp))
with open('none_45.csv') as fp:
    no45 = list(csv.reader(fp))
with open('none_46.csv') as fp:
    no46 = list(csv.reader(fp))
with open('none_47.csv') as fp:
    no47 = list(csv.reader(fp))
with open('none_48.csv') as fp:
    no48 = list(csv.reader(fp))
with open('none_49.csv') as fp:
    no49 = list(csv.reader(fp))
with open('none_50.csv') as fp:
    no50 = list(csv.reader(fp))

# wa~wa50, sh~sh50, no~no50まで配列が完成

sh = np.array(sh)
sh2 = np.array(sh2)
sh3 = np.array(sh3)
sh4 = np.array(sh4)
sh5 = np.array(sh5)
sh6 = np.array(sh6)
sh7 = np.array(sh7)
sh8 = np.array(sh8)
sh9 = np.array(sh9)
sh10 = np.array(sh10)
sh11 = np.array(sh11)
sh12 = np.array(sh12)
sh13 = np.array(sh13)
sh14 = np.array(sh14)
sh15 = np.array(sh15)
sh16 = np.array(sh16)
sh17 = np.array(sh17)
sh18 = np.array(sh18)
sh19 = np.array(sh19)
sh20 = np.array(sh20)
sh21 = np.array(sh21)
sh22 = np.array(sh22)
sh23 = np.array(sh23)
sh24 = np.array(sh24)
sh25 = np.array(sh25)
sh26 = np.array(sh26)
sh27 = np.array(sh27)
sh28 = np.array(sh28)
sh29 = np.array(sh29)
sh30 = np.array(sh30)
sh31 = np.array(sh31)
sh32 = np.array(sh32)
sh33 = np.array(sh33)
sh34 = np.array(sh34)
sh35 = np.array(sh35)
sh36 = np.array(sh36)
sh37 = np.array(sh37)
sh38 = np.array(sh38)
sh39 = np.array(sh39)
sh40 = np.array(sh40)
sh41 = np.array(sh41)
sh42 = np.array(sh42)
sh43 = np.array(sh43)
sh44 = np.array(sh44)
sh45 = np.array(sh45)
sh46 = np.array(sh46)
sh47 = np.array(sh47)
sh48 = np.array(sh48)
sh49 = np.array(sh49)
sh50 = np.array(sh50)

wa = np.array(wa)
wa2 = np.array(wa2)
wa3 = np.array(wa3)
wa4 = np.array(wa4)
wa5 = np.array(wa5)
wa6 = np.array(wa6)
wa7 = np.array(wa7)
wa8 = np.array(wa8)
wa9 = np.array(wa9)
wa10 = np.array(wa10)
wa11 = np.array(wa11)
wa12 = np.array(wa12)
wa13 = np.array(wa13)
wa14 = np.array(wa14)
wa15 = np.array(wa15)
wa16 = np.array(wa16)
wa17 = np.array(wa17)
wa18 = np.array(wa18)
wa19 = np.array(wa19)
wa20 = np.array(wa20)
wa21 = np.array(wa21)
wa22 = np.array(wa22)
wa23 = np.array(wa23)
wa24 = np.array(wa24)
wa25 = np.array(wa25)
wa26 = np.array(wa26)
wa27 = np.array(wa27)
wa28 = np.array(wa28)
wa29 = np.array(wa29)
wa30 = np.array(wa30)
wa31 = np.array(wa31)
wa32 = np.array(wa32)
wa33 = np.array(wa33)
wa34 = np.array(wa34)
wa35 = np.array(wa35)
wa36 = np.array(wa36)
wa37 = np.array(wa37)
wa38 = np.array(wa38)
wa39 = np.array(wa39)
wa40 = np.array(wa40)
wa41 = np.array(wa41)
wa42 = np.array(wa42)
wa43 = np.array(wa43)
wa44 = np.array(wa44)
wa45 = np.array(wa45)
wa46 = np.array(wa46)
wa47 = np.array(wa47)
wa48 = np.array(wa48)
wa49 = np.array(wa49)
wa50 = np.array(wa50)

no = np.array(no)
no2 = np.array(no2)
no3 = np.array(no3)
no4 = np.array(no4)
no5 = np.array(no5)
no6 = np.array(no6)
no7 = np.array(no7)
no8 = np.array(no8)
no9 = np.array(no9)
no10 = np.array(no10)
no11 = np.array(no11)
no12 = np.array(no12)
no13 = np.array(no13)
no14 = np.array(no14)
no15 = np.array(no15)
no16 = np.array(no16)
no17 = np.array(no17)
no18 = np.array(no18)
no19 = np.array(no19)
no20 = np.array(no20)
no21 = np.array(no21)
no22 = np.array(no22)
no23 = np.array(no23)
no24 = np.array(no24)
no25 = np.array(no25)
no26 = np.array(no26)
no27 = np.array(no27)
no28 = np.array(no28)
no29 = np.array(no29)
no30 = np.array(no30)
no31 = np.array(no31)
no32 = np.array(no32)
no33 = np.array(no33)
no34 = np.array(no34)
no35 = np.array(no35)
no36 = np.array(no36)
no37 = np.array(no37)
no38 = np.array(no38)
no39 = np.array(no39)
no40 = np.array(no40)
no41 = np.array(no41)
no42 = np.array(no42)
no43 = np.array(no43)
no44 = np.array(no44)
no45 = np.array(no45)
no46 = np.array(no46)
no47 = np.array(no47)
no48 = np.array(no48)
no49 = np.array(no49)
no50 = np.array(no50)


sh_flat = sh.ravel()
sh2_flat = sh2.ravel()
sh3_flat = sh3.ravel()
sh4_flat = sh4.ravel()
sh5_flat = sh5.ravel()
sh6_flat = sh6.ravel()
sh7_flat = sh7.ravel()
sh8_flat = sh8.ravel()
sh9_flat = sh9.ravel()
sh10_flat = sh10.ravel()
sh11_flat = sh11.ravel()
sh12_flat = sh12.ravel()
sh13_flat = sh13.ravel()
sh14_flat = sh14.ravel()
sh15_flat = sh15.ravel()
sh16_flat = sh16.ravel()
sh17_flat = sh17.ravel()
sh18_flat = sh18.ravel()
sh19_flat = sh19.ravel()
sh20_flat = sh20.ravel()
sh21_flat = sh21.ravel()
sh22_flat = sh22.ravel()
sh23_flat = sh23.ravel()
sh24_flat = sh24.ravel()
sh25_flat = sh25.ravel()
sh26_flat = sh26.ravel()
sh27_flat = sh27.ravel()
sh28_flat = sh28.ravel()
sh29_flat = sh29.ravel()
sh30_flat = sh30.ravel()
sh31_flat = sh31.ravel()
sh32_flat = sh32.ravel()
sh33_flat = sh33.ravel()
sh34_flat = sh34.ravel()
sh35_flat = sh35.ravel()
sh36_flat = sh36.ravel()
sh37_flat = sh37.ravel()
sh38_flat = sh38.ravel()
sh39_flat = sh39.ravel()
sh40_flat = sh40.ravel()
sh41_flat = sh41.ravel()
sh42_flat = sh42.ravel()
sh43_flat = sh43.ravel()
sh44_flat = sh44.ravel()
sh45_flat = sh45.ravel()
sh46_flat = sh46.ravel()
sh47_flat = sh47.ravel()
sh48_flat = sh48.ravel()
sh49_flat = sh49.ravel()
sh50_flat = sh50.ravel()

wa_flat = wa.ravel()
wa2_flat = wa2.ravel()
wa3_flat = wa3.ravel()
wa4_flat = wa4.ravel()
wa5_flat = wa5.ravel()
wa6_flat = wa6.ravel()
wa7_flat = wa7.ravel()
wa8_flat = wa8.ravel()
wa9_flat = wa9.ravel()
wa10_flat = wa10.ravel()
wa11_flat = wa11.ravel()
wa12_flat = wa12.ravel()
wa13_flat = wa13.ravel()
wa14_flat = wa14.ravel()
wa15_flat = wa15.ravel()
wa16_flat = wa16.ravel()
wa17_flat = wa17.ravel()
wa18_flat = wa18.ravel()
wa19_flat = wa19.ravel()
wa20_flat = wa20.ravel()
wa21_flat = wa21.ravel()
wa22_flat = wa22.ravel()
wa23_flat = wa23.ravel()
wa24_flat = wa24.ravel()
wa25_flat = wa25.ravel()
wa26_flat = wa26.ravel()
wa27_flat = wa27.ravel()
wa28_flat = wa28.ravel()
wa29_flat = wa29.ravel()
wa30_flat = wa30.ravel()
wa31_flat = wa31.ravel()
wa32_flat = wa32.ravel()
wa33_flat = wa33.ravel()
wa34_flat = wa34.ravel()
wa35_flat = wa35.ravel()
wa36_flat = wa36.ravel()
wa37_flat = wa37.ravel()
wa38_flat = wa38.ravel()
wa39_flat = wa39.ravel()
wa40_flat = wa40.ravel()
wa41_flat = wa41.ravel()
wa42_flat = wa42.ravel()
wa43_flat = wa43.ravel()
wa44_flat = wa44.ravel()
wa45_flat = wa45.ravel()
wa46_flat = wa46.ravel()
wa47_flat = wa47.ravel()
wa48_flat = wa48.ravel()
wa49_flat = wa49.ravel()
wa50_flat = wa50.ravel()

no_flat = no.ravel()
no2_flat = no2.ravel()
no3_flat = no3.ravel()
no4_flat = no4.ravel()
no5_flat = no5.ravel()
no6_flat = no6.ravel()
no7_flat = no7.ravel()
no8_flat = no8.ravel()
no9_flat = no9.ravel()
no10_flat = no10.ravel()
no11_flat = no11.ravel()
no12_flat = no12.ravel()
no13_flat = no13.ravel()
no14_flat = no14.ravel()
no15_flat = no15.ravel()
no16_flat = no16.ravel()
no17_flat = no17.ravel()
no18_flat = no18.ravel()
no19_flat = no19.ravel()
no20_flat = no20.ravel()
no21_flat = no21.ravel()
no22_flat = no22.ravel()
no23_flat = no23.ravel()
no24_flat = no24.ravel()
no25_flat = no25.ravel()
no26_flat = no26.ravel()
no27_flat = no27.ravel()
no28_flat = no28.ravel()
no29_flat = no29.ravel()
no30_flat = no30.ravel()
no31_flat = no31.ravel()
no32_flat = no32.ravel()
no33_flat = no33.ravel()
no34_flat = no34.ravel()
no35_flat = no35.ravel()
no36_flat = no36.ravel()
no37_flat = no37.ravel()
no38_flat = no38.ravel()
no39_flat = no39.ravel()
no40_flat = no40.ravel()
no41_flat = no41.ravel()
no42_flat = no42.ravel()
no43_flat = no43.ravel()
no44_flat = no44.ravel()
no45_flat = no45.ravel()
no46_flat = no46.ravel()
no47_flat = no47.ravel()
no48_flat = no48.ravel()
no49_flat = no49.ravel()
no50_flat = no50.ravel()


shake = np.vstack((sh_flat, sh2_flat, sh3_flat, sh4_flat, sh5_flat, sh6_flat, sh7_flat, sh8_flat, sh9_flat, sh10_flat, sh11_flat, sh12_flat, sh13_flat, sh14_flat, sh15_flat, sh16_flat, sh17_flat, sh18_flat, sh19_flat, sh20_flat, sh21_flat, sh22_flat, sh23_flat, sh24_flat, sh25_flat, sh26_flat, sh27_flat, sh28_flat, sh29_flat, sh30_flat, sh31_flat, sh32_flat, sh33_flat, sh34_flat, sh35_flat, sh36_flat, sh37_flat, sh38_flat, sh39_flat, sh40_flat, sh41_flat, sh42_flat, sh43_flat, sh44_flat, sh45_flat, sh46_flat, sh47_flat, sh48_flat, sh49_flat, sh50_flat ))

wave = np.vstack((wa_flat, wa2_flat, wa3_flat, wa4_flat, wa5_flat, wa6_flat, wa7_flat, wa8_flat, wa9_flat, wa10_flat, wa11_flat, wa12_flat, wa13_flat, wa14_flat, wa15_flat, wa16_flat, wa17_flat, wa18_flat, wa19_flat, wa20_flat, wa21_flat, wa22_flat, wa23_flat, wa24_flat, wa25_flat, wa26_flat, wa27_flat, wa28_flat, wa29_flat, wa30_flat, wa31_flat, wa32_flat, wa33_flat, wa34_flat, wa35_flat, wa36_flat, wa37_flat, wa38_flat, wa39_flat, wa40_flat, wa41_flat, wa42_flat, wa43_flat, wa44_flat, wa45_flat, wa46_flat, wa47_flat, wa48_flat, wa49_flat, wa50_flat ))

none = np.vstack((no_flat, no2_flat, no3_flat, no4_flat, no5_flat, no6_flat, no7_flat, no8_flat, no9_flat, no10_flat, no11_flat, no12_flat, no13_flat, no14_flat, no15_flat, no16_flat, no17_flat, no18_flat, no19_flat, no21_flat, no21_flat, no22_flat, no23_flat, no24_flat, no25_flat, no26_flat, no27_flat, no28_flat, no29_flat, no30_flat, no31_flat, no32_flat, no33_flat, no34_flat, no35_flat, no36_flat, no37_flat, no38_flat, no39_flat, no40_flat, no41_flat, no42_flat, no43_flat, no44_flat, no45_flat, no46_flat, no47_flat, no48_flat, no49_flat, no50_flat ))
#print(sh)
#print(sh_flat)
print(shake)
print(wave)
print(none)
os.chdir('..')
