import sys

class Animal:
    def print(self):
        print("Here is your animal")
        print(f"Length of the arms = {self.armlen} m.")
        print(f"Length of the legs = {self.leglen} m.")
        print(f"Number of eyes = {self.numeyes}.")
        print(f"Does it have a tail? {self.tail}.")
        print(f"Does it have fur? {self.fur}.")
        
    def __init__(self, armlen=1., leglen=2., numeyes=2, tail=False, fur=False ):
        self.armlen = armlen
        self.leglen = leglen
        self.numeyes = numeyes
        self.tail = tail
        self.fur = fur
        
        
def main():
    armlen = 1.
    leglen = 2.
    numeyes=2
    tail=False
    fur=False
    
    if(len(sys.argv)>=2):
        nsides = int(sys.argv[1])
        
    if(len(sys.argv)>=3):
        length = int(sys.argv[2])
        
    if(len(sys.argv)>=4):
        nsides = int(sys.argv[3])
        
    if(len(sys.argv)>=5):
        length = int(sys.argv[4])
        
    if(len(sys.argv)>=6):
        length = int(sys.argv[5])
        
    our_animal = Animal(armlen = armlen, leglen = leglen, numeyes = numeyes, tail = tail, fur = fur)
    our_animal.print()
    
if __name__=="__main__":
    main()