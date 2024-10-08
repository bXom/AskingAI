import os
import uuid
from PyPDF2 import PdfReader, PdfWriter
from config import Config

# TODO: 拆分pdf文件
def sub_pdf(pdf_path, max_size):
  print('max_size: ', max_size)
  # 获取项目根目录
  project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 构建完整的文件路径
  full_pdf_path = os.path.join(project_root, Config.STATIC_FOLDER, pdf_path)

  if not os.path.exists(full_pdf_path):
    raise FileNotFoundError(f"文件 {full_pdf_path} 不存在")

  pdf_reader = PdfReader(full_pdf_path)
  file_path_list = []
  current_writer = PdfWriter()
  current_size = 0
  base_name = os.path.splitext(full_pdf_path)[0]
  file_index = 1
  current_path = f"{base_name}_{uuid.uuid4().hex}_{file_index}.pdf"

  for page in pdf_reader.pages:
    current_writer.add_page(page)
    # 临时保存当前PDF以估算大小
    with open(current_path, 'wb') as f:
      current_writer.write(f)
    current_size = os.path.getsize(current_path)

    # 如果当前文件大小超过最大允许大小，则保存当前页面之前的所有页面，并开始新文件
    if current_size > max_size:
      # 移除最后添加的页面以保持文件大小在限制之下
      current_writer = PdfWriter()  # 创建新的 PdfWriter 对象
      for i in range(len(current_writer.pages) - 1):
          current_writer.add_page(pdf_reader.pages[i])
      with open(current_path, 'wb') as f:
          current_writer.write(f)
      file_path_list.append(current_path)
      current_writer = PdfWriter()
      current_writer.add_page(page)  # 将超出大小的页面加入新的PDF文件
      file_index += 1
      current_path = f"{base_name}_{uuid.uuid4().hex}_{file_index}.pdf"
  
  # 保存最后一个PDF文件，如果有内容的话
  if current_writer.pages:
    with open(current_path, 'wb') as f:
      current_writer.write(f)
    file_path_list.append(current_path)

  return file_path_list