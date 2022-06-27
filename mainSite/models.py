from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50);

    #게시글에 이미지 필드 추가
    mainphoto = models.ImageField(blank=True, null=True);
    contents = models.TextField();

    def __str__(self):
        return self.postname;

