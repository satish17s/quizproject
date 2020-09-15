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
    correctanswer = models.ManyToManyField('Option',related_name='trivia_answer', blank=True)


    def __str__(self):
        return self.question

class Option(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label


class Player(models.Model):
     name = models.CharField(max_length=250,null=True,blank=True, unique=True)

     def __str__(self):
         return self.name

class Answersheet(models.Model):
     player=models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_name')
     question = models.ForeignKey(Trivia, on_delete=models.CASCADE,related_name='player_question')
     playeranswer=models.ManyToManyField('Option',related_name='player_answer', blank=True)
     date_completed = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.player.name

     def get_player_answer(self):
         return ", ".join([answer.label for answer in self.playeranswer.all()])
