from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from takeasnip import settings
from .forms import SnippetForm, CommentForm
from .models import Snippet, Comment, Vote


# Create your views here.

# Returns snippets list
def snippet_list(request):
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'snippet_list.html', {'snippets': snippets})

# Returns details of snippet
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    comments = Comment.objects.filter(snippet=pk).order_by('-created_at')
    upvotes = snippet.get_votes(1)
    downvotes = snippet.get_votes(-1)

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
        'comment_form': comment_form,
        'upvotes': upvotes,
        'downvotes': downvotes,}
        )

@login_required
def vote_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    existing_vote = Vote.objects.filter(user=request.user, snippet=snippet)

    if not existing_vote and request.method == 'POST':
        value = request.POST.get('vote')
        if value in ['1', '-1']:
            Vote.objects.create(
                user=request.user,
                snippet=snippet,
                value=value
            )
    return redirect('snippet_detail', pk=snippet.pk)


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

def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    user = request.user

    if request.method == 'POST' and snippet.author == user:
        snippet.delete()

    return redirect('snippet_list')

def snippet_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet)

    return render(request, 'snippet_form.html', {'form': form})
