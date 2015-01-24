from data_masher import NameData
from contextlib import contextmanager
import tempfile
import os


# Can't just use StringIO to mock files because of my filelike wrapper
# so using this instead
# http://stackoverflow.com/questions/11892623/python-stringio-and-compatibility-with-with-statement-context-manager
@contextmanager
def tempinput(data):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(data)
    temp.close()
    yield temp.name
    os.unlink(temp.name)


def test_one_unique_full_name_count():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        assert nd.unique_full_names == 3

def test_one_unique_first_name_count():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        assert nd.unique_first_names == 3

def test_one_unique_last_name_count():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        assert nd.unique_last_names == 2

def test_two_common_last_names():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        assert nd.most_common_last_names[0] == 3

def test_three_common_first_names():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        assert nd.most_common_first_names[0] == 2

def test_four_common_first_names():
    data = "Moore, Matt --\nMoore, Matt --\nJohn, Smith --\nMoore, Mary\nJones, Anthony\nGallow, Sarah"
    with tempinput(data) as temp_file:
        nd = NameData(temp_file)
        names = nd.modified_names(n=3)
        assert len(names) == 3
        assert "Moore, Matt" not in names
