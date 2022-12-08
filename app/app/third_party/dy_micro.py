from bytedance import ByteDance

from app.core.config import settings

tt_app = ByteDance(
    # 核心配置
    app_id=settings.APP_ID,
    app_secret=settings.APP_SECRET,
    # 支付相关配置，可以不配置
    access_token_type='file', # 保存access_token的方法
    ac_path='./dy_access_token' # 如果指定access_token_type = file的时候，指定路径用，不指定就是根目录
    )