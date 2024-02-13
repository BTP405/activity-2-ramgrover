import matplotlib.pyplot as plt

with open('q2.txt') as f:
    contents = f.readlines()
    print(contents)
a = []
for i in contents:
    a.append(int(i))
p =0
for i in a:
    p = p+i
print(p)

y = [0,0,0,0,0,0]

for i in a:
    if i<=10:
        if i >= 0:
            y[1] = y[1] + 1
    if i<=20:
        if i > 10:
            y[2] = y[2] + 1
    if i<=30:
        if i > 20:
            y[3] = y[3] + 1
    if i<=40:
        if i > 30:
            y[4] = y[4] + 1
    if i<=50:
        if i > 40:
            y[5] = y[5] + 1
y[0] = y[1]
print(y)
# corresponding y axis values 
x = [0,10,20,30,40,50] 
    
# plotting the points  
plt.bar(x,y, width=5.0) 

    
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
    
# giving a title to my graph 
plt.title('My first graph!') 
    
# function to show the plot 
plt.show() 
plt.savefig('snowfallbyharnoor.png')
