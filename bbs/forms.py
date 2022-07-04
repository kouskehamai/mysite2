from django import forms
from bbs.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', )

        # ↓これを追加
        labels = {
            'content': '投稿内容',
        }

        # ↓これを追加
        help_texts = {
            'content': None,
        }