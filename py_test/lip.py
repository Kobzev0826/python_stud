import matplotlib.pyplot as plt

start_point = [0,0]
L = int(input ("Dlina: "))
H = int(input ("H: "))
h = int(input ("h: "))
N = int(input("N: "))

x1 = start_point[0]
y1 = start_point[1] - H

x2 = start_point[0] + (L / 2)
y2 = start_point[1] - h

x3 = start_point[0] + L
y3 = start_point[1] - H
#----------расчет центра дуги-----------------------------------------
A = x2 - x1
B = y2 - y1
C = x3 - x1
D = y3 - y1
E = A * (x1 + x2) + B * (y1 + y2)
F = C * (x1 + x3) + D * (y1 + y3)
G = 2 * (A * (y3 - y2) - B * (x3 - x2))
#Если G = 0, это значит, что через данный набор точек провести окружность нельзя.
#print(G)
Cy = (A * F - C * E) / G
Cx = (D * E - B * F) / G
R = ( (y1 - Cy)**2 + (x1 - Cx)**2 )**0.5
print(Cx,Cy,R)
#--------------цикл-----------------------------------------------
X_list = []
Y_list = []
dx = L / (N-1)
#print(dx)
x = start_point[0]
for i in range(N):
    print(i,x)
    y = Cy + (R**2 - ( (x-Cx)**2 ))**0.5

    plt.plot([x,x],[y,start_point[1]])
    X_list.append(x)
    Y_list.append(y)
    x = x + dx

#print(X_list)
#print(Y_list)
#------------------вывод графика--------------------------
plt.plot(X_list,Y_list)
plt.plot([start_point[0],x3],[start_point[1],start_point[1]])
plt.show()