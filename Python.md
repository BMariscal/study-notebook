WSGI gateway and concurrent requests
---

https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive
http://xplordat.com/2020/02/16/a-flask-full-of-whiskey-wsgi/


Weak References within threads
---

https://medium.com/pipedrive-engineering/weak-references-and-objects-management-in-python-threads-589226044d8e


Python Multithreading and Multiprocessing Tutorial
---

https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python


MULTIPROCESSING VS. THREADING IN PYTHON: WHAT YOU NEED TO KNOW
---
https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/


Exploring Concurrency in Python & AWS
---
https://www.awsadvent.com/2016/12/04/exploring-concurrency-in-python-aws/


How to use Flask with gevent
---
https://iximiuz.com/en/posts/flask-gevent-tutorial/



GUNICORN  sync and async types
---
https://stackoverflow.com/questions/38425620/gunicorn-workers-and-threads
Workers are the number of processes that get spawned. Threads are the number of threads in each process.

Threads is only meaningful with the threaded worker. Every other worker type ignores that setting and runs one thread per process.
https://github.com/benoitc/gunicorn/issues/1045

https://www.spirulasystems.com/blog/2015/01/20/gunicorn-worker-types/
https://medium.com/@nhudinhtuan/gunicorn-worker-types-practice-advice-for-better-performance-7a299bb8f929




Better performance by optimizing Gunicorn config
---
https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7

Python3 Features
--
https://towardsdatascience.com/features-you-likely-dont-use-in-python-3-but-you-should-2d79dba4cfb3

Asyncio
--
https://cheat.readthedocs.io/en/latest/python/asyncio.html

https://www.integralist.co.uk/posts/python-asyncio/

https://medium.com/@interfacer/intro-to-async-concurrency-in-python-and-node-js-69315b1e3e36

https://stackoverflow.com/questions/34753401/difference-between-coroutine-and-future-task-in-python-3-5#:~:text=The%20coroutine%20is%20scheduled%20to,the%20result%20of%20the%20operation.

https://docs.python.org/3.4/library/asyncio-task.html




What is port sharding in Linux and why should I care
--
https://blog.n0p.me/2018/02/2018-02-20-portsharding/

Orchestrating a Background Job Workflow in Celery for Python
--
https://www.toptal.com/python/orchestrating-celery-python-background-jobs

The Flask Mega-Tutorial 
--
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs


Thread pool
---
https://en.wikipedia.org/wiki/Thread_pool
