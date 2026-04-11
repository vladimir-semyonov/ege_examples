stars = [list(map(float, x.replace(',', '.').split())) for x in open('2b.txt')]
n = 4

clusters = {1:[], 2:[], 3:[] , 4:[]} #5:[]}
for star in stars:
    x, y = star
    if x > 23:
        clusters[1] += [star]
    elif y > 16:
        clusters[2] += [star]
    elif x > 15:
        clusters[3] += [star]
    else:
        clusters[4] += [star]
def r(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def centroid(cluster):
    sumres = 10**20
    for a in cluster:
        suma = 0
        for b in cluster:
            suma += r(a,b)
            if suma < sumres:
                sumres = suma
                res = a
    return res

px, py = 0, 0
for cl in clusters:
    center = centroid(clusters[cl])

    px += center[0]
    py += center[1]

print(int((px/n)*10000), int((py/n)*10000))
