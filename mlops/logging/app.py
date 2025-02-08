import logging

# logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Arithmaetic App")

def add(x,y):
    result = x+y
    logger.debug(f"Addition of {x}+{y}={result}")
    return result

def subtract(x,y):
    result = x-y
    logger.debug(f"Subtraction of {x}-{y} = {result}")
    return result

def multiplication(x,y):
    result = x*y
    logger.debug(f"multiplication of {x}*{y} = {result}")
    return result

def division(x,y):
    try:
        result = x / y
        logger.debug(f"Addition of {x}/{y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None
    
add(10,20)
subtract(50,20)
multiplication(10,20)
division(10,0)