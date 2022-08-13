from django.shortcuts import render, redirect
from blog.models import Posts, Comments
from blog.forms import PostsForm, CommentsForm
from blog.mixin import error_filter
from django.contrib import messages
# Create your views here.


def post_create_detail(request):
    posts = Posts.objects.all().order_by('-date_posted')
    pform = PostsForm()
    cform = CommentsForm()
    error = None
    if request.method == 'POST':
        postform = PostsForm(request.POST)
        if postform.is_valid():
            postform.save()
        else:
            error = error_filter(postform.errors)
    return render(request, 'home.html', {'pform': pform, 'cform': cform, 'posts': posts, 'error': error})


def view_comments(request, pk):
    post = Posts.objects.get(id=pk)
    cform = CommentsForm()
    try:
        comments = post.comments.all().order_by('-created_on')
    except Comments.DoesNotExist:
        comments = None
    return render(request, 'comments.html', {'post': post, 'comments': comments, 'cform': cform})


def create_comment(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        cmntform = CommentsForm(request.POST)
        if cmntform.is_valid():
            cmnt = cmntform.save(commit=False)
            cmnt.post = post
            cmnt.save()
            return redirect(f'/viewcomments{pk}')   # redirecting urlpattern require 1 positional argument which is post pk(id)
        else:
            cmnt_error = cmntform.errors
            messages.add_message(request, messages.ERROR, cmnt_error)
            return redirect('/')
    cform = CommentsForm()
    return render(request, 'comments_form.html', {'cform': cform})


def comment_update(request, pk):
    cmnt = Comments.objects.get(id=pk)
    if request.method == 'POST':
        post_id = cmnt.post.id          # here we need to get post id for redirecting to right comments page
        cmntform = CommentsForm(request.POST, instance=cmnt)
        if cmntform.is_valid():
            cmntform.save()
            return redirect(f'/viewcomments{post_id}')
        else:
            messages.add_message(request, messages.ERROR, cmntform.errors)
    cmntform = CommentsForm(instance=cmnt)
    return render(request, 'comments_form.html', {'cform': cmntform})


def delete_comment(request, pk):
    cmnt = Comments.objects.get(id=pk)
    post_id = cmnt.post.id
    if request.method == 'POST':
        cmnt.delete()
        return redirect(f'/viewcomments{post_id}')
    return render(request, 'comment_confirm_delete.html', {'postid': post_id})  # postid is needed to redirect to comments page


def update_post(request, pk):
    pobj = Posts.objects.get(id=pk)
    pform = PostsForm(instance=pobj)
    if request.method == 'POST':
        pform = PostsForm(request.POST, instance=pobj)
        if pform.is_valid():
            pform.save()
            return redirect('/')
        else:
             messages.add_message(request, messages.ERROR, pform.errors)
    return render(request, 'post_form.html', {'pform': pform})


def del_post(request, pk):
    if request.method == 'POST':
        pobj = Posts.objects.get(id=pk)
        pobj.delete()
        return redirect('/')
    return render(request, 'post_confirm_delete.html')
