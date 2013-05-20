In one shell, run:

    celery worker -A requeue

In another, run

    python requeue.py

to poll using `result.ready()`.

Run

    python requeue.py wait

to just sleep for longer than the task takes.

When using `result.ready()`, the result is requeued after calling `result.get`, so it'll just sit around until it expires. When just sleeping, the result message is collected as you'd expect and the result queue disappears.
