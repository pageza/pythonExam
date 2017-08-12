from django.shortcuts import render,redirect
from django.db import models
from django.db.models import Count
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.

# declared two arrays to divide between favourites
favourites = []
quotes = []

# populate the quotes array
bigQuotes = Quote.objects.all()
for quote in bigQuotes:
    quotes.append(quote)


def index(request):

    return render(request, 'main/index.html')

def create_user(request):
    #validate and create UserManager
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name= request.POST.get('name'),
            email= request.POST.get('email'),
            password= bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
        )
        request.session['user_id']= user.id
        return redirect('/quotes')
    return  redirect('/')

def log_in(request):
    login = User.objects.log_in(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        return redirect('/quotes')
    return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')

def success(request):

    user = User.objects.filter(id=request.session['user_id']).first()
    context = {
        'user': user,
        'quotes': quotes,
        'favourites' : favourites
            }
    return render(request, 'main/success.html', context)

def create_quote(request):
    if len(request.POST.get('author')) < 4 :
        messages.error(request, 'Author must be more that 3 Letters')
    if len(request.POST.get('quote')) < 10 :
        messages.error(request, 'Quote must be more that 10 Letters')
    else :
        quote = Quote.objects.create(
            author = request.POST.get('author'),
            quote = request.POST.get('quote'),
            posted_by = User.objects.filter(id=request.session['user_id']).first(),
            )
        quotes.append(quote)
    return redirect('/quotes')

def delete(request, id):
    Quote.objects.filter(id=id).delete()
    return redirect('/quotes')

def user(request, id):
    user = User.objects.filter(id=id).first()
    quotes = Quote.objects.filter(posted_by=id).annotate(count=Count('posted_by'))
    context = {
        'user' : user ,
        'quotes' : quotes,
    }
    return render(request, 'main/user.html',context)

def add(request, id):
    quotes.remove(Quote.objects.get(id=id))
    favourites.append(Quote.objects.get(id=id))
    return redirect('/quotes')

def remove(request, id):
    favourites.remove(Quote.objects.get(id=id))
    quotes.append(Quote.objects.get(id=id))
    return redirect('/quotes')
