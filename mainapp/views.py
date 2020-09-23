from django.shortcuts import render, redirect
from django.views.generic.base import View

def index(request):
    return render(request, 'pages/index.html')

# приклад додавання нової сторінки

# def test(request):
#     data = {
#         "serial_header": True # створення умови для відображення хедера
#     }
#     return render(request, 'pages/test.html', context=data)

