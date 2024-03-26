from functools import wraps

from django.core.cache import cache


def cache_result(cache_key, timeout=3600):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = cache.get(cache_key)
            if not result:
                result = func(*args, **kwargs)
                cache.set(cache_key, result, timeout)
            return result

        return wrapper

    return decorator


@cache_result("cache_key")
def get_data():
    return "data"
