from django.http import HttpResponse
from django.shortcuts import render     #To pass html files as  output to HttpResponse 
import operator

def homepage(request):
    #return HttpResponse('This is the Homepage') ---> this is only to display any text
    #return render(request, 'home.html', {'Value':'From Dictionary'})  # We can pass dictionary here. 
    #The value of the corresponding key will be displayed. Code to display is in home.html within {{}}
    return render(request, 'home.html')
    


def count(request):
    fulltext = request.GET['fulltext'] 
    print(fulltext)
    #here fulltext is the name given in textarea of home.html
    wordsplit = fulltext.split() 

    worddictionary = {}
    for word in wordsplit:
        if word in worddictionary:
            #Increment the value
            worddictionary[word] += 1 
        else:
            #new value found. write to dictionary
            worddictionary[word] = 1


    sortword = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {"fulltext" : fulltext, "count" : len(wordsplit), "sortword" : sortword})

def about(request):
    return render(request, 'about.html')