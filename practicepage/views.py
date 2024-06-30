from django.http import HttpResponse
from django.shortcuts import render

data = {'people': [
        {
            'id': 5,
            'name': 'yonny',
            'year': 2002
        },
        {
            'id': 1,
            'name': 'lucy',
            'year': 1998
        },
        {
            'id': 4,
            'name': 'mark',
            'year': 2001

        }
        ]
       }



def home(request):
    return render(request,'home/home.html', data)

def aboutUs(request):
    return HttpResponse("this is the about us page")