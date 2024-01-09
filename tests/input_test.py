from pytest import MonkeyPatch
from utils.Input import Input


def test_when_given_value_is_empty_uses_default_value_instead(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: '')

    value = Input.get(
        name='test',
        inputMsg='type value: ',
        default='default value',
    )

    assert value == 'default value'


def test_confirm_method(monkeypatch: MonkeyPatch):
    inputs = ['y', 'Y', 'n', 'sdfsd']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    assert Input.confirm('Create? ') is True
    assert Input.confirm('Create? ') is True
    assert Input.confirm('Create? ') is False
    assert Input.confirm('Create? ') is False
