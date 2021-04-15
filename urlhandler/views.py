from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
import random, string
from .models import shorturl
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})

def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

@login_required(login_url='/login/')
def generate(request):
    if request.method == "POST":
        # generate
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            usr =request.user
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_url=short)
            if not check:
                newurl = shorturl(
                    user=usr,
                    original_url=original,
                    short_url=short,
                )
                newurl.save()
                return redirect(dashboard)
            else:
                messages.error(request, "Already Exists")
                return redirect('/dashboard/')
        elif request.POST['original']:
            # genarate randomly
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = shorturl.objects.filter(short_url=short)
                if not check:
                    newurl = shorturl(
                        user=usr,
                        original_url=original,
                        short_url=short,
                    )
                    newurl.save()
                    return redirect(dashboard)
                else:
                    continue
        else:
            # error
            messages.error(request, "Empty Fields")
            return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')

def home(request, short= None):
    if not short or short is None:
        return render(request,'home.html')
    else:
        try:
            check = shorturl.objects.get(short_url=short)
            check.visits = check.visits + 1
            check.save()
            return redirect(check.original_url)
        except shorturl.DoesNotExist:
            return render(request, 'home.html', {'error':'error'})