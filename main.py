import periodictable

symbol = input('No daj symbol ziom: ')
print(periodictable.elements.__getattribute__(symbol).mass)
