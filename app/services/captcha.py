import random
import io
import os
import threading
from PIL import Image, ImageDraw, ImageFont
from config import Config

# 生成验证码图像
def generate_captcha_image():
  captcha_code, image_bytes = generate_captcha()
  # 获取项目根目录
  project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 构建完整的文件路径
  file_path = os.path.join(project_root, Config.CACHE_IMG_PATH, f'captcha-{captcha_code}.png')
  with open(file_path, 'wb') as f:
    f.write(image_bytes)
  # 设置10分钟后自动删除文件
  timer = threading.Timer(600, lambda: os.remove(file_path))
  timer.start()
  return captcha_code

# 生成验证码
def generate_captcha():
  # 获取项目根目录
  project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 生成4位随机数字
  captcha_text = ''.join(random.choices('0123456789', k=4))
  # 创建图像
  width, height = 120, 50
  image = Image.new('RGB', (width, height), color='white')
  draw = ImageDraw.Draw(image)
  try:
    # 尝试加载字体（请确保字体文件存在）
    font_path = os.path.join(project_root, Config.FONTS_PATH, 'hussar.otf')
    font = ImageFont.truetype(font_path, 36)
  except IOError:
    # 如果字体加载失败，使用默认字体
    font = ImageFont.load_default()
  # 绘制文本
  text_width, text_height = draw.textsize(captcha_text, font)
  x = (width - text_width) / 2
  y = (height - text_height) / 2
  draw.text((x, y), captcha_text, font=font, fill='black')
  # 添加一些噪点
  for _ in range(1000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    draw.point((x, y), fill='gray')
  # 添加一些线条
  for _ in range(5):
    start = (random.randint(0, width - 1), random.randint(0, height - 1))
    end = (random.randint(0, width - 1), random.randint(0, height - 1))
    draw.line([start, end], fill='gray')
  # 将图像转换为字节流
  img_byte_array = io.BytesIO()
  image.save(img_byte_array, format='PNG')
  img_byte_array = img_byte_array.getvalue()
  return captcha_text, img_byte_array
