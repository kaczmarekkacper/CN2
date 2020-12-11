from ImportData import ImportData
from Example import *


if __name__ == '__main__':
    import_data = ImportData.ImportData()
    path_to_data = "Data/"
    # files = ["student-mat.csv", "student-por.csv"]
    files = ["car.data"]
    first_line_skip = True
    prediction_position = -1

    data_raw = import_data.get_data(path_to_data, files, first_line_skip)
    data = []
    for row in data_raw:
        example = Example.Example()
        example.init_values(row, prediction_position)
        data.append(example)
