from logger import logging

def add(a,b):

    logging.debug("The Addition operation is happening")
    return a+b

logging.debug("The Function is called")
add(23,35)