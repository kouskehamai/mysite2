from django.shortcuts import render, redirect
from django.http import HttpResponse
from bbs.models import Post
from bbs.forms import PostForm  # <- これを追加


def home_view(request):
    # request.methodによって処理を分岐
    if request.method == 'GET':
        return home_view_get(request)
    elif request.method == 'POST':
        return home_view_post(request)
    else:
        return HttpResponse('invalid method', status=400)


def home_view_get(request, form=None):
    """
    パス bbs/ の GET
    """
    context = {}  # コンテキストを作成

    context['title'] = '一行掲示板'  # ページのタイトル
    context['posts'] = Post.objects.order_by('-id').all()  # Postのリストを取得

    if form:
        context['form'] = form
    else:
        context['form'] = PostForm()  # フォームを保存

    # renderにコンテキストを渡しテンプレートを描画
    return render(request, 'bbs/home.html', context)


def home_view_post(request):
    """
    パス bbs/ の POST
    """
    form = PostForm(request.POST)
    if not form.is_valid():
        return home_view_get(request, form=form)

    form.save()
    return redirect('bbs_home')
