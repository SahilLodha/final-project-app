#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import numpy as np

def euclidean(point, data):
    return np.sqrt(np.sum((point - data)**2, axis=1))


class KNeighborsClassifier():
    def __init__(self, k=5, dist_metric='euclidean'):
        self.k = k
        self.dist_metric = dist_metric

    def fit(self, X_train):
        self.X_train = X_train

    def predict(self, X_test):

        if self.dist_metric == 'euclidean':
            distances = euclidean(X_test.to_numpy(), self.X_train.to_numpy())
            x_train_copy = self.X_train.copy()
            x_train_copy['distance'] = distances
        x_train_copy = x_train_copy.loc[x_train_copy.distance>0]
        x_train_copy = x_train_copy.sort_values(by='distance', ascending=True).iloc[:self.k]
        x_train_copy = x_train_copy.drop('distance', axis=1).sum(axis=0)
        x_train_copy = x_train_copy.loc[lambda x : (x > 0)]
        x_train_copy = x_train_copy.sort_values(ascending=False)

        return x_train_copy


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodMart.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
