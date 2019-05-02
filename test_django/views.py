from django.http import HttpResponse as response
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'aboutus.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    totalcount=len(wordlist)
    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word]=1
    worddict=sorted([(value,key) for (key,value) in worddict.items()])
    return render(request,'count.html',{'totalcount':totalcount,'fulltext':fulltext,'worddict':worddict})
