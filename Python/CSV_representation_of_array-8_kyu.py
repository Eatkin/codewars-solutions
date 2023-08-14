# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
# 2023-08-02T16:50:41.417+0000
import pandas as pd
import re
def to_csv_text(array):
    # The worst code ever, where pandas is used to turn a 2D array into a CSV text by converting it into a DataFrame, splitting it by newlines, and then performing a complex dance of left-stripping, regex and .replace to achieve the perfect alignment of commas
    # It was worth it
    return re.sub(r" +", ",", "\n".join([x.lstrip() for x in pd.DataFrame(array).to_string(header=False, index=False).split("\n")])).replace(",NaN", "").replace(".0", "")