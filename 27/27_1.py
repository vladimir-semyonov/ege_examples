stars = [list(map(float, x.replace(',', '.').split())) for x in open('.txt')] #Создаём список, считывая с файла координаты звёзд

n = 4 #Кол-кластеров
clusters = {1:[], 2:[], 3:[] , 4:[]} #Словарь кластеров

#Разбиваем звёзды по кластерам
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
#Функция поиска расстояния между звёздами
def r(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

#Функция поиска центроида
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

#Ищем среднее арифметическое для центроидов
px, py = 0, 0
for cl in clusters:
    center = centroid(clusters[cl])
    px += center[0]
    py += center[1]

print(int((px/n)*10000), int((py/n)*10000))
