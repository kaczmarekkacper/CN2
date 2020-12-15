import configparser
from DataManager import DataManager
from Example import *
from CN2 import Algorithm
from Statistics import ConfusionMatrix, Counter


def get_config():
    config = configparser.ConfigParser()
    config_file = "config.ini"
    config.read(config_file)
    which_data = config['DEFAULT']['data']
    path_to_data = config[which_data]['path_to_data']
    files = (config[which_data]['files'])
    first_line_skip = bool(config[which_data]['first_line_skip'])
    prediction_position = int(config[which_data]['prediction_position'])
    sets_number = int(config[which_data]['sets_number'])
    seed = int(config[which_data]['seed'])
    min_significance = float(config[which_data]['min_significance'])
    max_star_size = int(config[which_data]['max_star_size'])
    return path_to_data, files, first_line_skip, prediction_position, sets_number, seed, min_significance, max_star_size


if __name__ == '__main__':
    path_to_data, files, first_line_skip, prediction_position, sets_number, seed,\
                                                                min_significance, max_star_size = get_config()
    data_manager = DataManager.DataManager()
    data_raw = data_manager.get_data(path_to_data, files, first_line_skip)
    data = []
    for row in data_raw:
        example = Example.Example()
        example.init_values(row, prediction_position)
        data.append(example)
    train_set, test_sets = data_manager.split_sets(data, sets_number, seed)

    alg = Algorithm.Algorithm(train_set)
    alg.selectors = data_manager.get_selectors(data)
    classes = data_manager.get_classes(data)
    alg.min_significance = min_significance
    alg.max_star_size = max_star_size
    alg.learn()
    for test_set in test_sets:
        alg.test(test_set)
        confusion_matrix = ConfusionMatrix.ConfusionMatrix.make_confusion_matrix(test_set, classes)
        for row in confusion_matrix:
            print(row)
        print("\n")
        counter = Counter.Counter.count_predictions(test_set)
        print("{:d} na {:d} = {:.2f}%".format(counter, len(test_set), counter / len(test_set) * 100))
        print("\n")
