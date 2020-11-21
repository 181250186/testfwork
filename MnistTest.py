import os

nimage = os.listdir('testMnist/new9/')
count1 = 0
for j in nimage:
    count1+=1
print(count1)
image = os.listdir('testMnist/9/')
count2 = 0
for j in image:
    count2+=1
print(count2)
count=count1/count2
print('新数据集图像数是原数据集的{}倍。'.format(count))