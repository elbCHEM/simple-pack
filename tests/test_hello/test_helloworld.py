"""The the mandetory hello function using monkeypatching"""
from simple.hello import hello


def test_hello(monkeypatch) -> None:
    # Replace '__builtins__.print' with a mock version such that
    # I can check what is printed to stdout.
    last_output = None
    def myprint(string: str) -> None:
        nonlocal last_output
        last_output = string
    monkeypatch.setattr('builtins.print', myprint)

    # Perform function call of hello, which uses print function
    hello()

    # # Check if print matches expected
    if not last_output:
        raise ValueError('Nothing was outputted')
    assert last_output == "Hello, World!"
