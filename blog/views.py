from django.shortcuts import render, get_object_or_404
from . models import Blog

def allblogs(request):
    blogs =Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':detailblog})



#class BlogList(generic.ListView):
    #queryset = Blog.objects.filter(status=1).order_by('-created_on')
    #template_name = 'index.html'

#class BlogDetail(generic.DetailView):
    #model = Blog
    #template_name = 'blog_detail.html'


# Create your views here.
