import pickle


def read_pop_from_file():
    with open('pop.pkl', 'rb') as in_file:
        pops = pickle.load(in_file)
        for el in pops['scores']:
            print(str(el['the_worst']))

read_pop_from_file()
