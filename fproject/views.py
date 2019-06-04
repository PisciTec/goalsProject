from django.shortcuts import render
from .models import Post, Goal
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
	goals = Goal.objects.all()
	return render(request, 'fproject/post_list.html', {'posts': posts, 'goals': goals})
def goal_list(request):
	goals = Goal.objects.all()
	return render(request, 'fproject/goals.html', {'goals': goals})
