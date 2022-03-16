from django.db import models

class Topic(models.Model):#主题
    text = models.CharField(max_length=200)#让数据库留下200字符
    date_added = models.DateTimeField(auto_now_add=True)#自动设置当前时间

    def __str__(self):
        return self.text

class Entry(models.Model):#知识条目
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#关联到主题
    text = models.TextField()#无限制字段
    date_added = models.DateTimeField(auto_now_add=True)#时间戳

    class Meta:
        verbose_name_plural = "entries"#用entries表示多个条目

    def __str__(self):
        return f"{self.text[:50]}..."#呈现前50个字符