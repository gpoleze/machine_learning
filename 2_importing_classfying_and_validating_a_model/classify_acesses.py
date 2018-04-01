from functions.load_data_from_file import read_csv
from sklearn.naive_bayes import MultinomialNB

X, Y = read_csv("2_importing_classfying_and_validating_a_model/acesso_pagina.csv")

training_x = [X[index] for index in range(90)]
training_y = [Y[index] for index in range(90)]

testing_x = [X[index] for index in range(90, len(X))]
testing_y = [Y[index] for index in range(90, len(Y))]

model = MultinomialNB()
model.fit(training_x, training_y)

results = model.predict(testing_x)
print(f'results:{results}')

diff = results - testing_y
print(f"diff:\t{diff}")
success = [value for value in diff if value == 0]
print(f"success:{success}")
success_rate = len(success) / len(testing_y) * 100
print(f"success rate: {success_rate:.2f}%")
