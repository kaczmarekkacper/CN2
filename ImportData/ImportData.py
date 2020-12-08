import csv


class ImportData:
    def __init__(self):
        self.paths = []
        self.objects = []

    def get_data(self, path):
        self.paths.append(path + 'student-mat.csv')
        self.paths.append(path + 'student-por.csv')
        data = []
        for path in self.paths:
            with open(path, newline='') as f:
                reader = csv.reader(f)
                data_from_path = list(reader)
            data_from_path = data_from_path[1:len(data_from_path)]
            data.append(data_from_path)
        self.__merge_tables(data)
        return self.objects

    def __merge_tables(self, data_to_merge):
        for data in data_to_merge:
            self.objects += data
