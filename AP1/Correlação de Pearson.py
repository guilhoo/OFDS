# Código feito por Paulo Guilherme Da Cunha Dias Furtado
# para a matéria de Oficina de Desenvolvimento de Sistemas 1,
# matéria ministrada pelo professor Fabio Santos da Silva,
# Universidade do Estado do Amazonas, 2021.

# Correlação de Pearson

import math

users = {

			"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2, "Norah Jones": 4.5, "Phoenix": 5, "Slightly Stoopid": 1.5, 
							"The Strokes": 2.5, "Vampire Weekend": 2},

			"Bill": {"Blues Traveler": 2, "Broken Bells": 3.5, "Deadmau5":4, "Phoenix": 2, "Slightly Stoopid": 3.5, "Vampire Weekend": 3},

			"Chan": {"Blues Traveler": 5, "Broken Bells": 1, "Deadmau5": 1, "Norah Jones": 3, "Phoenix": 5, "Slightly Stoopid": 1},

			"Dan": {"Blues Traveler": 3, "Broken Bells": 4, "Deadmau5": 4.5, "Phoenix": 3, "Slightly Stoopid": 4.5, "The Strokes": 4,
							"Vampire Weekend": 2},
			
			"Hailey": {"Broken Bells": 4, "Deadmau5": 1, "Norah Jones": 4, "The Strokes": 4, "Vampire Weekend": 1},

			"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4, "Norah Jones": 5, "Phoenix": 5, "Slightly Stoopid": 4.5, "The Strokes": 4,
							"Vampire Weekend": 4},

			"Sam": {"Blues Traveler": 5, "Broken Bells": 2, "Norah Jones": 3, "Phoenix": 5, "Slightly Stoopid": 4, "The Strokes": 5},

			"Veronica": {"Blues Traveler": 3, "Norah Jones": 5, "Phoenix": 4, "Slightly Stoopid": 2.5, "The Strokes": 3},

			"Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5, "The Strokes": 4.25, "Weird AI": 4},

			"Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird AI": 1},

		}

def pearson(x, y):

# Numerador da Fórmula:

	n = 0
	xj = 0

	for i in x: 
		if i in y:
			xj += (x[i] * y[i])
			n += 1

	xi = 0
	yi = 0

	for i in x:
		if i in y:
			xi += x[i]

	for i in y:
		if i in x:
			yi += y[i]

	numerador = xj - ((xi * yi)/ n)

	numerador = round(numerador, 2)

# Denominador da Fórmula:

	# Elemento mais a esquerda do denominador

	x2 = 0

	for i in x:
		if i in y:
			x2 += x[i] ** 2

	xi2 = xi ** 2

	d1 = (xi2/n)

	d1 = (x2 - d1)

	d1 = d1 ** 0.5


	# Elemento mais a direita do denominador

	y2 = 0

	for i in y:
		if i in x:
			y2 += y[i] ** 2 

	yi2 = yi ** 2

	d2 = (yi2/n)

	d2 = (y2 - d2)

	d2 = d2 ** 0.5

	denominador = (d1 * d2)

# Realizando último cálculo

	corr_pearson = (numerador/denominador)

	return corr_pearson

print(pearson(users["Angelica"], users["Bill"]))
print(pearson(users["Angelica"], users["Hailey"]))
print(pearson(users["Angelica"], users["Jordyn"]))