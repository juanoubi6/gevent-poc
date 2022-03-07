import gevent
import requests
import time


def _execute_http_request(number):
    start = time.time()
    result = requests.get("http://localhost/delay/2")
    end = time.time()
    print("result from request {}: {}. Time spent: {}".format(number, result.status_code, end - start))


def requests_test_without_gevent():
    print("starting to execute requests")
    start = time.time()
    for i in range(3):
        _execute_http_request(i+1)
    end = time.time()
    print("executed all requests in: {}".format(end - start))


def requests_test_with_gevent():
    print("starting to execute requests")
    start = time.time()

    greenlet_list = []
    for i in range(3):
        greenlet_list.append(gevent.spawn(_execute_http_request, i))

    _ = gevent.joinall(greenlet_list)

    end = time.time()
    print("executed all requests in: {}".format(end - start))
