import pandas as pd

class ParsedDataToCsvFile(file):
    """File wrapper based on http://stackoverflow.com/a/14279543/190597, but using
    read() instead of next() since pandas filereader imp changed"""
    def read(self, *args):
        lines = super(ParsedDataToCsvFile, self).read(*args)
        new_chunk = ""
        for line in lines.split("\n"):
            new_chunk+= self.parse_to_csv(line)
        return new_chunk

    def parse_to_csv(self, line):
        # PUNT: Do regex checking to verify names. This is sloppy
        names = line.split(" --")[0].split(",")
        if len(names) > 1:
            new_line = "%s\n" % ",".join(names)
            return new_line
        else:
            return ""


class NameData(object):
    """Imports name data into a pandas dataframe and exposes
    methods to aggregate data"""
    def __init__(self, filename="test-data.txt"):
        self.import_data(filename)

    def import_data(self, filename):
        """read data from txt file into a dataframe object"""
        self.df = pd.read_csv(ParsedDataToCsvFile(filename, "r"), \
            header=None, names=["last", "first"])

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
        pass
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
