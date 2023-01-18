from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={"name":"Umang","class":"MCA"}
    return render(request, "index.html",params)
    # return HttpResponse("Home")

def analyze(request):
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    uppercase=request.POST.get("uppercase","off")
    newlineremove=request.POST.get("newlineremove",'off')
    spaceremove=request.POST.get("spaceremove","off")
    charcnt=request.POST.get("charcnt","off")
    analyzed=djtext
    if(removepunc=="on"):
        tempanalyzed=""
        punchuation='''"'!@#$%^&*()\,<>~.?/:;'''
        for char in djtext:
            if char not in punchuation:
                tempanalyzed+=char
        analyzed=tempanalyzed
    if(uppercase=="on"):
        print(analyzed)
        analyzed=analyzed.upper()
        print(analyzed)
    if(newlineremove=="on"):
        tempanalyzed=""
        for char in analyzed:
            if(char!="\n" and char!="\r"):
                tempanalyzed+=char
        analyzed=tempanalyzed
    if(spaceremove == "on" ):
        tempanalyzed=""
        for index,char in enumerate(analyzed):
            if not(analyzed[index]==" " and analyzed[index+1]==" "):
                tempanalyzed+=char
        analyzed=tempanalyzed
    if(charcnt=="on"):
        analyzed=""
        cnt=0
        for char in djtext:
            cnt+=1
        analyzed="Total character is:"+str(cnt)

    if(removepunc == "off" and uppercase == "off" and newlineremove=="off" and spaceremove=="off" and charcnt=="off"):
        return HttpResponse("Please check the boxes")
    # return HttpResponse("Remove punchuation")
    
    params = {'purpose': "Remove punctuation", "analyze_text": analyzed}
    return render(request, 'analyze.html',params)