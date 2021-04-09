from django.views import generic
#from django.views.generic.detail import DetailView
from blog.models import Blog

class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'


# Create your views here.
