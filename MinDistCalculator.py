import random

points= [(random.randint(0,10),random.randint(1,10))for _ in range(4)]

print("Points: ",points)

def euclideanDistance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

distances = []
for i in range(len(points)-1):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))
        
print("Minimum Distance: ",min(distances))