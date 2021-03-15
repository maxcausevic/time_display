from django.shortcuts import render, redirect
from time import gmtime, strftime
    
def index(request):
    context = {
        "date":strftime("%Y-%m-%d"),
        "time": strftime("%H:%M %p")
    }
    return render(request,'index.html', context)



