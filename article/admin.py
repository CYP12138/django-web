from django.contrib import admin


# 导入ArticlerPost
from .models import ArticlePost
from .models import ArticleColumn

# 注册ArticlePost模型到admin中
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)