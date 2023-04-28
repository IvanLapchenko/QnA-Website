from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .forms import AddPostForm


def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post_list.html', {'posts': posts})


@csrf_exempt
def post_add(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.data)
    form = AddPostForm()
    return render(request, 'post_add.html', {'form': form})
