# print("in calc", __name__)

def add():
    return 'addition'

def sub():
    return 'substraction'

if __name__ == "__main__":
    print(add())
    print(sub())
    
class Computer:
     
    def config(self):
        print("i7, 16GB, 1TB")
        
con1 = Computer()

con1.config()