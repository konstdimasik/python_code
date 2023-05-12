# substring searching algorithm
import pytest


def contains_wrong(text, pattern):
    for i in range(len(text) - len(pattern)):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False


def contains(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False


@pytest.mark.parametrize(('text', 'sub'), [
    ('1001011', '011'),
    ('0111011', '011'),
    ('0110110', '111'),
    ('00100111', '111'),
])
def test_contains(text: str, sub: str) -> None:
    assert contains(text, sub) == contains_wrong(text, sub)
