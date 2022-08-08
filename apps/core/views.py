from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    #a = 10
    #bb = 'teste jkdasfhasdkfhasdfhjkasdf'
    
    return render(request, 'core/index.html')