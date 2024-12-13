'''
Nicholas Del Grosso

Hi Panos,

Some extra explaining here (please forgive the long message):

Attached is an updated version of the file, showing a better case of how to write the integration test (note that no "capsys" nor patching is needed in the integration test, making the test very easy to write and run, as it only deals with Python objects and no other systems.  

"Don't patch your own code" is a good rule of thumb for helping write testable code; if we can make our code easier to test through mocks via dependency injection, then why not?   This approach also leads to the architectural practice of the Single Responsibility Principle in SOLID coding, with functions that have to do integration of systems (the cli() function in this example) being written to *only* do integration--nothing  else.  

This has the final result of reducing the number of integration tests that are needed; a test of a mocked-out integration function is just a unit test.  This is a very good thing; integration tests imply coupled units, and coupled units are hard to maintain and extend, and can have non-obvious behaviors (that should be extra-tested as a result).  

Anyway, hope that this demo was interesting!

Best wishes,

Nick
'''

from argparse import ArgumentParser
from unittest.mock import Mock, patch

from pytest import mark


def main(x):
    return x + 3

def cli(args = None, mainfun=main, printer=print):
    parser = ArgumentParser(args=args)
    parser.add_argument('x')
    args = parser.parse_args()
    result = main(x=args.x)
    printer(result)



#############

# e2e tests
@mark.slow
def test_cli_e2e(capsys):
    import subprocess
    subprocess.run('python cli.py 4')
    assert capsys.stdout == '6'


# integration tests no longer needed, because

# unit test of an integration function (tests that integration happens correctly)
def test_cli():
    mock_main = Mock()
    mock_main.return_value(6)
    mock_print = Mock()
    cli(args=['3'], mainfun=mock_main, printer=mock_print)
    mock_main.assert_called_with(x=3)
    mock_print.assert_called_once_with(6)



# unit test
def test_main():
    result = main(3)
    assert result == 6

def __name__ == '__main__':
    cli()