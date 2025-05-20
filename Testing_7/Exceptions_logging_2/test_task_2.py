import pytest
from io import StringIO
from contextlib import redirect_stdout
from Exceptions_logging_2.task_2 import main, main_2



def test_main_output_and_return():
    f = StringIO()
    with redirect_stdout(f):
        result = main()

    output = f.getvalue().strip().splitlines()

    assert result == 'https://'
    assert output == [
        "Inside except https://",
        "Very important action"
    ]



def test_main2_output_and_return():
    f = StringIO()
    with redirect_stdout(f):
        main_2()

    output = f.getvalue().strip().splitlines()

    assert output == [
        "GOOGLE.RU"
    ]