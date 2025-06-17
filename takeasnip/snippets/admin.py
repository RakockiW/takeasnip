from django.contrib import admin

from .models import Snippet, VoteSnippet, Comment, VoteComment


# Register your models here.

class VoteSnippetInline(admin.TabularInline):
    model = VoteSnippet
    extra = 0
    readonly_fields = ('value', 'user')
    fields = ('value', 'user')
    can_delete = False

class VoteCommentInline(admin.TabularInline):
    model = VoteComment
    extra = 0
    readonly_fields = ('value', 'user')
    fields = ('value', 'user')
    can_delete = False

class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('created_at', 'author')
    fields = ('created_at', 'author', 'content')
    extra = 0
    inlines = (VoteCommentInline, )

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'technology', 'created_at')
    readonly_fields = ('created_at', 'author')
    inlines = (CommentInline, VoteSnippetInline, )

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(VoteSnippet)