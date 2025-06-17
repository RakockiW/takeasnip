from django.contrib.auth.decorators import login_required
from django.db.models import Q, query
from django.shortcuts import render, get_object_or_404, redirect

from takeasnip import settings
from .forms import SnippetForm, CommentForm
from .models import Snippet, Comment, VoteSnippet, VoteComment


# Create your views here.

# Returns snippets list
def snippet_list(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    technology_filter = request.GET.get('technology')

    snippets = Snippet.objects.all()

    if category_filter:
        snippets = snippets.filter(category__iexact=category_filter)

    if technology_filter:
        snippets = snippets.filter(technology__iexact=technology_filter)

    if query:
        snippets = snippets.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query) |
            Q(technology__icontains=query) |
            Q(category__icontains=query)
        )


    categories = Snippet.objects.values_list(
        'category', flat=True).distinct()

    technologies = Snippet.objects.values_list(
        'technology', flat=True).distinct()

    snippets = snippets.order_by('-created_at')

    return render(request, 'snippet_list.html', {
        'snippets': snippets,
        'categories': categories,
        'selected_category': category_filter,
        'technologies': technologies,
        'selected_technology': technology_filter,
    })

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
        'comment_form': comment_form,
    })

@login_required
def vote_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    existing_vote = VoteSnippet.objects.filter(user=request.user, snippet=snippet)

    if not existing_vote and request.method == 'POST':
        value = request.POST.get('vote')
        if value in ['1', '-1']:
            VoteSnippet.objects.create(
                user=request.user,
                snippet=snippet,
                value=value
            )
    return redirect('snippet_detail', pk=snippet.pk)


@login_required
def snippet_create(request):

    form = SnippetForm(request.POST or None)

    if form.is_valid():
        snippet = form.save(commit=False)
        snippet.author = request.user
        snippet.save()
        return redirect('snippet_detail', pk=snippet.pk)

    return render(request, 'snippet_form.html', {'form': form})

def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    user = request.user

    if request.method == 'POST' and snippet.author == user:
        snippet.delete()

    return redirect('snippet_list')

def snippet_edit(request, pk):

    snippet = get_object_or_404(Snippet, pk=pk)

    form = SnippetForm(request.POST or None, instance=snippet)

    if form.is_valid():
        snippet = form.save(commit=False)
        snippet.author = request.user
        snippet.save()
        return redirect('snippet_detail', pk=snippet.pk)

    return render(request, 'snippet_form.html', {'form': form})

@login_required
def vote_comment(request, pk):
    if request.method != 'POST':
        return redirect('snippet_detail', pk=get_object_or_404(Comment, pk=pk).snippet.pk)

    comment = get_object_or_404(Comment, pk=pk)
    snippet = comment.snippet

    existing_vote = VoteComment.objects.filter(user=request.user, comment=comment).first()

    if not existing_vote:
        value = request.POST.get('vote')
        if value in ['1', '-1']:
            VoteComment.objects.create(
                user=request.user,
                comment=comment,
                value=int(value)
            )
    return redirect('snippet_detail', pk=snippet.pk)


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST' and request.user == comment.author:
        comment.delete()

    return redirect('snippet_detail', pk=comment.snippet.pk)

