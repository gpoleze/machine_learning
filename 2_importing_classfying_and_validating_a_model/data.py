import csv


def load_data(file_path):
    X = []
    Y = []

    with open(file_path, "r") as input:
        reader = csv.reader(input)
        next(reader)

        for home, how_to, contact, buy in reader:
            X.append([int(home), int(how_to), int(contact)])
            Y.append(int(buy))

    return X, Y


if __name__ == '__main__':
    file_path = "acesso_pagina.csv"
    X, Y = load_data(file_path)

    from sklearn.naive_bayes import MultinomialNB

    model = MultinomialNB()
    model.fit(X, Y)

    results = model.predict(X)
    print(results)
