from django.http import HttpResponse
import socket


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. IP: {socket.gethostbyname(socket.gethostname())}")