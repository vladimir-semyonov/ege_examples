from math import dist

stars = [list(map(float, x.replace(',', '.').split())) for x in open('.txt')] #Создаём список, считывая с файла координаты звёзд

n = 3 #Кол-кластеров
clusters = {1:[], 2:[], 3:[]}  #Словарь кластеров 

#Разбиваем звёзды по кластерам
for star in stars:
    x, y = star
    if y > 8:
        clusters[1] += [star]
    elif x > 1:
        clusters[2] += [star]
    else:
        clusters[3] += [star]

#Функция поиска центроида
def centroid(cluster):
    sumres = 10**20
    for a in cluster:
        suma = 0
        for b in cluster:
            suma += dist(a,b) #Вместо создания функции поиска расстояния, используем уже готовую из бибилиотеки math
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
