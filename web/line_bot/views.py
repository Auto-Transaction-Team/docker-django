from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from line_bot.message_creater import create_single_text_message
from line_bot.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(2)
        request = json.loads(request.body.decode('utf-8'))
        events = request['events']
        for event in events:
            message = event['message']
            reply_token = event['replyToken']
            line_message = LineMessage(message_creater.create_single_text_message(message['text']))
            line_message.reply(reply_token)
        return HttpResponse("ok")
    else:
        return HttpResponse("NoMessage")