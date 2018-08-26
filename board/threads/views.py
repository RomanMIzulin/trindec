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
    for thread in thread_list:
        dic.update({thread.id:OnePost.objects.filter(thread_id=thread.id)})
    context = {'thread_list_all': thread_list, 'dic' : dic  }
    return render(request, 'threads/index.html',context)


def creation_thread(request):
    return render(request, 'threads/creation_thread.html')


def creation(request):
    context = {'text_of_thread': request}
    t = Thread()
    t.published_date = timezone.now()
    p = OnePost()
    p.published_date = timezone.now()
    p.thread = t
    p.text = text_of_post(request)
    p.id = 3
    t.save()
    p.save()
    return redirect('thread/' + str(t.id))

def thread_num(request, thread_id):
    context = {'t_id': thread_id}
    try:
        context.update({'posts': OnePost.objects.filter(thread_id = thread_id),'t': Thread.objects.get(id= thread_id) })
    except Thread.DoesNotExist:
        raise Http404('Thread does not exist')
    return render(request, 'threads/thread_num.html', context)
