import pytest
from tasks_oop.person import Person


@pytest.mark.parametrize('arguments, expected_result',
                         [(('David', 'Brown', '10.10.1991', 'USA', 'Chicago', '011-444-3333',
                            'Project Manager', '4.25', '2000.0', 'Male'),
                           'Full name: David Brown, Age: 33, Gender: Male'
                           )])
def test_show_personal_info(arguments, expected_result):
    """
    verify show_personal_info function
    """
    first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender = arguments
    person = Person(first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender)

    assert person.show_personal_info() == expected_result


@pytest.mark.parametrize('arguments, expected_result',
                         [(('Kate', 'Holms', '10.10.1993', 'USA', 'Chicago', '011-444-3333',
                            'Python Developer', '4.25', '2000.0', 'Female'),
                           'Job title: Python Developer, Experience: 4.25, Salary: 2000.0 USD'
                           )])
def test_show_job_profile(arguments, expected_result):
    """
    verify show_job_profile function
    """
    first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender = arguments
    person = Person(first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender)

    assert person.show_job_profile() == expected_result


@pytest.mark.parametrize('arguments, expected_result',
                         [(('Laura', 'Holms', '10.10.1993', 'USA', 'Chicago',
                            '011-4567-5633', 'JavaScript Developer', '1.25', '2000.0'),
                           'Country: USA, City: Chicago, Phone: 011-4567-5633'
                           )])
def test_show_contacts(arguments, expected_result):
    """
    verify show_contacts function
    """
    first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender = arguments
    person = Person(first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender)

    assert person.show_contacts() == expected_result


@pytest.mark.parametrize('period, arguments,  expected_result',
                         [(12, ('Ben', 'Dilan', '10.10.1995', 'USA', 'Phoenix',
                                '011-4567-5633', 'JavaScript Developer', '4.25', '2000.0'),
                           'Income for 12 months: 31800.0'
                           )])
def test_show_income(period, arguments, expected_result):
    """
    verify show_income function
    """
    first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender = arguments
    person = Person(first_name, last_name, dob, country, city, phone, job_title, experience, salary, *gender)

    assert person.show_income(period) == expected_result


def test_persons_count():
    """
    verify persons_count
    """

    assert Person.count == 4
