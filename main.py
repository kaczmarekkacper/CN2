from ImportData import ImportData
from Student import *

if __name__ == '__main__':
    import_data = ImportData.ImportData()
    path_to_data = "Data/"
    data_raw = import_data.get_data(path_to_data)
    data = []
    for row in data_raw:
        student = Student.Student(row)
        data.append(data)
    
