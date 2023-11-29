# 1*1 =1
# 1*2 =2  2*2=4
# 1*3=3   2*3=6 3*3=9   ....
#  j是指每列的第一个 i是指
for i in range(1, 10):
    for j in range(1, i+1):
        # print(j)
        print(j, end="*"+str(i)+"="+str(i*j)+" ")
    print("\n")