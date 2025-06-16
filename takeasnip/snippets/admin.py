from django.contrib import admin

from .models import Snippet, Vote, Comment

# Register your models here.

class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0
    readonly_fields = ('value', 'user')
    fields = ('value', 'user')
    can_delete = False

class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('created_at', 'author')
    fields = ('created_at', 'author', 'content')
    extra = 0

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'technology', 'created_at')
    readonly_fields = ('created_at', 'author')
    inlines = (CommentInline, VoteInline, )

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Vote)