from django.db import models

# Create your models here.
class Guest(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdata = models.DateTimeField()
    
    class Meta:
        #ordering = ('-title', 'id') # 1차키 2차키(타이틀이 같으면 아이디로 정렬)
        ordering = ('-id',)