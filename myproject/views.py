# i have created this file ##nikhillanje
from django.http import HttpResponse # type: ignore
from django.shortcuts import render #for Templates



def index (request):
    # return HttpResponse("Hello Nikhil")
    #also
    #return HttpResponse("<h1>Hello Nikhil</h1>")\
    #params = {'name':'Nikhil' , 'place':'Mars'}
    return render(request , 'analayze.html' ) #,params)
    



# def analayze (request):
#     djtext = request.GET.get('text','default')
#     removepunc = request.GET.get('removepunc','off')
#     fullcaps = request.GET.get('fullcaps','off')
#     newlineremover = request.GET.get('newlineremover', 'off')
#     extraspceremover = request.GET.get('extraspceremover', 'off')
#     # print(djtext)
#     # print(removepunc)
#     if removepunc == 'on':
#        # analayze = djtext
#        punctuation = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#        analayze = ""
#        for char in djtext :
#            if char not in punctuation :
#                analayze = analayze + char
#        params = {'purpose':'Remove Punctuations' , 'analayze_text':analayze}
#        # return HttpResponse("analayze")
#        return render(request , 'analayze2.html' , params)
#     elif(fullcaps=='on'):
#         analayze = djtext.capitalize()  # Capitalize only the first letter
#         params = {'purpose': 'Change to UpperCase', 'analayze_text': analayze}
#         return render(request, 'analayze2.html', params)
#     elif(newlineremover=='on'):
#         analayze=''
#         for char in djtext :
#             if char !="\n":
#                 analayze = analayze + char.upper()

#                 params = {'purpose': 'Remove New Lines', 'analayze_text': analayze}
#         return render(request, 'analayze2.html', params)
#     elif(extraspceremover=='on'):
#         analayze=""
#         for index , char in enumerate(djtext):
#             if not (djtext[index] == " " and djtext[index+1] == " "):
#                 analayze = analayze + char
#                 params = {'purpose': 'Extra Space Remover', 'analayze_text': analayze}
#         return render(request, 'analayze2.html', params)
#     else :
#         return HttpResponse("Error , Please check the Box")



def analayze(request):
    djtext = request.POST.GET.get('text', 'default')
    removepunc = request.POST.GET.get('removepunc', 'off')
    fullcaps = request.POST.GET.get('fullcaps', 'off')
    newlineremover = request.POST.GET.get('newlineremover', 'off')
    extraspaceremover = request.POST.GET.get('extraspaceremover', 'off')

    operations_done = []
    analyzed = djtext

    if removepunc == 'on':
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuation)
        operations_done.append('Removed Punctuations')

    if fullcaps == 'on':
        analyzed = analyzed.upper()
        operations_done.append('Changed to Uppercase')

    if newlineremover == 'on':
        analyzed = analyzed.replace('\n', ' ').replace('\r', ' ')
        operations_done.append('Removed New Lines')

    if extraspaceremover == 'on':
        analyzed = ' '.join(analyzed.split())
        operations_done.append('Removed Extra Spaces')

    if not operations_done:
        return HttpResponse("Error: Please select at least one operation.")

    params = {
        'purpose': ', '.join(operations_done),
        'analayze_text': analyzed
    }

    return render(request, 'analayze2.html', params)


#Exercise Route
def about (request):
    return HttpResponse("""<h1>Personal Navigator</h1><br>
                        <a href="https://chat.openai.com/" target="_blank" class="chat-link">Try ChatGPT Now</a><br>
                        <a href="https://www.youtube.com/" target="_blank" class="chat-link">Visit YouTube</a><br>
                        <a href="https://www.google.com/" target="_blank" class="chat-link">Visit Google</a><br>
                        <a href="https://www.facebook.com/" target="_blank" class="chat-link">Visit Facebook</a><br>
                        <a href="https://www.instagram.com/" target="_blank" class="chat-link">Visit Instagram</a>

""")

# def capitalizefirst (request):
#     return HttpResponse("capitalizefirst")

# def newlineremove (request):
#     return HttpResponse("newlineremove")

# def spaceremove (request):
#     return HttpResponse("spaceremove")

# def charcount (request):
#     return HttpResponse("charcount")