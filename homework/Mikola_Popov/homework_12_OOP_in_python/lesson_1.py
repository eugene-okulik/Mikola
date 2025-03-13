import json


class CountryData:
    def __init__(self, file):
        self.__file = file
        self.__data = self.read_file()
        self.__keys_data = self.search_keys()
        self.__country = self.__data[self.__keys_data[0]]
        self.__evg_temp = self.__data[self.__keys_data[1]]
        self._comfort = self.__is_comfort()

    def read_file(self):
        with open(self.__file, "r+") as file:
            for line in file:
                file_data = json.loads(line)
        return file_data

    def search_keys(self):
        keys = self.__data.keys()
        return list(keys)

    def display_info(self):
        for i in self.__keys_data:
            print(self.__data[i])

    def __is_comfort(self):
        for i in self.__keys_data:
            if isinstance(self.__data[i], int):
                if self.__data[i] >= 25:
                    return f"{self.__data[i]} - Yes comfortable"
                elif self.__data[i] < 25:
                    return f"{self.__data[i]} Not comfortable!!!"

    @property
    def data(self):
        return self.__data

    @property
    def comfort(self):
        return self._comfort

    @comfort.setter
    def comfort(self, value):
        self._comfort = value

    def __str__(self):
        return f"File {self.__file} with data {self.__data}"


class CountryDataWithTemp(CountryData):
    def __init__(self, file):
        super().__init__(file)
        self.min_temp = self.__data[self.__keys_data[2]]


data1 = CountryData("data1.txt")
print(data1)
data1.display_info()
data2 = CountryData("data2.txt")
data2.display_info()
print(data2.comfort)
data3 = CountryData("data3.txt")
print(data3.data)
data3.display_info()
print(data3.comfort)
