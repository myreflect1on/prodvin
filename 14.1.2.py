import turtle as t
m = [250,-90,50,-90,250,-90,50,-90]
[t.forward(i) if i > 0 else t.right(int(abs(i))) for i in m]

