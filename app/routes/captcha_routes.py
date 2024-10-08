from flask import Blueprint
from ..services.captcha import generate_captcha_image

captcha_route = Blueprint('captcha', __name__)

# 生成验证码图片
@captcha_route.route('', methods=['GET'])
def create_code():
  return generate_captcha_image()