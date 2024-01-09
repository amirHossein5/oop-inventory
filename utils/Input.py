from utils.Rules import Rules


class Input:
    @staticmethod
    def get(
        name: str,
        inputMsg: str,
        rules: list[Rules] = [Rules.required],
        default: str = None,
    ) -> any:
        if default:
            default = str(default)

        return Input.__raiseInput(
            name=name,
            inputMsg=inputMsg,
            rules=rules,
            default=default
        )

    @staticmethod
    def confirm(inputMsg: str) -> bool:
        return Input.__raiseInput(
            name='confirmation',
            inputMsg=inputMsg,
            rules=[Rules.required]
        ).lower() == 'y'

    @staticmethod
    def __raiseInput(
        name: str,
        inputMsg: str,
        rules: list[Rules],
        invalidMsg: str = '',
        wasInvalid: bool = False,
        default: any = None
    ) -> any:
        if wasInvalid:
            print(invalidMsg)

        value = input(inputMsg)

        if default and value == '':
            value = value or default

        for rule in rules:
            validation = rule(fieldName=name, value=value)

            if validation.hasErrors:
                return Input.__raiseInput(
                    name=name,
                    inputMsg=inputMsg,
                    rules=rules,
                    invalidMsg=validation.errorMsg,
                    wasInvalid=True,
                    default=default,
                )

            value = validation.castedValue

        return value
