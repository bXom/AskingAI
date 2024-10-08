import os
from app import create_app
from config import DevelopmentConfig, ProductionConfig, Config

# 根据环境变量选择配置
if os.environ.get('FLASK_SERVER') == 'deploy':
  config = ProductionConfig
elif os.environ.get('FLASK_SERVER') == 'dev':
  config = DevelopmentConfig
else:
  config = Config

app = create_app(config)

if __name__ == '__main__': app.run(host='0.0.0.0', port=app.config['PORT'])
