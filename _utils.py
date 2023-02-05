def _text2Arr(_text: str) -> list:
    arrResult = _text.strip().split("\n")
    arrResult = [i for i in arrResult if i]
    return arrResult


def _incChr(letter: str, inc_num: int) -> str:
    result = chr(ord(letter) + inc_num)
    return result
