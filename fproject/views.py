from django.shortcuts import render, get_object_or_404
from .models import Post, Goal
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
	goals = Goal.objects.all()
	return render(request, 'fproject/post_list.html', {'posts': posts, 'goals': goals})
def goal_list(request):
	goals = Goal.objects.all()
	return render(request, 'fproject/goals.html', {'goals': goals})
def post_detail(request,pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'fproject/post_detail.html', {'post': posts})
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
		
	return render(request, 'fproject/post_edit.html', {'form': form})

def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'fproject/post_edit.html', {'form': form})

def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'fproject/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)
def post_remove(request,pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')