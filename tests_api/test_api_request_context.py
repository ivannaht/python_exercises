from playwright.sync_api import Playwright


def test_user_data(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url='https://dummyjson.com'
    )
    response = api_context.get('users/3')

    user_data = response.json()

    assert user_data['firstName'] == 'Sophia'
    assert user_data['lastName'] == 'Brown'
    assert user_data['age'] == 42
    assert user_data['gender'] == 'female'
    assert user_data['address'] == {'address': '1642 Ninth Street', 'city': 'Washington', 'state': 'Alabama',
                                    'stateCode': 'AL', 'postalCode': '32822', 'coordinates':
                                        {'lat': 45.289366, 'lng': 46.832664}, 'country': 'United States'}
