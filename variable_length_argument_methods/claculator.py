

class Calculator:

    def operation(self,*args,**kwargs):

        #print(args) # (10,20)
        #print(kwargs) # {"op":"+"}

        if kwargs.get("op")=="+":

            return args[0]+args[1]
        
        if kwargs.get("op")=="-":

            return args[0]-args[1]
        
    


calculator_instance = Calculator()

print(calculator_instance.operation(10,20,op="+"))
print(calculator_instance.operation(10,20,op="-"))



