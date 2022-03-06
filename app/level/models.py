from django.db import models

# Create your models here.



class QuestionAll(models.Model):

    question_id = models.IntegerField()
    # 望月さんが作られた問題集のIDをここで取ってくる
    # gaibu_key = models.ForeignKey()



class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    # def __str__(self):
    #     return '<Friend:id=' + str(self.id) + ', ' + \
