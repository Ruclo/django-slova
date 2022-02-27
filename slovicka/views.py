from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Cvicenie, Pokus, Odpoved
from random import shuffle
from django.contrib.auth.models import Group
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        #return render(request, 'slovicka/index.html')
        return redirect('prihlasenie/')
    else:
        return redirect('home/')

def prihlasenie(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            return redirect('/slovicka/home/')
        else:
            return redirect('/slovicka/')
    else:
        return render(request, 'slovicka/index.html')


def odhlasenie(request):
    logout(request)
    return redirect('/slovicka/prihlasenie/')


# def home(request):
#     if request.user.is_authenticated:
#         if request.user.groups.all():
#             trieda = str(request.user.groups.all()[0])
#         else:
#             trieda = None
#         zoznamcviceni = Cvicenie.objects.filter(trieda=trieda)
#         #print(zoznamcviceni)
#         return render(request, 'slovicka/home.html', context={
#             'cvicenia' : zoznamcviceni
#         })
#     else:
#         return redirect('prihlasenie/')

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.all():
            trieda = str(request.user.groups.all()[0])
        else:
            trieda = None
        zoznamcviceni = Cvicenie.objects.filter(trieda=trieda)
        #print(zoznamcviceni)
        pokusy = [i.cvicenie for i in Pokus.objects.filter(ziak=request.user)]
        hotove = []
        for i in pokusy:
            if i in zoznamcviceni:
                hotove.append(i)
        return render(request, 'slovicka/home.html', context={
            'cvicenia' : zoznamcviceni,
            'hotove' : hotove
        })
    else:
        return redirect('prihlasenie/')

def cvicenie(request, cvicenie_id):
    cvicenie = get_object_or_404(Cvicenie, pk=cvicenie_id)
    if str(request.user.groups.all()[0]) == cvicenie.trieda:
        if request.method=='POST':
            p = Pokus(ziak=request.user, cvicenie=cvicenie)
            p.save()
            spravne_odpovede = []
            for slovicko in cvicenie.slovicko_set.all():
                spravne_odpovede.append(slovicko.jazyk2)
            print(spravne_odpovede)
            odpovede = request.POST.getlist('odpoved')
            print(odpovede)
            for index in range(len(odpovede)):
                spravne = True if odpovede[index] == spravne_odpovede[index] else False
                o = Odpoved(ziak=request.user, pokus=p, odpoved=odpovede[index], jespravne=spravne,
                            spravne=spravne_odpovede[index])
                o.save()
                print(o.jespravne)

            #print(request.POST.items())
            return redirect('/slovicka/home/')
        else:
            if cvicenie.typ == 'Dopisovanie':
                vypracovane = Pokus.objects.filter(ziak=request.user, cvicenie=cvicenie)
                if not vypracovane:
                    slovicka_set = cvicenie.slovicko_set.all()
                    slovicka = []
                    for slovicko in slovicka_set:
                        slovicka.append(slovicko.jazyk1)
                    return render(request, 'slovicka/cvicenia.html', context={'slovicka': slovicka})
                    #return HttpResponse('Toto je tvoje')
                else:
                    return render(request, 'slovicka/done.html')
            elif cvicenie.typ == 'Spajanie':
                vypracovane = Pokus.objects.filter(ziak=request.user, cvicenie=cvicenie)
                if not vypracovane:
                    slovicka_set = cvicenie.slovicko_set.all()
                    slovicka1 = []
                    slovicka2 = []
                    for slovicko in slovicka_set:
                        slovicka1.append(slovicko.jazyk1)
                        slovicka2.append(slovicko.jazyk2)
                    shuffle(slovicka2)
                    return render(request, 'slovicka/cvicenia2.html', context={'slovicka1': slovicka1, 'slovicka2' : slovicka2})
                    # return HttpResponse('Toto je tvoje')
                else:
                    return render(request, 'slovicka/done.html')
    else:
        return HttpResponse('Toto nie je tvoje')


