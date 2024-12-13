#### How to structure tests  hints by Nick del Grosso

from argparse import ArgumentParser
from unittest.mock import patch

from pytest import mark


def main(x):
    return x + 3

def cli(args = None):
    parser = ArgumentParser(args=args)
    parser.add_argument('x')
    args = parser.parse_args()
    result = main(x=args.x)
    print(result)



#############

# e2e tests
@mark.slow
def test_cli_e2e(capsys):
    import subprocess
    subprocess.run('python cli.py 4')
    assert capsys.stdout == '6'


# integration tests
def test_cli(capsys):
    with patch('__main__.main') as mock_main:
        cli(args=['3'])
        mock_main.assert_called_with(x=3)



# unit tests
def test_main():
    result = main(3)
    assert result == 6

def __name__ == '__main__':
    cli()