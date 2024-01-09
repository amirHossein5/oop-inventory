from bootstrap import bootstrap


def main():
    bootstrap()

    action('main_page', False)


def action(name: str, printBefore: bool = True, params: dict = {}) -> None:
    from actions import actions

    method = actions.get(name)

    if not method:
        raise ValueError('Method not found in actions')
    if not callable(method):
        raise ValueError(f'{method} is not callable from actions')

    if printBefore:
        print()

    if len(params) == 0:
        return actions.get(name)()
    return actions.get(name)(params)


if __name__ == "__main__":
    main()
