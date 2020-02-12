import pytest
@pytest.fixture
def supply_url():
	return "https://reqres.in/api"

@pytest.fixture
def supply_url_petstore():
	return "https://petstore.swagger.io/v2/pet/findByStatus/"

@pytest.fixture
def supply_parametria():
	aa= 10
	bb= 20
	cc= 30
	return [aa,bb,cc]