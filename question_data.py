from _openai import getNewData, getQuestionResults
from _gspread import readSheet

from ___ import _questions, _all_data, _gsheet


for key, val in _all_data.items():
    # # --------------------------------------------------------------------------------------------------------------
    wsheet = readSheet(_gsheet, key)
    # getQuestionResults(wsheet, _questions, start_at=1, end_at=2, overwrite=True)
    getQuestionResults(wsheet, _questions)
    # # --------------------------------------------------------------------------------------------------------------
