from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import People



def home(request):
    data = People.objects.all()
    return render(request,'home/home.html', {'people': data})

def aboutUs(request):
    return HttpResponse("this is the about us page")

def personDetail(request, id):
    data = People.objects.get(pk=id)
    return render(request,'home/person.html', {'person': data})

def add(request):
    name = request.POST.get("name") #gets the data from the POST
    year = request.POST.get("year")

    if name and year:
        person = People(name=name, DOB=year)
        person.save() #saves obj to the db
        return HttpResponseRedirect('/home')

    return render(request, 'home/add.html')

def delete(request, id):

    try: #error handling
        person = People.objects.get(pk=id)
    except:
        raise Http404("Person Does Not Exist")
    
    person.delete()#delete from the db
    return HttpResponseRedirect('/home')