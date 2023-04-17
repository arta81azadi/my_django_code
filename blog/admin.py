from django.contrib import admin
from .models import Post


@admin.register(Post)
class Blog(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'deta_created', ]
    ordering = ('-deta_created', )

