# -*- coding: UTF-8 -*-
# 手機共通屬性: price, camera_count, screen_size
# 特殊功能: special_freature() 

# 手機一 google phone:
# price=10, camera_count=3, screen_size=5
# special_freature 輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
# 例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]

# 手機二 taiwan phone:
# price=20, camera_count=1, screen_size=3
# special_freature
# 輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
# 例如: ---

import mobile

print("\n ------MobilePhone------ \n")
print(mobile.MobilePhone(165,54,83).special_freature())

print("\n ------GooglePhone------ \n")
print(mobile.GooglePhone().special_freature([12,3,5,23,61,43,1526,234,457,34,14]))

print("\n ------TaiwanPHone------ \n")
print(mobile.TaiwanPhone().special_freature(50))
