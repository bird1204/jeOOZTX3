# 自評作業狀況 ( **耗時： 3.5 HR** )

### [ 2 HR ] 挑戰一: OO觀念運用 (folder: x_1)

主要耗時在計算 Fibonacci 時，首先使用單純遞迴解決，後由於測試結果不好；時間複雜度為 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <msup>
    <mn>2</mn>
    <mi>n</mi>
  </msup>
  <mo stretchy="false">)</mo>
</math> ，遂嘗試降至 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math> ，深入瞭解後另有 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mi>l</mi>
  <mi>o</mi>
  <mi>g</mi>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math> 之解法，惟本專案為測試用，因此選擇不使用此法

### [ 0.5 HR ] 挑戰二: pip 及 Django 實作  (folder: x_2)

開發機使用 **conda** 管理環境，因此 requirements.txt 還算乾淨

```bash
# pip 匯出 
pip freeze > requirements.txt

# conda 匯出requirements.txt
activate <environment-name>
conda list -e > requirements.txt

# conda 匯出 environment
activate <environment-name>
conda env export > <environment-name>.yml
```

### [ 1 HR ] 挑戰三: 檔案與資料操作 (folder: x_3)

花了一點時間在搜尋台灣電話號碼的格式，經查市話格式各有不同，因此設定規則為：

````
手機 : 09 開頭，固定 10 碼
市話 : 區碼開頭，固定 10 碼
````

# 工作 / 程式上的期待

首先附上個人 [resume](https://www.cakeresume.com/wei-yi-chiu-python) ，目前正在尋找擁有下列特質的機會：

1. 從軟體獲利的團隊
2. 具備軟體思維的團隊
3. 有募資 或 目標成為上市公司的團隊
4. 在近未來計劃使用 ML/DL 解決更大的問題
5. 跨文化的團隊 ( Nice-to-have ) 

個人希望持續利用軟體的優勢，分析更大量級的問題，並提出具備影響力的解法。
對於程式的看法則偏向工欲善其事，必先利其器，比起新技術，更**傾向採用最適合產品的成熟技術，且持續找尋最適合的方式**。