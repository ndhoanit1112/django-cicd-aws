
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from app.fibs.tasks import fib_task
from app.fibs.models import FibResult
from app.fibs.cache import FibCache
import os
from django.conf import settings
import uuid


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

        cache = FibCache()
        result = cache.get(input)
        if result is None:
            fib_task.delay(new_fib.id)
            file_path = os.path.join(settings.BASE_DIR, f'app/fibs/temp/{new_fib.id}.txt')
            with open(file_path, "w") as writer:
                random_str = uuid.uuid4().hex
                writer.write(f"{random_str} === {new_fib.id}")
        else:
            new_fib.result = result
            new_fib.status = FibResult.STATUS_SUCCESS
            new_fib.save()

        return redirect("index")
