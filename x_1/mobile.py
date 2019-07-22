# -*- coding: UTF-8 -*-
import math
class MobilePhone:
    def __init__(self, price=0, camera_count=0, screen_size=0):
        self.price=price
        self.camera_count=camera_count
        self.screen_size=screen_size
    def special_freature(self):
        return

class GooglePhone(MobilePhone):
    def __init__(self, price=10, camera_count=3, screen_size=5):
        super().__init__()
    def special_freature(self, list=[]):
        # special_freature 輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
        results = []
        for int in sorted(list, reverse=True):
            if (int % 2 == 0 and int > 10):
                results.append(int)
        return results

class TaiwanPhone(MobilePhone):
    def __init__(self, price=20, camera_count=1, screen_size=3):
        super().__init__()
    def special_freature(self, n=1):
        # 輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
        fib = self.fibonacci(n)
        npr = self.npr(int(str(fib)[-2]), int(str(fib)[-1]))
        return {'fibonacci' : fib , 'npr' : npr}

    def npr(self, n, r):
        if n == r:
            return float('inf')
        elif n > r:
            return math.factorial(n) / math.factorial(n-r)
        else:
            return math.factorial(r) / math.factorial(r-n)

    def fibonacci(self, n):
        fibs = [0, 1]
        for i in range(2, n+1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[n]