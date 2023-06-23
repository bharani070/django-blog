#from django.http import HttpResponse
from blogs.models import Blog, Category, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts' : posts,
        'category' : category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, post_slug):
    single_blog = get_object_or_404(Blog, slug=post_slug, status="Published")
    if request.method =='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count
    } 
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_discription__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context = {
        'blogs' : blogs,
        'keyword' : keyword,
    }
    return render(request, 'search.html', context)
