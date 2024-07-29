from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, text, output_path):
    """
    在图像上添加文字水印并保存。

    参数：
    image_path (str): 输入图像的路径。
    text (str): 水印文字。
    output_path (str): 保存水印图像的路径。
    """
    # 打开输入图像
    image = Image.open(image_path).convert('RGB')
    
    # 创建水印图层
    watermark = Image.new('RGBA', image.size)
    draw = ImageDraw.Draw(watermark, 'RGBA')
    
    # 加载字体
    font = ImageFont.load_default()
    
    # 计算文本尺寸
    text_bbox = draw.textbbox((0, 0), text, font=font)
    textwidth = text_bbox[2] - text_bbox[0]
    textheight = text_bbox[3] - text_bbox[1]
    width, height = image.size
    x = width - textwidth - 10
    y = height - textheight - 10
    
    # 绘制水印
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    
    # 叠加水印
    watermarked = Image.alpha_composite(image.convert('RGBA'), watermark)
    
    # 保存结果
    watermarked.convert('RGB').save(output_path)
    return output_path