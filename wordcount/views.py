from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request): #this request parameter will take requests from user whenever user wants to go other pages
    return render(request,'home.html')   #,{'hithere':'this is me'}   bjjbjbj

def about(request):
     return render(request,'about.html')



def count(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()
    worddict ={}
    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1

    sortedwords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    #return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict': worddict.items()})
    return render(request,'count.html',{'fulltext': fulltext,'count':len(wordlist),'sort':sortedwords})
#def eggs(request):
 #   return HttpResponse('<h1>Eggs</h1>')


