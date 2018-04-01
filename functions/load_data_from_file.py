import csv


def read_csv(file_path):
    def reader_function(X, Y, reader):
        for home, how_to, contact, buy in reader:
            X.append([int(home), int(how_to), int(contact)])
            Y.append(int(buy))
        return X, Y

    return __read_file(file_path, reader_function)


def read_csv_with_categories(file_path, categories):
    def reader_function(X, Y, reader):
        for home, search, logged, buy in reader:
            categoric_variable = [1 if search == category else 0 for category in categories]
            X.append([int(home), categoric_variable, int(logged)])
            Y.append(int(buy))
        return X, Y

    return __read_file(file_path, reader_function)


def __read_file(file_path, reader_fucntion):
    X, Y = [], []

    with open(file_path, "r") as input:
        reader = csv.reader(input)
        next(reader)
        X, Y = reader_fucntion(X, Y, reader)

    return X, Y
