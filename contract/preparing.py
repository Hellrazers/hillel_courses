import functools
import logging



logger = logging.getLogger('api')

def logger_api(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        base_url = args[0].path
        if kwargs.get('item_id') is not None:
            base_url += f'/{kwargs["item_id"]}'


        if kwargs.get("data") is not None:
            logger.info(f'Request: Method: {func.__name__.split('_')[0].upper()} path: {base_url} and payload: {kwargs.get("data")}')
        else:
            logger.info(f'Request: Method: {func.__name__.split('_')[0].upper()} path: {base_url}')
        reps = func(*args, **kwargs)
        logger.info(f'Response: {reps.json()} and status code: {reps.status}')
        return reps
    return wrapper
