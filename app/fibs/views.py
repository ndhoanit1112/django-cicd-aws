
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from app.fibs.tasks import fib_task
from app.fibs.models import FibResult


def index(request):
    if request.method == "GET":
        results = FibResult.objects.order_by("-id")[:16]
        context = {
            'results': results,
            'status_error': FibResult.STATUS_ERROR
        }
        return render(request, 'fibs/list.html', context=context)

    if request.method == "POST":
        input = request.POST.get("number")
        if not input:
            return HttpResponseBadRequest()
        
        new_fib = FibResult.objects.create(
            input=input,
            status=FibResult.STATUS_PENDING,
        )
        
        fib_task.delay(new_fib.id)

        return redirect("index")
