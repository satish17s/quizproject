from django.shortcuts import render,get_object_or_404
from .models import Trivia,Option,Player, Answersheet
from django.utils import timezone
from .forms import TriviaForm,OptionForm,PlayerForm,AnswersheetForm



def playgame(request):
    pk = Trivia.objects.first().pk
    # import pdb; pdb.set_trace();
    player=Player.objects.all()
    return render(request,'triviaapp/question.html', {'pk': pk,'form':'PlayerForm'})

def getname(request,pk=None):
    if request.method=='GET':
        return render(request,'triviaapp/getname.html',{'form':PlayerForm()})
    else:
        try:
            form=PlayerForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['name']
                form.save()
                # pk = Player.objects.first().pk
                # if pk:
                #     player = Player.objects.get(pk=pk)
                # else:
                #     Player = Player.objects.first()
                request.session['name'] = username
            pk = Trivia.objects.first().pk
            return render(request,'triviaapp/playgame.html',{ "pk": pk})

        except ValueError:
            return render(request,'triviaapp/getname.html',{'form':TriviaForm,'error':'bad data input'})


def question(request,pk=None):
    if request.POST:
        print("*"*100, pk)
        print(request.POST)
        question = Trivia.objects.get(pk=pk)
        player, player_created = Player.objects.get_or_create(name__icontains=request.session['name'])
        answers = Option.objects.filter(id__in=request.POST.get('option'))
        answer, created = Answersheet.objects.get_or_create(
            question=question,
            player=player
        )
        # answer.playeranswer.clear()
        answer.playeranswer.add(*request.POST.getlist('option'))
        answer.save()
    last_trivia=Trivia.objects.last()
    if pk:
        trivia = Trivia.objects.get(pk=pk)
    else:
        trivia = Trivia.objects.first()
    # if pk==2:
    #     player = Player.objects.get(name__iexact=request.session['name'])
    #     answers = Answersheet.objects.filter(player=player)
    #     print("ANSWERS", answers.count())
    #     return render(request,'triviaapp/summary.html', {"answers": answers})
    return render(request,'triviaapp/question.html', {'trivia': trivia,'last_id':last_trivia.id, "pk": 2})


def history(request):
    answers = Answersheet.objects.all()
    return render(request,'triviaapp/history.html', {"answers": answers})


def summary(request):
    player = Player.objects.get(name__iexact=request.session['name'])
    answers = Answersheet.objects.filter(player=player)
    print("ANSERRRRrr", answers.count())


    return render(request,'triviaapp/summary.html', {"answers": answers})
