import sys
import random
import string

class passwordGenerator:
    def __init__(self): 
        self.data = []

        self.length = 16
        self.num = 3

        self.punctuation = True
        self.digits = True
        self.letters = True

        if(self.argExists(2)):
            self.length = int(sys.argv[1])
        
        if(self.argExists(3)):           
            self.num = int(sys.argv[2])
 
        if(self.argExists(4)):           
            self.punctuation = self.isBool(sys.argv[3])
         
        if(self.argExists(5)):           
            self.digits = self.isBool(sys.argv[4])
 
        if(self.argExists(6)):
            self.letters = self.isBool(sys.argv[5])

        if not self.letters and not self.digits and not self.punctuation:
            print("one item must be true")
            sys.exit()

    def argExists(self,num):
        return len(sys.argv) >= num

    def isBool(self,arg):
        if arg.lower() in ["true","True","yes","y","Ja","1","correct","yo"]:
            return True
        else:
            return False

    def pwgen(self):
        random_source = ""
        password = ""

        if self.letters:
            random_source += string.ascii_letters
            password += random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)

        if self.digits:
            random_source += string.digits
            password += random.choice(string.digits)

        if self.punctuation:
            random_source += string.punctuation
            password += random.choice(string.punctuation)

        for i in range(self.length):
            password += random.choice(random_source)

        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)

        return password

    def create(self):
        for i in range(self.num):
            print(self.pwgen())
        

pwGEN = passwordGenerator()

pwGEN.create()