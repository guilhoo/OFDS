import math

users = {

 		   "Paulo": {"Coldplay": 5.0, "Imagine Dragons": 4.0, "Cage the Elephant": 4.3, "Artic Monkeys": 3.0},

 		   "Eloa": {"Coldplay": 3.0, "Imagine Dragons": 2.5, "Cage the Elephant": 5.0, "Fleet Foxes": 3.5},

 		   "Will": {"Imagine Dragons": 5.0, "Cage the Elephant": 1.5, "Fleet Foxes": 2.0, "The Ink Spots": 4.0},

 		   "João": {"Coldplay": 1.5, "Cage the Elephant": 3.0, "Fleet Foxes": 3.5, "Artic Monkeys": 5.0}, 

 		   "Miguel": {"Coldplay":5.0, "Fleet Foxes": 4.6, "Artic Monkeys": 5.0, "The Ink Spots": 1.0},

 		  }

def minkowski (rating1, rating2, r):

	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0

def manhattan(rating1, rating2):

	distance = 0
	for i in rating1:
		if i in rating2:
			distance = distance + abs(rating1[i] - rating2[i])

	return distance

def computeNearestNeighbor(username, users):

	distances = []
	for user in users:
		if user != username:
			distance = minkowski(users[user], users[username], 2)
			distances.append((distance, user))

	distances.sort()
	return distances

def recommend(username, users):

	nearest = computeNearestNeighbor(username, users)[0][1]
	recommendations = []

	neighborRatings = users[nearest]
	userRatings = users[username]

	for i in neighborRatings:
		if not i in userRatings:
			recommendations.append((i, neighborRatings[i]))

	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

""" Paulo Guilherme Da Cunha Dias Furtado """
""" Sistema de recomendação colaborativa utilizando minhas bandas favoritas e meus amigos."""

print("\nTestando a funcção Minkowski:")
a = minkowski(users["Eloa"], users["Paulo"], 1)
print(a)

print("\nTestando a funcção de Vizinho mais Próximo:")
b = computeNearestNeighbor("Paulo", users)
print(b)

print("\nTestando a funcção de Recomendação para o usuário informando:")
c = recommend("Miguel", users)
print(c)
