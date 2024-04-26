from PIL import Image

def filter_color(image_path, color_range, output_path):
    """
    将图片中落在指定颜色范围内的像素替换为透明
    :param image_path: 输入图片路径
    :param color_range: RGB颜色范围，例如(0, 0, 0) 到 (50, 50, 50)
    :param output_path: 输出图片路径
    """
    # 读取图片
    image = Image.open(image_path)

    # 将图片转换为RGBA模式，方便设置透明度
    image = image.convert("RGBA")

    # 获取图片的像素数据
    data = image.getdata()

    # 创建一个新的像素列表，将指定颜色范围内的像素替换为透明
    new_data = []
    for item in data:
        # 如果当前像素落在指定颜色范围内
        if color_range[0] <= item[:3] <= color_range[1]:
            # 设置透明度为0
            new_data.append((0, 0, 0, 0))
        else:
            # 其他颜色保持不变
            new_data.append(item)

    # 更新图片的像素数据
    image.putdata(new_data)

    # 保存处理后的图片
    image.save(output_path)

# 设置RGB颜色范围
color_range = ((0, 0, 0), (30, 30, 30))

# 调用函数并指定输入和输出路径
filter_color("24_filtered.jpg", color_range, "output_image24.png")
