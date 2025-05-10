import pytest

from src.vacancy import Vacancy


def test_vacancy_init(vacancy_Python_developer):
    """Тест инициализации экземпляра объекта Vacancy"""
    assert vacancy_Python_developer.name == "Python_developer"
    assert vacancy_Python_developer.url == "https://hh.ru/applicant/vacancy_response?vacancyId=117286365"
    assert vacancy_Python_developer.salary_from == 100000
    assert vacancy_Python_developer.salary_to == 120000
    assert vacancy_Python_developer.description == "Разработка и поддержка, back end части веб-приложений."


def test_str_method(vacancy_Python_developer):
    """Тест на метод __str__."""

    assert (
        str(vacancy_Python_developer)
        == "Вакансия: Python_developer, Зарплата: 100000-120000, URL: https://hh.ru/applicant/vacancy_response?vacancyId=117286365"
    )


def test_vacancy_comparison_lt(vacancy_Python_developer, vacancy_system_administrator):
    """Тест на сравнение вакансий по средней зарплате (меньше)."""

    assert vacancy_Python_developer > vacancy_system_administrator


def test_vacancy_comparison_gt(vacancy_system_administrator, vacancy_Python_developer):
    """Тест на сравнение вакансий по средней зарплате (больше)."""

    assert vacancy_system_administrator < vacancy_Python_developer


def test_from_platform(platform_data):
    """Тест на метод from_platform."""
    vacancies = Vacancy.from_platform(platform_data)

    assert len(vacancies) == 2

    for vacancy in vacancies:
        assert isinstance(vacancy, Vacancy)

    assert vacancies[0].name == "Программист"
    assert vacancies[0].url == "https://example.com/job1"
    assert vacancies[0].salary_from == 80000
    assert vacancies[0].salary_to == 150000
    assert vacancies[0].description == "Отдел разработки"

    assert vacancies[1].name == "Тестировщик"
    assert vacancies[1].url == "https://example.com/job2"
    assert vacancies[1].salary_from == 60000
    assert vacancies[1].salary_to == 100000
    assert vacancies[1].description == "Отдел тестирования"


def test_vacancy_str_method(capsys, vacancy_Python_developer):
    """Тест метода __str__ класса Vacancy с использованием capsys."""
    print(vacancy_Python_developer)
    captured = capsys.readouterr()
    expected_output = "Вакансия: Python_developer, Зарплата: 100000-120000, URL: https://hh.ru/applicant/vacancy_response?vacancyId=117286365\n"
    assert captured.out == expected_output


def test_vacancy_comparison_lt(vacancy_Python_developer, vacancy_system_administrator):
    """Тест оператора < (__lt__) для сравнения вакансий по средней зарплате."""
    assert vacancy_system_administrator < vacancy_Python_developer
    assert not vacancy_Python_developer < vacancy_system_administrator
