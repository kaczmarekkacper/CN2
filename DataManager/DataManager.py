import csv
import random


class DataManager:
    def __init__(self):
        self.paths = []
        self.objects = []

    def get_data(self, path, files, first_line_skip):
        data = []
        files = eval(files)
        for file in files:
            path_to_file = path + file
            with open(path_to_file, newline='') as f:
                reader = csv.reader(f)
                data_from_path = list(reader)
            if first_line_skip:
                data_from_path = data_from_path[1:len(data_from_path)]
            data.append(data_from_path)
        self.__merge_tables(data)
        return self.objects

    def __merge_tables(self, data_to_merge):
        for data in data_to_merge:
            self.objects += data

    @staticmethod
    def split_sets(data, sets_number, seed):
        train_set = []
        test_sets = []
        for i in range(sets_number - 1):
            test_sets.append([])
        sets_by_class = DataManager.__split_data_by_class(data)
        for set_to_split in sets_by_class:
            subsets = []
            size = len(set_to_split)
            index_from = 0
            for i in range(sets_number):
                index_to = round(size/sets_number*(i+1))
                subsets.append(set_to_split[index_from:index_to])
                index_from = index_to
            train_set += subsets.pop(0)
            for i in range(sets_number-1):
                test_sets[i] += subsets[i]
        DataManager.__randomize_set(train_set, seed)
        for test_set in test_sets:
            DataManager.__randomize_set(test_set, seed)
        return train_set, test_sets

    @staticmethod
    def __split_data_by_class(data):
        sets_by_class = []
        labels = {}
        for example in data:
            if example.value not in labels.keys():
                labels.update({example.value: len(sets_by_class)})
                sets_by_class.append([])
            sets_by_class[labels[example.value]].append(example)
        return sets_by_class

    @staticmethod
    def __randomize_set(set_to_randomize, seed):
        random.Random(seed).shuffle(set_to_randomize)

    @staticmethod
    def get_selectors(data):
        size_of_attr = len(data[0].attributes)
        list_of_attr = []
        for i in range(size_of_attr):
            for example in data:
                DataManager.__append_attribute_if_unique(i, example.attributes[i], list_of_attr)
        return list_of_attr

    @staticmethod
    def __append_attribute_if_unique(i, attribute, list_of_attr):
        attr = [i, attribute]
        if attr not in list_of_attr:
            list_of_attr.append(attr)

    @staticmethod
    def get_classes(data):
        list_of_classes = []
        for example in data:
            DataManager.__append_value_if_unique(example.value, list_of_classes)
        return list_of_classes

    @staticmethod
    def __append_value_if_unique(value, list_of_classes):
        if value not in list_of_classes:
            list_of_classes.append(value)
