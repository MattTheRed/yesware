import pandas as pd

class NameData(object):
    """Imports name data into a pandas dataframe and exposes
    methods to aggregate data"""
    def __init__(self, filename):
        pass

    def import_data(self):
        """read data from txt file into a dataframe object"""
        # Regex to match format

    @property
    def unique_full_names(self):
        self._get_unique_count("full")

    @property
    def unique_first_names(self):
        self._get_unique_count("full")

    @property
    def unique_last_names(self):
        self._get_unique_count("full")

    def _get_unique_count(self, column):
        pass

    @property
    def most_common_last_names(self):
        self._get_most_common("last")

    @property
    def most_common_first_names(self):
        self._get_most_common("first")


    def _get_most_common(self, column):
        pass

    @property
    def modified_names(self, n=25):
        # slice off the top n elements
        # copy new data into another temp df object
        # to check against



if __name__ == "main":
    # Handle custom file name input
    filename = "test-data.txt"
    nd = NameData(filename)

    # 1
    # print nd.unique_full_names
    # print nd.unique_first_names
    # print nd.unique_last_names

    # 2
    #print nd.unique_first_names

    # 3
    # print nd.unique_first_names

    # 4
    # print nd.modified_names
