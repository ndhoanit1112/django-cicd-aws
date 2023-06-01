from django.http import HttpResponse
from app.polls.models import Poll
from datetime import datetime
import random
import socket


def index(request):
    time_now = datetime.now().strftime("%Y%m%d_%H%M")
    number = random.randint(100)
    Poll.objects.create(name=f"Poll {time_now}", number=number)
    new_poll = Poll.objects.all().order_by("-id").first()
    return HttpResponse(f"Hello, world. You're at the polls index. Latest Poll: {new_poll.name} - {new_poll.number}. IP: {socket.gethostbyname(socket.gethostname())}. Code updated at: 202306011252.")