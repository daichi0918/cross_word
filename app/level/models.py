from django.db import models

# Create your models here.


class QuestionAll(models.Model):

    question_id = models.IntegerField()
    # 望月さんが作られた問題集のIDをここで取ってくる
    # gaibu_key = models.ForeignKey()