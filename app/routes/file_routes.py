from flask import Blueprint, jsonify, request
from ..schemas.file_schemas import CompressFileSchema, SubPDFSchema
from ..utils import handle_validation_error
from ..services import compress_file, sub_pdf

file_route = Blueprint('file', __name__)

def get_file_type(file_path):
  return file_path.split('.')[-1]

# 文件压缩
@file_route.route('/compress', methods=['POST'])
def compress_file_route():
  schema = CompressFileSchema()
  data = request.json
  # 验证输入数据
  errors = schema.validate(data)
  if errors:
    return handle_validation_error(errors)
  
  file_path = data['file_path']
  file_type = get_file_type(file_path)
  compressed_file = compress_file(file_path, file_type)
  return jsonify({'message': '文件压缩成功', 'compressed_file': compressed_file})

# 拆分 pdf
@file_route.route('/pdf/sub', methods=['POST'])
def sub_pdf_route():
  schema = SubPDFSchema()
  data = request.json
  # 验证输入数据
  errors = schema.validate(data)
  if errors:
    # 只传递错误信息
    return handle_validation_error(errors)

  file_path_list = sub_pdf(data['pdf_path'], data['max_size'])
  return jsonify({'message': '文件拆分成功', 'file_path_list': file_path_list})