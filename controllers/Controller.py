from utils.Action import Action
from main import action


class Controller:
    @staticmethod
    def nextActions(actions: list[Action]) -> None:
        return Controller.__nextActions(actions)

    @staticmethod
    def __nextActions(actions: list[Action], wrongInput: bool = False) -> None:
        print()
        if (wrongInput):
            print('wrong input(type the letter that is inside of [])')
            print()

        for a in actions:
            print(a.input)

        letter = input(': ')

        filteredActions = [a for a in actions if a.key == letter]

        if len(filteredActions) != 0:
            return action(filteredActions[0].action, params=filteredActions[0].params)

        Controller.__nextActions(actions, wrongInput=True)
