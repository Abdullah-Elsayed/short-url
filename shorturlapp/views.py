from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UrlForm
from pyshorteners import Shortener


# Create your views here.

def home(request):

    form = UrlForm()
    link = None
    # shorurl = pyshorteners.Shortener()
    # link= shorurl.tinyurl.short('https://www.google.com/search?q=65&oq=65&aqs=edge..69i57j0l5j69i60.514j0j4&sourceid=chrome&ie=UTF-8')
    # print(link)
    if request.method == 'POST':

        #     # Create a form instance and populate it with data from the request (binding):
        form = UrlForm(request.POST)

    #     # Check if the form is valid:
        if form.is_valid():
            
                    # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            try:
                x = form.cleaned_data['url']
                print(x)
                shorurl = Shortener()
                link= shorurl.tinyurl.short(x)
                print(link)
                form = UrlForm()

            except:
                return HttpResponse('pleace check your connection')

    context = {'url': form,'link':link}

    return render(request, 'shorturlapp/index.html', context)
