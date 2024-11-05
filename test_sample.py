import sys

import pytest


def send_attachment(attachment_size_mb: int | float) -> str | ValueError:
    if int(attachment_size_mb) > 30:
        raise ValueError("Произошла ошибка при отправке. Вложение слишком большое")
    return "Вложение успешно отправлено"


@pytest.mark.parametrize(
    "size, is_sent",
    [
        (20, True),
        (29.9, True),
        (40, False)
    ]
)
def test_send_attachment(size: int | float, is_sent: bool):
    if not is_sent:
        with pytest.raises(ValueError) as exc:
            send_attachment(size)
        assert "ошибка" in str(exc.value)
    else:
        assert "успешно" in str(send_attachment(size))


def print_username(username: str) -> None:
    if type(username) is not str:
        sys.stderr.write("Type mismatch")
        return
    print(f"Welcome, {username}")


def test_output(capsys):
    print_username("Ivan")
    captured = capsys.readouterr()
    assert captured.out == "Welcome, Ivan\n"
    print_username(["Ivan", "Ivan2"])
    captured = capsys.readouterr()
    assert captured.err == "Type mismatch"
