from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .forms import SnippetForm
from .models import NewTour
from django.urls import reverse
from django.shortcuts import get_object_or_404

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            category = form.cleaned_data['category']

            send_mail(
                    "Заявка на підбір туру", 
                    "Ім'я клієнта: " + name + ". Телефон: " + phone + ". Спосіб комунікації: " + category+ ".", 
                    "from",
                    ["igorechekqwerty@gmail.com", ],
                    fail_silently=False
                    )
        return redirect(reverse('index', kwargs={}, args={}))
    form = ContactForm()
    return render(request, 'pages/index.html', {'form':form})

def all_tours(request):
    show_all = NewTour.objects.all()
    data = {'serial_header' : True,
            'show_all' : show_all}
    return render(request, 'pages/all_tours.html', context=data)

def hot_tours(request):
    show_hot = NewTour.objects.filter(is_hot_tour=True)
    data ={'serial_header' : True,
            'show_hot' : show_hot}
    return render(request, 'pages/hot_tours.html', context=data)

def blog(request):
    data ={'serial_header' : True}
    return render(request, 'pages/blog.html', context=data)

def in_search(request):
    tour = request.GET.get('destination-country')
    # city_from =
    # flight_date =
    # nights = 
    # persons = 
    print("Testing search button", tour)
    return render(request, 'pages/search_tour.html')


######## 

def snippet_detail(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            print('VALID')
    form = SnippetForm()
    form.save()
    return render(request, 'pages/index.html', {'form':form})















# class get_message(View):
#     def get(self, request):
#         if request.method == 'POST':
#             name = request.POST['clientName']
#             phone = request.POST['clientPhone']
#             communication_methods = request.POST['clientChoise']
#             contact = ContactUs(name = name, phone=phone, communication_methods=communication_methods)
#             contact.save()
#             try:
#                 send_mail(
#                     "Someone searchig a tour", 
#                     "Ім'я: " + name + " Телефон: " + phone + " Спосіб комунікації: " + communication_methods, 
#                     "wowrvua@gmail.com", 
#                     "igorechekqwerty@gmail.com", 
#                     fail_silently=False
#                     )
#             except:
#                 print("Failed to send email!")
#         return redirect('index')

# приклад додавання нової сторінки

# def test(request):
#     data = {
#         "serial_header": True # створення умови для відображення хедера
#     }
#     return render(request, 'pages/test.html', context=data)

