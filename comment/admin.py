from django.contrib import admin

from .models import Comment

# 注册ArticlePost模型到admin中
admin.site.register(Comment)