import os
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        name = old_function.__name__    
        data_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(str(f'{data_time}, {result}, {name}, {args, kwargs} \n' ))
        return result 
    return new_function

def logger_param(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            name = old_function.__name__    
            data_time = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(str(f'{data_time}, {result}, {name}, {args, kwargs} \n' ))
            return result 
        return new_function
    return __logger