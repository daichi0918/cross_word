from django.db import models

# Create your models here.
class VerticalHint(models.Model):
    
    crossword_id = models.IntegerField(default=0)
    hint = models.CharField(max_length=500)

    def __str__(self):
        
        cross_word = str(self.crossword_id)
        return "Quiz" + cross_word

class HorizonalHint(models.Model):
    
    crossword_id = models.IntegerField(default=-1)
    hint = models.CharField(max_length=500)

    def __str__(self):

        cross_word = str(self.crossword_id)
        return "Quiz" + cross_word

class Cross_wordSomething(models.Model):

    crossword_id = models.IntegerField(default=-1)
    crossword_ans = models.CharField(max_length=500)
    crossword_ans_comment = models.CharField(max_length=500)
    crossword_js = models.CharField(max_length=500)

    def __str__(self):

        crossword_id = str(self.crossword_id)
        return "Cross_wordSomething_" + crossword_id



