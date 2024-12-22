import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url='https://dummyjson.com'
    )
    yield api_context
    api_context.dispose()


def test_user_data(api_context: APIRequestContext):
    response = api_context.get('users/3')

    user_data = response.json()

    assert user_data['firstName'] == 'Sophia'
    assert user_data['lastName'] == 'Brown'
    assert user_data['age'] == 42
    assert user_data['gender'] == 'female'
    assert user_data['address'] == {'address': '1642 Ninth Street', 'city': 'Washington', 'state': 'Alabama',
                                    'stateCode': 'AL', 'postalCode': '32822', 'coordinates':
                                        {'lat': 45.289366, 'lng': 46.832664}, 'country': 'United States'}


def test_user_search(api_context: APIRequestContext):
    query = 'Sophia'
    response = api_context.get(f'/users/search?q={query}')

    selected_users = response.json()

    for user in selected_users['users']:
        assert query in user['firstName']


def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        'users/add',
        headers={'Content-Type': 'application/json'},
        data={
            'firstName': 'Ilona',
            'lastName': 'Green',
            'age': 21
        }
    )
    user_data = response.json()

    assert user_data['firstName'] == 'Ilona'
    assert user_data['lastName'] == 'Green'
    assert user_data['age'] == 21


def test_update_user(api_context: APIRequestContext):
    response = api_context.put(
        'users/1',

        data={
            'firstName': 'Emma',
            'lastName': 'Gamer',
            'age': 25
        }
    )
    user_data = response.json()

    assert user_data['firstName'] == 'Emma'
    assert user_data['lastName'] == 'Gamer'
    assert user_data['age'] == 25


def test_delete_user(api_context: APIRequestContext):
    response = api_context.delete('users/1')

    result = response.json()

    assert result['isDeleted'] is True
