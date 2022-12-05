scor = b[['reliability_scoring', 'profitability_scoring', 'volatility_scoring']]

scaler = StandardScaler()
scaler1 = scaler.fit_transform(scor)
col_names = list(scor.columns)
scor1 = pd.DataFrame(scaler1, columns=col_names)
b['reliability_scoring'] = scor1['reliability_scoring']
b['profitability_scoring'] = scor1['profitability_scoring']
b['volatility_scoring'] = scor1['volatility_scoring']

# Кластеризируем данные
kmeans = KMeans(n_clusters=3)
kmeans.fit(scor1)
b['total_scor'] = kmeans.labels_

# Находим центры кластеров
centroids = kmeans.cluster_centers_
print(centroids)

# Выгружаем центры кластеров первоначальной выборки и преобразуем их
centroids_first = [[-0.82299872, -0.58702657, 0.27754298], [0.70051727, -0.27611672, -0.92107224],
                   [0.28727921, 1.08138105, 0.67684092]]
centroids_first0 = []
for i in centroids_first[0]:
    i = i
    centroids_first0.append(i)
print(centroids_first0)
centroids_first1 = []
for i in centroids_first[1]:
    i = i
    centroids_first1.append(i)
print(centroids_first1)
centroids_first2 = []
for i in centroids_first[2]:
    i = i
    centroids_first2.append(i)
print(centroids_first2)
# Преобразуем центры кластеров итоговой выборки
centroids0 = []
for i in centroids[0]:
    i = i
    centroids0.append(i)
print(centroids0)
centroids1 = []
for i in centroids[1]:
    i = i
    centroids1.append(i)
print(centroids1)
centroids2 = []
for i in centroids[2]:
    i = i
    centroids2.append(i)
print(centroids2)
# Измеряем евклидово расстояние и определяем сходимость центроидов кластеров
distance_buy1 = math.dist(centroids_first0, centroids0)
distance_buy2 = math.dist(centroids_first0, centroids1)
distance_buy3 = math.dist(centroids_first0, centroids2)
print(distance_buy1)
print(distance_buy2)
print(distance_buy3)
buy = 0
if (distance_buy1 < distance_buy2) & (distance_buy1 < distance_buy3):
    buy += 0
elif (distance_buy2 < distance_buy1) & (distance_buy2 < distance_buy3):
    buy += 1
else:
    buy += 2
print(buy)
distance_hold1 = math.dist(centroids_first1, centroids0)
distance_hold2 = math.dist(centroids_first1, centroids1)
distance_hold3 = math.dist(centroids_first1, centroids2)
print(distance_hold1)
print(distance_hold2)
print(distance_hold3)
hold = 0
if (distance_hold1 < distance_hold2) & (distance_hold1 < distance_hold3):
    hold += 0
elif (distance_hold2 < distance_hold1) & (distance_hold2 < distance_hold3):
    hold += 1
else:
    hold += 2
print(hold)
distance_sell1 = math.dist(centroids_first2, centroids0)
distance_sell2 = math.dist(centroids_first2, centroids1)
distance_sell3 = math.dist(centroids_first2, centroids2)
print(distance_sell1)
print(distance_sell2)
print(distance_sell3)
sell = 0
if (distance_sell1 < distance_sell2) & (distance_sell1 < distance_sell3):
    sell += 0
elif (distance_sell2 < distance_sell1) & (distance_sell2 < distance_sell3):
    sell += 1
else:
    sell += 2
print(sell)
#  Выставляем рекомендации
tot = []
for i in b['total_scor']:
    if i == buy:
        tot1 = 'buy'
    elif i == hold:
        tot1 = 'hold'
    else:
        tot1 = 'sell'
    tot.append(tot1)
b['total_scor'] = tot