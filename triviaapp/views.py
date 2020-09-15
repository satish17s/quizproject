from django.shortcuts import render,get_object_or_404
from .models import Trivia
from django.utils import timezone
from .forms import TriviaForm,OptionForm,PlayerForm


def playgame(request):
    pk = Trivia.objects.first().pk
    # import pdb; pdb.set_trace();
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
            return render(request,'triviaapp/playgame.html',{})

        except ValueError:
            return render(request,'triviaapp/getname.html',{'form':TriviaForm,'error':'bad data input'})


def question1(request, pk=None):
    if pk:
        trivia = Trivia.objects.get(pk=pk)
    else:
        trivia = Trivia.objects.first()
    return render(request,'triviaapp/question1.html', {'trivia': trivia})



def question11(request):
    if request.method=='GET':
        return render(request,'triviaapp/question1.html',{'form':TodoForm()})
    else:
        try:
            trivia=Trivia()
            form=TriviaForm(request.POST)
            newtrivia=form.save(commit=False)
            newtrivia.save()
            return redirect('question2')
        except ValueError:
            return render(request,'triviaapp/question1.html',{'form':TodoForm,'error':'bad data input'})


def question2(request,todo_pk):
    todo=get_object_or_404(Trivia,pk=trivia_pk)
    if request.method=='POST':
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')

def summary(request,todo_pk):
    todo=get_object_or_404(Trivia,pk=trivia_pk)
    if request.method=='POST':
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')


def viewtodo(request,todo_pk):
    todo=get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if request.method=='GET':
        form=TodoForm(instance=todo)
        return render(request,'todoapp/viewtodo.html',{'todo':todo,'form':form})
    else:
        try:
            form=TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request,'todoapp/viewtodo.html',{'todo':todo,'form':form,'error':'bad data input'})


def history(request):
    pass
