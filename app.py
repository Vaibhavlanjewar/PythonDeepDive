import logging

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def div(a, b):
    try:
        result = a // b
        logger.debug(f"Dividing {a} // {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero error when dividing {a} by {b}")
        return None

# Test the functions
add(10, 5)
sub(10, 5)
mul(10, 5)
div(10, 5)
div(10, 0)
