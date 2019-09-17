from .celery import app

@app.task
def add(n, m):
    res = n + m
    print(res)
    return res

@app.task
def low(n, m):
    res = n - m
    print(res)
    return res



