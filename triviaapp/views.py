from django.shortcuts import render,get_object_or_404
from .models import Trivia,Option,Player
from django.utils import timezone
from .forms import TriviaForm,OptionForm,PlayerForm


def playgame(request):
    pk = Trivia.objects.first().pk
    # import pdb; pdb.set_trace();
    player=Player.objects.all()
    return render(request,'triviaapp/question1.html', {'pk': pk,'form':'PlayerForm'})

def getname(request):
    if request.method=='GET':
        return render(request,'triviaapp/getname.html',{'form':PlayerForm()})
    else:
        try:
            form=PlayerForm(request.POST)
            if form.is_valid():
                form.save()
                # pk = Player.objects.first().pk
                # if pk:
                #     player = Player.objects.get(pk=pk)
                # else:
                #     Player = Player.objects.first()
                # request.session['player'] = trivia.player
            return render(request,'triviaapp/playgame.html',{'form':PlayerForm})

        except ValueError:
            return render(request,'triviaapp/getname.html',{'form':TriviaForm,'error':'bad data input'})


def question1(request, pk=None):
    if pk:
        trivia = Trivia.objects.get(pk=pk)
    else:
        trivia = Trivia.objects.first()
    return render(request,'triviaapp/question1.html', {'trivia': trivia})


def summary(request,todo_pk):
    todo=get_object_or_404(Trivia,pk=trivia_pk)
    if request.method=='POST':
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')


def history(request):
    pass
