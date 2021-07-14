import logging

## Logging method

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

##Logging attributes : 'DEBUG' , 'INFO' , 'WARNING' , 'ERROR' , 'CRITICAL'

#logging.disable(logging.DEBUG)
## Disable aal the logging statments below the priority level of WARNING

def factorial(n):
    logging.info('The input number is:'+str(n))
    fact = 1 ;
    for i in range(1,n+1):
        logging.debug('The number is : '+str(i))
        fact = fact * i
    logging.warning('The factorial of number is:'+str(n))    
    print('Factorial of the number:'+ str(fact))
    return fact

logging.critical(factorial(5))
    

