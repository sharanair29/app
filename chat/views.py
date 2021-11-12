from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chat.bot import chat4
from chat.models import ConvoChats
from django.contrib import messages
# Create your views here.


ls2=[]

@csrf_exempt
def get(request):
    userText = str(request.GET.get("msg")) # data from input
    while True:
        print(userText)
        ls2.append(f'User: {userText}')
        bot_reply = chat4(userText)
        ls2.append(f'BrowserBot: {bot_reply}')
        print(ls2)
        return HttpResponse(str(bot_reply))


def index(request):
    return render(request, 'trialbot/bot.html')
    
@csrf_exempt
def store(request):
    if request.method == 'POST':
        message = ls2

        store = ConvoChats(message=message)

        store.save()
        messages.success(request, 'Your conversations have been uploaded for bot training')
        return redirect('index')
