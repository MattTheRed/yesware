Yesware Coding Challenge
=======================

Clone the repo and install the requirements:

```
pip install -r requirements.txt
````
Run the script and follow the prompts

```
python data_masher.py
```

Imp details and future improvements
===================================

- I used pandas DataFrames, which are a tabular data structure designed to
perform well with large datasets.

- To get the data into a DataFrame I ended up creating a ParsedDataToCsvFile
file like object to manipulate the input file into the correct format on the fly.
If I knew regexs better, I believe there is way to specify custom deliminators
with a regex when importing data with pandas

- Write some tests
