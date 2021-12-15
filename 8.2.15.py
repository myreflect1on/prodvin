n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

l1= n + m - x - t
l2 = m + k - y - t
l3 = n + k - z - t
p2 = l1 + l2 + l3
p1 = (n - l1 - l3 - t) + (m - l1 - l2 - t) + (k - l2 - l3 - t)
p3 = a - p1 - p2 - t
print(p1)
print(p2)
print(p3)
