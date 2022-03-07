from gevent import monkey

from requests_example import requests_test_without_gevent, requests_test_with_gevent

if __name__ == '__main__':
    # Should take 6 seconds
    requests_test_without_gevent()

    # Should take 6 seconds too as request library is not monkey patched, so every request is a blocking IO
    requests_test_with_gevent()

    monkey.patch_socket()

    # Should take 2 seconds as each request becomes a non-blocking IO
    requests_test_with_gevent()
