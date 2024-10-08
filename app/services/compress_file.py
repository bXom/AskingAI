import os
import uuid
from config import Config

def compress_file(file_path, file_type):
  file_type = file_type.lower()
  # 获取项目根目录
  project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 构建完整的文件路径
  file_path = os.path.join(project_root, Config.STATIC_FOLDER, file_path)
  if file_type == 'pdf':
    from PyPDF2 import PdfReader, PdfWriter
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"文件 {file_path} 不存在")
    pdf_reader = PdfReader(file_path)
    pdf_writer = PdfWriter()
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      pdf_writer.add_page(page)
    compressed_path = file_path.replace('.pdf', f'_{uuid.uuid4().hex}' + '.pdf')
    with open(compressed_path, 'wb') as f:
      pdf_writer.write(f)
    return compressed_path
  else:
    from PIL import Image
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"文件 {file_path} 不存在")
    image = Image.open(file_path)
    compressed_path = file_path.replace('.' + file_type, f'_{uuid.uuid4().hex}.' + file_type)
    if file_type in ['jpg', 'jpeg']:
      image.save(compressed_path, quality=20, optimize=True)
    elif file_type == 'png':
      image.save(compressed_path, optimize=True, compress_level=9)
    elif file_type == 'gif':
      image.save(compressed_path, optimize=True)
    else:
      image.save(compressed_path, optimize=True)
    return compressed_path
