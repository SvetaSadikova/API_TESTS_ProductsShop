import pytest

from fixture.application import Application


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )


@pytest.fixture
def application(request):
    url = request.config.getoption("--api-url")
    return Application(url)
