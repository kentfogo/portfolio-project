from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Create a blogs model
#title
#pub_date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

class Meta:
    ordering = ['created_on']

def __str__(self):
    return self.title




#Add the blog app to settings
#Create a migration
#Migrate
#Add to admin
