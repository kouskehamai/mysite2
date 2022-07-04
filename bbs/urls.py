from django.urls import path
from bbs.views import home_view  # bbs\views.pyからhome_view関数をインポート

urlpatterns = [
    path('', home_view, name='bbs_home'),  # ルートにhome_viewを指定
]