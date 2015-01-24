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
        names = line.split(" --")[0].split(", ")
        if len(names) > 1:
            new_line = "%s\n" % ",".join(names)
            return new_line
        else:
            return ""


class NameData(object):
    """Imports name data into a pandas dataframe and exposes
    methods to aggregate data"""
    def __init__(self, filename):
        self.import_data(filename)

    def import_data(self, filename):
        """read data from txt file into a dataframe object"""
        self.df = pd.read_csv(ParsedDataToCsvFile(filename, "r"), \
            header=None, names=["last", "first"])

    @property
    def unique_full_names(self):
        pass
        # Could use drop_duplicates() if I don't need original data
        # self._get_unique_count("full")

    @property
    def unique_first_names(self):
        return self._get_unique_count("first")

    @property
    def unique_last_names(self):
        return self._get_unique_count("last")

    def _get_unique_count(self, column):
        return len(self.df[column].value_counts())

    @property
    def most_common_last_names(self):
        return self._get_most_common("last")

    @property
    def most_common_first_names(self):
        return self._get_most_common("first")


    def _get_most_common(self, column):
        return self.df[column].value_counts()[:10]

    def modified_names(self, n=None):
        if not n:
            n = 25
        # Using sets for faster lookup times for when n is large
        first_names = set()
        last_names = set()
        i = 1
        for pk, row in self.df.iterrows():
            if not row["first"] in first_names and not row["last"] in last_names:
                first_names.add(row["first"])
                last_names.add(row["last"])
                i += 1
            if i > n:
                break
        return [", ".join(x) for x in zip(first_names, list(last_names)[::-1])]

def go():
    nd = NameData("test-data.txt")
    print nd.modified_names()

if __name__ == "__main__":
    print "in here"
    # Handle custom file name input
    filename = "test-data.txt"
    nd = NameData(filename)

    print "#1: # of unique first names:"
    # print nd.unique_full_names
    print nd.unique_first_names
    print "#1: # of last first names:"
    print nd.unique_last_names

    print "#2: 10 most common last names"
    print nd.most_common_last_names

    print "#3: 10 most common first names"
    print nd.most_common_first_names

    print "#4: N modified names"
    print nd.modified_names()

    # 4
    # print nd.modified_names
