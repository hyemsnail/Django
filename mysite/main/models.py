from django.db import models

# Create your models here.
class Content(models.Model):
    content = models.TextField(verbose_name='content') # 관리자나 폼에서 필드 이름을 content라고 표시하게 한다.

    def __str__(self):
        return self.content # 모델의 인스턴스가 문자열로 변환될 때 content의 필드를 반환