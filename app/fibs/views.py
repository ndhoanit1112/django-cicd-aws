
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from app.fibs.tasks import fib_task
from app.fibs.models import FibResult


@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("GET")

    if request.method == "POST":
        input = request.POST.get("number")

        if not input:
            return HttpResponseBadRequest()
        
        new_fib = FibResult.objects.create(
            input=input,
            status=FibResult.STATUS_PENDING,
        )
        
        fib_task.delay(new_fib.id)

        return HttpResponse("Processing!")
