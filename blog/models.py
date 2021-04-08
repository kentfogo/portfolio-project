from django.db import models
from django.db.models import permalink

# Create a blogs model
#title
#pub_date
#body
#image
class blog(models.Model)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def__unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self)
        return('view_blog_post', None, { 'slug': self.slug})

class Category(models.Model)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def_unicode_(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category',None,{'slug': self.slug})





#Add the blog app to settings
#Create a migration
#Migrate
#Add to admin
