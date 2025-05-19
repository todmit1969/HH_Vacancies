import json
import pytest

from src.vacancy import Vacancy
from src.file_manager import SaveToJSON
import os


def test_add_vacancy(test_json_file, vacancy_Python_developer, vacancy_system_administrator):
    """Тестирование метода add_vacancy класса SaveToJSON."""
    os.remove(test_json_file)
    storage = SaveToJSON(test_json_file)
    storage.add_vacancy([vacancy_Python_developer, vacancy_system_administrator])

    with open(test_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == vacancy_Python_developer.name
    assert data[1]["name"] == vacancy_system_administrator.name


def test_get_vacancies(test_json_file, vacancy_Python_developer, vacancy_system_administrator):
    """Тестирование метода get_vacancies класса SaveToJSON."""
    storage = SaveToJSON(test_json_file)
    storage.add_vacancy([vacancy_Python_developer, vacancy_system_administrator])

    result = storage.get_vacancies({"name": "Python_developer"})
    assert len(result) == 1
    assert result[0]["name"] == "Python_developer"


def test_delete_vacancy(test_json_file, vacancy_Python_developer, vacancy_system_administrator):
    """Тестирование метода delete_vacancy класса SaveToJSON."""
    storage = SaveToJSON(test_json_file)
    storage.add_vacancy([vacancy_Python_developer, vacancy_system_administrator])

    storage.delete_vacancy({"name": "Python_developer"})
    data = storage._load_data()

    assert len(data) == 1
    assert data[0]["name"] == "Системный администратор"


def test_add_invalid_vacancy(test_json_file, vacancy_with_negative_salary):
    """Тестирование валидации при добавлении некорректной вакансии в SaveToJSON."""
    storage = SaveToJSON(test_json_file)
    with pytest.raises(ValueError):
        storage.add_vacancy([Vacancy(**vacancy_with_negative_salary)])
