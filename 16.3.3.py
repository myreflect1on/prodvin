words = 'the world is mine take a look what you have started'.split()
s = map((lambda x: '"'+x+'"'), words)
print(*s)