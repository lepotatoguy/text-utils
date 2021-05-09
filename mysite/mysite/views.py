# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>hello</h1>")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default') #returns text which is passed from index, text na paile default return korbe
    
    #Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    #print(removepunc)
    #print(djtext)

    #check which checkbox is on
    if(removepunc == "on" and fullcaps=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        final = ""
        for char in djtext:
            final = final + char.upper()

        params = {'given_word': 'Removed Punctuations and Changed to Uppercase', 'analyzed_text': final}
        djtext = final
        return render(request, 'analyze.html',params)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'given_word':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #Analyze the text
        return render(request, 'analyze.html',params)
    
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'given_word': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html',params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'given_word': 'Removed NewLines', 'analyzed_text': analyzed}    
    
    

    if(removepunc != "on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

def about(request):
    return render(request, 'about.html')

def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default') #returns text which is passed from index, text na paile default return korbe
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")

def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")

