from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment


def home(request):
    comment = Comment.objects.filter().order_by('-date')
    return render(request,'index.html',{'comment':comment})


def gallery(request):
    return render(request, 'gallery.html')

def hobby(request):
    return render(request, 'hobby.html')

def music(request):
    return render(request, 'music.html')
    
def place(request):
    return render(request, 'place.html')


def index(request):
    comment = Comment.objects.filter().order_by('-date')
    comment_form = CommentForm()
    return render(request,'index.html',{'comment':comment, 'comment_form': comment_form})

def create(request):

    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) 
        finished_form.save()
        return redirect('home')


def delete(request, comment_id):
    deleteComment = get_object_or_404(Comment,pk=comment_id)
    deleteComment.delete()
    return redirect('home')


def update(request, comment_id):
    updateComment = get_object_or_404(Comment,pk=comment_id)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            updateComment.comment=form.cleaned_data["comment"]
            updateComment.save()
            return redirect('home')

    else:
        form=CommentForm()
    return render(request,'update.html',{'form':form})