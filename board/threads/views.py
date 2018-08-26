from django.shortcuts import render, redirect
from .models import Thread,OnePost
from .forms import text_of_post
from django.utils import timezone
from django.http import Http404
# Create your views here.


def index(request):
    #return render(request, 'threads/index.html', content_type='application/xhtml+xml')
    thread_list = Thread.objects.all()
    dic = dict()
    posts_list = []
    for thread in Thread.objects.all():
        posts_list += OnePost.objects.filter(thread_id = thread.id)
        dic.update({thread: OnePost.objects.filter(published_date = thread.published_date)})
    context = {'thread_list_all': thread_list, 'dic' : dic }
    return render(request, 'threads/index.html',context)


def creation_thread(request):
    return render(request, 'threads/creation_thread.html')


def creation(request):
    context = {'text_of_thread': request}
    t = Thread()
    t.published_date = timezone.now()
    t.number_of_OnePost = 0
    t.id = len(Thread.objects.all())+1
    p = OnePost()
    p.id = len(OnePost.objects.all())+1
    p.published_date = timezone.now()
    t.save()
    p.thread = t
    p.text = request.GET['text_of_thread']
    p.number_of_replies = 0
    p.save()
    return redirect('thread/' + str(t.id))

def thread_num(request, thread_id):
    context = {'t_id': thread_id}
    try:
        context.update({'posts': OnePost.objects.filter(thread_id = thread_id),'t': Thread.objects.get(id= thread_id) })
    except Thread.DoesNotExist:
        raise Http404('Thread does not exist')
    return render(request, 'threads/thread_num.html', context)
