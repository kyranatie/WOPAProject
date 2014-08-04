from blog.models import Blog,Category
from django.shortcuts import render_to_response, get_object_or_404
from .forms import PostForm
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def post_new(request):
   # global form
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
           post = form.save(commit=False)
           post.title = request.user
           post.save()

            #form.save
        else:
           # redirect(new_post)    

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render_to_response('post_edit.html', {'form': form})