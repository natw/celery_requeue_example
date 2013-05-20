In one shell, run:

    celery worker -A requeue

In another, run

    python requeue.py

to poll using `result.ready()`.

Run

    python requeue.py wait

to just sleep for longer than the task takes.

When using `result.ready()`, the result is requeued after calling `result.get`.
