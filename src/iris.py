#!/usr/bin/env python3

# This file holds the Naive Bayes classifier implementation for 'iris.csv' dataset.

from csv import reader
from random import seed
from naive_bayes import NaiveBayesClassifier


class Iris:


    def __init__(self):

        self.dataset_filename = 'datasets/iris.csv'
        self.description_filename = 'datasets/iris.names'
        self.nbc = NaiveBayesClassifier()
        self.dataset = self.nbc.load_dataset_from_csv(self.dataset_filename)


    def classify_data(self):

#        print('Enter the data to be classified')

        print('\nTrying to classify the new data: [5.6, 3.1, 4.0, 1.2]')

        model = self.nbc.divide_data_params_by_class(self.dataset)
        row = [5.6, 3.1, 4.0, 1.2]
        label = self.nbc.predict(model, row)

        print(f'\nPredicted: {label}')


    def calculate_accuracy(self):

        n_folds = 5
        scores = self.nbc.evaluate_algorithm(self.dataset, n_folds)

        print('\n\nCalculating the accuracy of the classifier using the iris.csv dataset...')
        print('\nResampling: k-fold cross validation split')
        print('\nAccuracy (5 folds): %.3f%%\n' % (sum(scores) / float(len(scores))))


    def show_dataset_description(self):

        csv_reader = reader(self.description_filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:

            print(row)


    def show_dataset_rows(self):

        csv_reader = reader(self.dataset_filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:

            print(row)


    def run(self):

        seed(1)

        print('\n=================================')
        print('          Iris dataset')
        print('=================================\n')

        for i in range(len(self.dataset[0]) - 1):
            self.nbc.string_column_to_float(self.dataset, i)

        self.nbc.string_column_to_int(self.dataset, len(self.dataset[0]) - 1)

        print()

        print('\nChoose the action:')
        print('\n1. Classify new data.')
        print('2. Calculate algorithm accuracy.')
        print('3. Show dataset rows.')
        print('4. Show dataset description\n')


        while True:

            choice = input('Choice: ')

            if choice not in ['1', '2', '3', '4']:
                print('Wrong choice! Please choose option 1-4.')

            elif choice == '1':

                try:
                    self.classify_data()
                    continue
                except KeyboardInterrupt:
                    continue

            elif choice == '2':

                try:
                    self.calculate_accuracy()
                    continue
                except KeyboardInterrupt:
                    continue

            elif choice == '3':

                try:
                    self.show_dataset_description()
                    continue
                except KeyboardInterrupt:
                    continue

            elif choice == '4':

                try:
                    self.show_dataset_rows()
                    continue
                except KeyboardInterrupt:
                    continue

            else:
                raise


def main():

    iris = Iris()
    iris.run()


if __name__ == "__main__":

  #  try:
        main()
#    except:
 #       print('\nAn error has occurred during the program execution!\n')

