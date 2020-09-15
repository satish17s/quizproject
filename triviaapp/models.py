from django.db import models
# Create your models here.

class Trivia(models.Model):

    STATUS_CHOICES = (
        (1, "Single"),
        (2, "Multiple")
    )
    question = models.CharField(max_length = 250)
    type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    options= models.ManyToManyField('Option',related_name='trivia_options')
    answer = models.ManyToManyField('Option',related_name='trivia_answer', blank=True)
    player = models.ForeignKey('Player',on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Option(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label


class Player(models.Model):
     name = models.CharField(max_length=250,null=True,blank=True)

     def __str__(self):
         return self.name
