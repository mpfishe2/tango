from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .libraries.ModelService import ChatDBX
import json, uuid, os

# env variables
load_dotenv()
DATABRICKS_TOKEN = os.environ['DATABRICKS_TOKEN']
DATABRICKS_URL = os.environ['DATABRICKS_URL']


def chat_view(request):
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())
    return render(request, "chat/chat.html", {"session_id": request.session['session_id']})

@csrf_exempt
def submit_message_view(request):
    if request.method == 'POST':
        try:
            sender = request.POST.get('sender')
            content = request.POST.get('content')
            session_id = request.POST.get('session_id')
            photo = request.FILES.get('photo')
            
            if sender and content and session_id:
                message_obj = Message(sender=sender, content=content, session_id=session_id)
                if photo:
                    message_obj.photo = photo
                message_obj.save()
            else:
                return HttpResponse(status=400)
            
            ## REPLY
            print(message_obj.content)
            reply = ChatDBX(DATABRICKS_TOKEN, DATABRICKS_URL, message_obj.content, "databricks-dbrx-instruct")
            print(reply)
            # reply = 'Hello!'

            return HttpResponse(reply, content_type='text/plain')
        except Exception as e:
            print(e)
            return HttpResponse(status=406)
    return HttpResponse(status=405)
