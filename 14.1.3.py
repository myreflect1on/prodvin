import turtle as t
m = [-22.5,50,-90,50,-90,50,-90,50,-112.5,50,-90,50,-90,50,-90,50,-112.5,50,-90,50,-90,50,-90,50,]
[t.forward(i) if i > 0 else t.left(int(abs(i))) for i in m]