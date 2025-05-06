from abc import ABC, abstractmethod
from typing import Dict

from src.vacancy import Vacancy


class BaseFileManager(ABC):
    """
    Базовый класс, определяющий методы
    добавления и удаления вакансий из файла
    """

    @abstractmethod
    def add_vacancy(self: object, vacancies: Vacancy) -> None:
        """Метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict):
        """Метод извлечения вакансий из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self: object, vacancies: Vacancy) -> None:
        """Метод для удаления вакансий из файла"""
        pass
