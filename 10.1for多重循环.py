# 100以内被7整除的数
arr1=[]
for i in range(1, 100):
  if(i%7==0):
    arr1.append(i)
print(arr1)
# 输入一个数 判断能否被7整除
num=int(input('请输入一个数：'))
if(num%7==0):
  print('可以被7整除')
else:
  print('不可以被7整除')
  
  
# 多重循环 二维数组
arr3=[[1,2,3],[4,5,6],[7,8,9]]
for  i in arr3:
  for j in i:
    print(j,end=' ')