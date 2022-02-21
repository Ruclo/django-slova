from django.shortcuts import redirect

def index(request):
    if not request.user.is_authenticated:
        #return render(request, 'slovicka/index.html')
        return redirect('/slovicka/prihlasenie/')
    else:
        return redirect('/slovicka/home/')

