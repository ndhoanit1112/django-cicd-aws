from app.celery import app
from app.fibs.cache import FibCache
from app.fibs.models import FibResult
import os
from django.conf import settings

def fib(n):
    if n < 0:
        raise ValueError("Unable to handle negative numbers!")
    
    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

@app.task(bind=True)
def fib_task(self, result_id):
    fib_result = FibResult.objects.get(pk=result_id)

    try:
        result = fib(fib_result.input)
        fib_result.result = result
        fib_result.status = FibResult.STATUS_SUCCESS

        file_path = os.path.join(settings.BASE_DIR, f'app/fibs/temp/{result_id}.txt')
        if os.path.isfile(file_path):
            with open(file_path, "r") as reader:
                content = reader.read()
                fib_result.message = f"{content} === {result}"

        cache = FibCache()
        cache.set(fib_result.input, result)
    except Exception as e:
        fib_result.status = FibResult.STATUS_ERROR
        fib_result.message = str(e)[:90]

    fib_result.save()
