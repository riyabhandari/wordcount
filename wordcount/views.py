from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['txt']
    wordslist=text.split()
    worddict={}
    for word in wordslist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sort=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':text,'count':len(wordslist),'worddict':sort})

def about(request):
    return render(request,'about.html')
