import time


def wait_until(*args, timeout=10, interval=1):
    """Decorator function for waiting until referred doesn't throw AssertionError."""

    def _wait_until(func):
        def wrapper(*args_, **kwargs_):
            start_time = time.time()
            while True:
                try:
                    func_result = func(*args_, **kwargs_)
                    return func_result
                except AssertionError as exception:
                    if time.time() - start_time > timeout:
                        raise exception
                    time.sleep(interval)

        return wrapper

    if len(args) == 1 and callable(args[0]):
        # No arguments, call the decorator
        return _wait_until(args[0])
    else:
        # Return the decorator
        return _wait_until
