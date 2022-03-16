from django import forms
from .models import Topic, Entry

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]#只包含text
        labels = {"text": ""}#不生成标签

class Entryform(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}#宽度设为80列