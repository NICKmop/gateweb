from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50);
    #게시글에 이미지 필드 추가
    mainphoto = models.ImageField(blank=True, null=True);
    contents = models.TextField();
    def __str__(self):
        return self.postname;

class skills(models.Model):
    nokey = models.AutoField(primary_key=True);
    # key sn sds lv
    sn = models.CharField(max_length=200);
    sbs = models.CharField(max_length=200);
    lv = models.CharField(max_length=200);
    # skillstime = models.DateTimeField('date published')
    def __str__(self):
        return "this is a skills : {}".format(self.sn);

class testModel(models.Model):
    test = models.CharField(max_length=50);

    def __str__(self) -> str:
        return 'this is a test : {}'.format( super().__str__());