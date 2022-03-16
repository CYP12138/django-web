from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import Topicform, Entryform
def index(request):#主页
    return render(request, "blogs/index.html")#模板渲染

def topics(request):
    topics = Topic.objects.order_by("date_added")#请求数据库数据按时间排序
    context = {"topics": topics}#上下文
    return render(request, "blogs/topics.html", context)

def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "blogs/topic.html", context)

def new_topic(request):
    if request.method != "POST":
        form = Topicform()
    else:
        form = Topicform(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect("blogs:topics")

    context = {"form": form}
    return render(request, "blogs/new_topic.html", context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = Entryform()
    else:
        form = Entryform(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("blogs:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "blogs/new_entry.html", context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != "POST":
        form = Entryform(instance=entry)
    else:
        form = Entryform(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:topic", topic_id=topic.id)

    context = {"topic": topic, "form": form, "entry": entry}
    return render(request, "blogs/edit_entry.html", context)