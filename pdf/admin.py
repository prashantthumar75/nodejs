from django.contrib import admin
from .models import RegisterModel

# Register your models here.

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

from django.contrib import admin
from .models import Post, PostImage

# admin.site.register(Post)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    pass
    # class Meta:
    #     model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

