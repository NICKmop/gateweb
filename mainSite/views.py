from django.shortcuts import render;
from .models import Post, skills;

# Create your views here - 기초 가이드
def index(request):
    return render(request,'main/index.html');

def blog(request):
    postlist = Post.objects.all();
    return render(request, 'main/blog.html', {'postlist':postlist});

def posting(request, pk):
    post = Post.objects.get(pk=pk);
    return render(request, 'main/posting.html', {'post': post});

# 포트폴리오 URL 실행
def portfolioindex(request):
    skillsList = skills.objects.all();
    print(skillsList);
    return render(request,'portfolio/index.html', {'skillsList':skillsList});
