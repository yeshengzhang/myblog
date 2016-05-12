# coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from datetime import *
import hashlib

from django.template import RequestContext

from app.models import User, Article, Visitor, Liuyan

# md5加密
md5jm = hashlib.md5()


# Create your views here.
def base(request):
    return render_to_response('base.html')


def index(request):
    try:
        limit = 2
        paginator = Paginator(Article.objects.order_by(Coalesce('create_time', 'title').desc()), limit)
        page_num = request.GET.get('page')
        try:
            page_info = paginator.page(page_num)
        except PageNotAnInteger:
            page_info = paginator.page(1)
        except EmptyPage:
            page_info = paginator.page(paginator.num_pages)
        # article_list = page_info.object_list
        return render_to_response('index.html', {'article_list': page_info}, context_instance=RequestContext(request))
    except BaseException, e:
        print e
        return HttpResponse(e)


def read(request):
    article_list = Article.objects.get(id=2)
    return render_to_response("read.html", {'article_list': article_list}, context_instance=RequestContext(request))


def write(request):
    if request.session.get('username') != 'admin':
        info = "你不是小张！不过可以<a href='../about/'>查看小张</a>"
        return HttpResponse(info)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        author = request.POST['author']

        article = Article()
        article.title = title
        article.body = body
        article.author = author
        article.create_time = datetime.now()
        article.save()
        return render(request, 'index.html', context_instance=RequestContext(request))
    return render(request, 'write.html', context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        print uname, '=====', pword
        if len(User.objects.filter(username=uname, password=pword)) == 1:
            request.session['username'] = uname
            info = "登陆成功！"
        else:
            info = "您输入的用户名或密码有误！"
        return render_to_response('login.html', {'info': info}, context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))


def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        pword = request.POST['password']
        # md5jm.update(request.POST['password'])
        # pword = md5jm.hexdigest()
        sex = request.POST['sex']
        reg_time = datetime.now()

        reg_user = User()
        try:
            if len(User.objects.filter(username=uname)) == 0:
                reg_user.username = uname
                reg_user.password = pword
                reg_user.sex = sex
                reg_user.reg_time = reg_time
                reg_user.save()
                return HttpResponse('success')
            else:
                return HttpResponse('username repeat')
        except BaseException, e:
            return HttpResponse(e)
    return render_to_response('register.html', context_instance=RequestContext(request))


def logout(request):
    del request.session['username']
    return render_to_response('index.html', context_instance=RequestContext(request))


def liuyan(request):
    if request.method == "POST":
        info = request.POST['body']
        return HttpResponse(info)
    return HttpResponse("<a href='../index'>留言成功</a>")


def about(request):
    return render_to_response('about.html')


def add_zan(request):
    if request.method == "POST":
        article_id = request.POST['ariticle_id']
        add = int(request.POST['add_zan'])
        add += 1
        # info = "article_id:", article_id, "add_zan:", add

        article = Article.objects.get(id=article_id)
        article.add_zan = add
        article.save()
        return render_to_response('index.html', context_instance=RequestContext(request))
    info = "<script>alert('感谢您点赞')</script>"
    return HttpResponse(info)
