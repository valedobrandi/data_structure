import pytest


@pytest.fixture(
    scope="module"
)  # Criamos a fixture por meio do decorador pytest.fixture
def my_list():  # Por padrão, o nome da fixture será o nome da função
    return [1, 2, 3]  # Retorna o valor que a fixture possuirá


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow")
