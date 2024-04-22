import json
from pathlib import Path

PATH_TEAM_DATA = Path(__file__). parent / 'team_data.json'
PATH_FILLED_TEAM = Path(__file__).parent / 'filled_team.json'


class Teams:

    def __init__(self, team=None, mascot=None, state=None) -> None:
        self.team = team
        self.mascot = mascot
        self.state = state


with open(PATH_TEAM_DATA, "r", encoding='utf8') as file:
    _team_data = json.load(file)


_filled_team = {}
for i, data in enumerate(_team_data):
    # Criando o nome da variável dinamicamente
    variable_name = f"team_{i+1}"
    _instance = Teams(**data)
    globals()[variable_name] = _instance
    _filled_team[variable_name] = _instance.__dict__

with open(PATH_FILLED_TEAM, 'w', encoding='utf8') as tp:
    json.dump(_filled_team, tp, ensure_ascii=False, indent=2)
