import math as m
def ax2(pair): return pair**2
def ax3(pair): return pair**3
def ain2(pair): return pair**0.5
def aabs(pair): return abs(pair)
def asin(pair): return m.sin(pair)
n = int(input())
func = {'квадрат':ax2(n), 'куб':ax3(n), 'корень':ain2(n), 'модуль':aabs(n), 'синус':asin(n)}
print(func[input()])