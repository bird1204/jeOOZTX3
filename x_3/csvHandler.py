# -*- coding: UTF-8 -*-
import pathlib, csv, random, string, numpy

class CsvHanlder:
    def __init__(self):
        pathlib.Path('ilovecoffee').mkdir(parents=False, exist_ok=True) 
        self.names = ['tom', 'peter', 'hank', 'ben', 'bert', 'jacy', 'john', 'sam', 'james', 'bill']
        self.phone_prefix = ['02', '03', '037', '04', '049', '05', '06', '07', '082', '0832', '089']
        self.data_set = []

    def create_csv(self):
        with open('ilovecoffee/customers.csv', 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['customer_id', 'customer_name', 'customer_mobile', 'frequency'])
            for data in self.__set_data_set():
                writer.writerow(data)
        return

    def calculate_csv(self):
        frequencies = []
        # 當被呼叫時，會讀取 /ilovecoffee/customers.csv，並列印出frequency 的中數、眾數及平均數 (取至小數點後 5 位)
        with open('ilovecoffee/customers.csv', newline='') as csvfile:
            rows = csv.reader(csvfile)
            next(rows, None) # 跳過 header
            for row in rows:
                frequencies.append(int(row[3]))

        frequencies = sorted(frequencies)
        counts = numpy.bincount(frequencies)
        return {
                'median': numpy.median(frequencies), 
                'mean': numpy.mean(frequencies), 
                'counts': numpy.argmax(counts)
            }

    def __set_data_set(self):
        for i in range(500):
            self.data_set.append(
                [
                    self.__generate_id(), 
                    self.__generate_name(), 
                    self.__generate_mobile(), 
                    self.__generate_frequency()
                ]
            )
        return self.data_set

    def __generate_id(self):
        # 長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字
        ids = [random.choice(string.ascii_letters)]
        for x in range(7):
            ids.append(random.choice(string.ascii_letters + string.digits))
        self.id_prefix = ''.join(ids)
        return self.id_prefix

    def __generate_name(self):
        # 隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....] 將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"
        return random.choice(self.names) + '.' + self.id_prefix

    def __generate_mobile(self):
        # 隨機產生一個+886開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生
        # 規則 -> 
        #        手機 09 開頭，固定 10 碼
        #        市話 區碼開頭，固定 10 碼
        while True:
            num_str = "+886"
            if random.randint(0,1) == 0:
                num_str += "9"
                num_str += "".join(random.choice(string.digits) for x in range(8))
            else:
                num_str += random.choice(self.phone_prefix)[1:]
                num_str += "".join(random.choice(string.digits) for x in range(14 - len(num_str)))

            if num_str not in map(lambda data: data[2], self.data_set):     
                return num_str 

    def __generate_frequency(self):
        #從 [0-20] 中隨機進行選擇
        return random.randint(0,20)