class Arithmetic :
    def __init__(self,variable1,variable2,operation):
        self.operation=operation
        self.variable1=variable1
        self.variable2=variable2
    def validate(self):
        if self.operation not in ['+', '-', '*', '/']:
            print("Invalid operation")
        if self.operation=='/' and self.variable2==0 :
            print("Error: Division by zero")
        else :
            print("Starting The Operation")
    def calculate(self):
        self.validate()
        match self.operation:
             case '+' :
              return self.variable1+self.variable2
             case '-' :
              return self.variable1-self.variable2
             case '*':
              return self.variable1*self.variable2
             case '/':
              return self.variable1/self.variable2
             
            
    
try :             
   a=float(input("Enter a Number :"))
   b=float(input("Enter a Number :"))
   c=input("Enter a Operation :")
   outer=Arithmetic(a,b,c)
   
   result=outer.calculate()
   print("Result:", result)

except Exception as e:
    print("Error:", e)
    
    
    
        
    


              
              
                
            
            
            
         
        
        
        
        