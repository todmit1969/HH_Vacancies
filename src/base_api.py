from abc import ABC, abstractmethod


class BasePlatform_API(ABC):
    """
    Абстрактный класс для работы с API платформы для поиска вакансий
    """

    @abstractmethod
    def connect(self, keyword: str) -> None:
        """
        Подключается к платформе поиска вакансий
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """
        Возвращает список словарей вакансий при помощи API
        """
        pass
