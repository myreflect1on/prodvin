import random as r
def generate_ip():
    passw = str(r.randint(1, 256)) + '.' + str(r.randint(0, 256))+ '.' + str(r.randint(0, 256))+ '.' + str(r.randint(1, 255))
    return passw