import os

nimage = os.listdir('testCifar/apple/')
count1 = 0
for j in nimage:
    count1+=1
print(count1)
image = os.listdir('Cifar/test/apple')
count2 = 0
for j in image:
    count2+=1
print(count2)
count=count1/count2
print('新数据集图像数是原数据集的{}倍。'.format(count))