# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robe''as no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random
 
skaitlis=100

min_rob=101
max_rob=501

for i in range(100):
    random_skaitlis=random.randintint(min_rob, max_rob)
    print(random_skaitlis)
