import pytest
import sqrt


@pytest.fixture(params=[-2, 5, 3])
def testcase(request) -> int:
    return request.param


def test_sqrt(testcase: int) -> None:
    assert sqrt.sqrt(testcase) == testcase ** 0.3
