from app.celery import app
from app.fibs.cache import FibCache
from app.fibs.models import FibResult

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

        cache = FibCache()
        cache.set(fib_result.input, result)
    except Exception as e:
        fib_result.status = FibResult.STATUS_ERROR
        fib_result.message = str(e)[:90]

    fib_result.save()
