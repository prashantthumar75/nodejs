from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

class RegisterModel(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    # num = models.IntegerField(('Phone number'))
    profileImage = models.ImageField(upload_to='pic',blank=True)
    is_block = models.BooleanField(default=False)

    # def get_absolute_url( self):
    #     return reverse('list')


from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


# from Comments.models import  *


# Create your models here.
class Post(models.Model):
    SOURCE_OPTIONS = [
        ('SCOIAL-FEED', 'SCOIAL-FEED'),
        ('COLLEGE-FEED', 'COLLEGE-FEED'),
    ]
    source = models.CharField(choices=SOURCE_OPTIONS, max_length=255, default='SCOIAL-FEED')
    title = models.CharField(max_length=255, null=True, default=None)
    content = models.TextField()
    # image = models.ImageField(upload_to='static/posts/images', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)

    # image = models.ImageField(upload_to='static/posts/images', null=True, default=None)
    # image_medium = ImageSpecField(source='image',
    #                               processors=[Thumbnail(200, 100)],
    #                               options={'quality': 60})
    # image_small = ImageSpecField(source='image',
    #                              processors=[Thumbnail(100, 50)],
    #                              options={'quality': 60})

    # liked = models.ManyToManyField(User,blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[:20])

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)  # newest on the top


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/posts/images', null=True, default=None)

    def __str__(self):
        return self.post.content[:10]

