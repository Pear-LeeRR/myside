from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Book


def index(request):
    return HttpResponse('Hello, world!')


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'book_list': book_list,
    }
    return render(request, 'lib/detail.html', context=context)


def addBook(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        pub_house = request.POST['pub_house']

    Book.objects.create(name=name, author=author, pub_house=pub_house, pub_date=timezone.now())

    # 重定向
    return HttpResponseRedirect(reverse('lib:detail'))


def delBook(request, book_id):
    Book.objects.filter(pk=book_id).delete()
    return HttpResponseRedirect(reverse('lib:detail'))

