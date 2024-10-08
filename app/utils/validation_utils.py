from flask import jsonify
from marshmallow import ValidationError

def handle_validation_error(errors):
  # 处理验证错误
  response = {"errors": errors}
  return jsonify(response), 400  # 返回错误响应和400状态码