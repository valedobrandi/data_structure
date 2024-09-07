import pytest
from class_queue import Stack


@pytest.fixture
def stack():
    return Stack()


def test_push(stack):
    stack.push(10)
    assert stack.peek() == 10


def test_pop(stack):
    stack.push(20)
    stack.pop()
    assert stack.is_empty()


def test_peek(stack):
    stack.push(30)
    stack.push(40)
    assert stack.peek() == 40


def test_min_value(stack):
    stack.push(50)
    stack.push(10)
    stack.push(30)
    assert stack.min_value() == 10


def test_limit_stack(stack):
    stack.limit_stack(2)
    stack.push(60)
    stack.push(70)
    with pytest.raises(OverflowError):
        stack.push(80)


def test_is_empty(stack):
    assert stack.is_empty()
    stack.push(90)
    assert not stack.is_empty()
