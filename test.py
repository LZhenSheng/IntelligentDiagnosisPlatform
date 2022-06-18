import cv2
# imgName ='I:/DeepLearning/Database/淋巴亚型分类/lymphoma.tar/lymphoma/MCL/sj-04-3077-R2_001.tif'
imgName1='D:/home/QQ20201031085645.jpg'
img = cv2.imread(imgName1)  # 读取图像
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
x = img.shape[1]  # 获取图像大小
y = img.shape[0]
print(x)