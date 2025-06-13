from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from takeasnip import settings
from .forms import SnippetForm, CommentForm
from .models import Snippet, Comment


# Create your views here.

# Returns snippets list
def snippet_list(request):
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'snippet_list.html', {'snippets': snippets})

# Returns details of snippet
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    comments = Comment.objects.filter(snippet=pk).order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.snippet = snippet
            comment.author = request.user
            comment.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'snippet_detail.html', {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,})

@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm()

    return render(request, 'snippet_form.html', {'form': form})
