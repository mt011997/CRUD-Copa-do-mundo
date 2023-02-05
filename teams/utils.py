from datetime import datetime


class NegativeTitlesError(Exception):
    def __init__(self, message) -> None:
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message) -> None:
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message) -> None:
        self.message = message


def data_processing(**dicionario):
    now = datetime.now()
    current_year = int(now.strftime("%Y"))
    titles = dicionario.get('titles')

    if titles < 0:
        return NegativeTitlesError("titles cannot be negative")

    cup_years = []
    for i in range(1930, current_year + 1, 4):
        cup_years.append(i)

    year_dic = datetime.strptime(dicionario.get('first_cup'), "%Y-%m-%d")
    year = int(year_dic.strftime("%Y"))

    if year not in cup_years:
        return InvalidYearCupError("there was no world cup this year")

    possible_participates = []
    for i in range(year, current_year, 4):
        possible_participates.append(i)

    if titles > len(possible_participates):
        return ImpossibleTitlesError("impossible to have more titles than disputed cups")

    pass
