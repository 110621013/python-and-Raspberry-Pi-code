不必宣告變數
\n是換行 r放在字串前則省略意義符號 但print(r"10\n20")則顯示10\n20
字串可以以陣列想法存取字元{word="123456789"  word[2]=3}
若a,b都="?"則a is b=True,id(a)=id(b)
aa.append(aa)陣列可遞迴,append添加陣列項目
若bb=aa則aa is bb=True
print(chr(98)*100)=100個chr(98)
while 判斷式:
try :
    num=input("enter:")
except ValueError:
    continue 掠過一次迴圈
    break 直接跳出迴圈
次方**
a, b, c = (int(x) for x in input().split(' '))  輸入的字串遇到空白建就分開成為x陣列
print(list(字串)) 用list方式印出字串
字串.lstrip("*")去除字串前面之*
陣列.index(值)
