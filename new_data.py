from _openai import getNewData
from _gspread import readSheet

from ___ import _all_data, _gsheet

for key, val in _all_data.items():
    # # --------------------------------------------------------------------------------------------------------------
    wsheet = readSheet(_gsheet, key)
    getNewData(wsheet, key, val)
    # # --------------------------------------------------------------------------------------------------------------
