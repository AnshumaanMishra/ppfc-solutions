points = []
t = int(input())
while(t > 0):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)

    points.append((a, b))
    t -= 1

sp = sorted(points)

def eucDist(point1, point2):
    return ((point1[1] - point2[1])**2 + (point1[0] - point2[0])**2)

def closestPair(points):
    if(len(points) == 1 or len(points) == 0):
        return float('inf'), [(float('inf'), float('inf')), (float('-inf'), float('-inf'))]
    if(len(points) == 2):
        return eucDist(points[0], points[1]), [points[0], points[1]]
    elif (len(points) == 3):
        d1 = eucDist(points[0], points[1])
        d2 = eucDist(points[1], points[2])
        d3 = eucDist(points[0], points[2])
        if(d1 > d2):
            if(d3 > d2):
                return d2, [points[1], points[2]]
            else:
                return d3, [points[0], points[2]]
        else:
            if(d3 > d1):
                return d1, [points[0], points[1]]
            else:
                return d3, [points[0], points[2]]
        return eucDist(points[0], points[1])

    def divideIntoTwo(points, mid):
        left, right = [], []
        for i in points:
            if(i[0] < mid[0]):
                left.append(i)
            else:
                right.append(i)
        return left, right

    def division(points, k):
        separated = []
        # k = k**0.5
        for i in points:
            if(abs(i[0] - mid[0]) < k):
                separated.append(i)
        return separated

    mid = points[len(points) // 2]
    left, right = divideIntoTwo(points, mid)
    k1, pair1 = closestPair(left)
    k2, pair2 = closestPair(right)
    if(k1 < k2):
        k = k1
        pair = pair1
    else:
        k = k2
        pair = pair2

    separated = division(points, k)
    # print("Separated: ", separated)
    separated = sorted(separated, key=lambda x: x[1])
    for i in range(0, len(separated)):
        for j in range(1, 8):
            if(i + j >= len(separated)):
                break

            currentDist = eucDist(separated[i], separated[i + j])
            if(currentDist < k):
                k = currentDist
                pair = [points[i], points[j]]

    return k, pair

minDist, (point1, point2) = closestPair(sp)
print(minDist)
