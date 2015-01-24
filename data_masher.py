import pandas as pd
import re

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
        name_str = line.split(" --")[0]
        if re.match("^[,a-zA-Z\s]+$", name_str) is not None:
            names = name_str.split(", ")
            if len(names) > 1:
                new_line = "%s\n" % ",".join(names)
                return new_line
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
        return len(self.df.drop_duplicates())

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
        if n > self.unique_first_names or n > self.unique_last_names:
            raise Exception("We don't have enough unique names for that!")
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
        return [", ".join(x) for x in zip(last_names, list(first_names)[::-1])]

if __name__ == "__main__":
    filename = raw_input("What is your filename? (test-data.txt)\n") \
        or "test-data.txt"
    n = raw_input("How many random names do you want? (25)\n") or 25
    nd = NameData(filename)

    print "#1: # of unique full names:"
    print nd.unique_full_names
    print "\n"
    print "#1: # of unique first names:"
    print nd.unique_first_names
    print "\n"
    print "#1: # of unique last names:"
    print nd.unique_last_names
    print "\n"
    print "#2: 10 most common last names"
    print nd.most_common_last_names
    print "\n"
    print "#3: 10 most common first names"
    print nd.most_common_first_names
    print "\n"
    print "#4: N modified names"
    print nd.modified_names(n=int(n))

