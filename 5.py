def isFactorial(n) : 
    i = 1; 
    while(True) : 
          
        if (n % i == 0) : 
            n //= i; 
              
        else : 
            break;  
              
        i += 1; 
  
    if (n == 1) : 
        return True;  
      
    else : 
        return False;  
def findnumber(n):
    t=True
    while t:
        if isFactorial(n):
            print(n,"Is a factorial of number")
            t=False
        else:
            n+=1
            
if __name__ == "__main__" :  
    n = int(input());  
    findnumber(n)
        