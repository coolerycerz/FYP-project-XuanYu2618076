import cv2
import os

# 指定图像文件夹路径
image_folder_path = 'D:/senior4/UESTC4006P Individual Project/EXPERIMENT/SIFT/CAR'
output_folder_path = 'D:/senior4/UESTC4006P Individual Project/EXPERIMENT/SIFT/PROCESSED'
# 获取文件夹中的所有图像文件
image_files = [os.path.join(image_folder_path, file) for file in os.listdir(image_folder_path) if
               file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 创建SIFT特征提取器
sift = cv2.xfeatures2d.SIFT_create()

for idx, image_file in enumerate(image_files, start=1):
    # 读取图像
    img = cv2.imread(image_file)

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测图像的特征点
    keypoints, descriptors = sift.detectAndCompute(img, None)

    # 在图像上绘制检测到的关键点
    sift_image = cv2.drawKeypoints(gray, keypoints, img)

    # 显示图像


    # 保存图像，添加序号到文件名
    output_filename = f"table_sift_{idx}_{os.path.basename(image_file).split('.')[0]}.jpg"
    output_filepath = os.path.join(output_folder_path, output_filename)
    cv2.imwrite(output_filepath, sift_image)


# 关闭所有窗口
cv2.destroyAllWindows()
