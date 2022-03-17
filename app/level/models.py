from django.db import models

# Create your models here.


class QuestionAll(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    question_id = models.IntegerField()
    # 望月さんが作られた問題集のIDをここで取ってくる?
    # gaibu_key = models.ForeignKey()
    # def __str__(self):
    #     return self.question_id

    # def get_title(self):
    #     try:
    #         return self.title
    #     except:
    #         return False

    # def get_memo(self):
    #     try:
    #         return self.memo
    #     except:
    #         return False

    # def get_question_id(self):
    #     try:
    #         return self.question_id
    #     except:
    #         return False

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'
