# 默认端口
class Config:
  DEBUG = False
  PORT = 5000
  STATIC_FOLDER = 'static'
  CACHE_PATH = 'cache'
  FONTS_PATH = STATIC_FOLDER+'/fonts'
  IMG_PATH = STATIC_FOLDER+'/img'
  CACHE_IMG_PATH = CACHE_PATH+'/img'

# 开发环境使用8080端口
class DevelopmentConfig(Config):
  DEBUG = True
  PORT = 8081
  STATIC_FOLDER = 'dev_static'
  CACHE_PATH = 'cache'
  FONTS_PATH = STATIC_FOLDER+'/fonts'
  IMG_PATH = STATIC_FOLDER+'/img'
  CACHE_IMG_PATH = CACHE_PATH+'/img'

# 生产环境使用80端口
class ProductionConfig(Config):
  PORT = 80
  STATIC_FOLDER = 'prod_static'
  CACHE_PATH = 'cache'
  FONTS_PATH = STATIC_FOLDER+'/fonts'
  IMG_PATH = STATIC_FOLDER+'/img'
  CACHE_IMG_PATH = CACHE_PATH+'/img'

# 可以根据需要添加更多配置类