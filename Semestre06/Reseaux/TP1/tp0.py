from collections import Counter
import os,time

def exo_init():
    a = set([1,3])
    b = set([2,4])

    print(a^b) # Output: {1, 2, 3, 4}
    print(a|b) # Output: {1, 2, 3, 4}
    print(a&b) # Output: set()
    print(a-b) # Output: {1, 3}

    t = list(range(1,100))
    print(t[5:20:2]) # Slice By 2

    s = "Bonjour Monsieur Bambrik"
    print(Counter(s.lower().split())) # Count Every Word
    print("oussama bellatreche".title()) # 'Oussama Bellatreche'
    
    s = "Python"
    print(s.ljust(10))        # 'Python    '
    print(s.center(10))       # '  Python  '
    print(s.rjust(10))        # '    Python'
    print(s.center(10, '*'))  # '**Python**'

    os.system("explorer /") # Open File Explorer
    time.sleep (5) 
    os.system ("explorer http:\\\\www.google.com") # Open Google
    time.sleep (5)
    os.system ("shutdown /s") # Eteindre PC

if __name__ == "__main__":    
    exo_init()
    
