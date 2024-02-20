# pylint: disable=unnecessary-dunder-call, invalid-name, line-too-long
from decimal import Decimal
import pytest
from faker import Faker
# from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")

@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")