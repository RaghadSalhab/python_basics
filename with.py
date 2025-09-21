class myContext:
    def __enter__(self):
        print('welcome ')
        return('this is with value')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('good bye iam leaving')
        print(f"exc_type: {exc_type}")
        print(f"exc_val: {exc_val}")
        print(f"exc_tb: {exc_tb}")
       # return True
       # then the program will continue 

with myContext() as value:
    print('inside')
    print(f'the value is {value}')
    raise ValueError('its an error ops')
print("Program continues") 
