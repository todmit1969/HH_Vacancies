import json
from typing import Dict, List

from config import JSON_PATH
from src.base_file_manager import BaseFileManager
from src.vacancy import Vacancy


class SaveToJSON(BaseFileManager):
    def __init__(self, file_path: str = "vacancies.json") -> None:
        self.__file_path = file_path
        if not self.__file_path.exists():
            self._save_data([])  # Создаём пустой JSON, если файла нет

    def _load_data(self) -> List[Dict]:
        """Приватный метод для загрузки данных из JSON-файла."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def _save_data(self, data: List[Dict]) -> None:
        """Приватный метод для сохранения данных в JSON-файл."""
        try:
            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancy(self, vacancies: List[Vacancy]) -> None:
        """Добавляет список вакансий в JSON - файл, избегая дублирования."""
        data = self._load_data()
        for vacancy in vacancies:
            vacancy_dict = vacancy.to_dict()
            if vacancy.salary_to < 0 or vacancy.salary_from < 0:
                raise (ValueError)
            else:
                if vacancy_dict not in data:
                    data.append(vacancy_dict)

        self._save_data(data)

    def get_vacancies(self, criteria: Dict) -> List[Dict]:
        """Возвращает список вакансий,
        которые соответствуют заданным критериям."""
        data = self._load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_vacancy(self, criteria: Dict) -> None:
        """Удаляет вакансии, соответствующие
        заданным критериям, из JSON-файла."""
        data = self._load_data()
        data = [
            item
            for item in data
            if not all(item.get(key) == value for key, value in criteria.items())
        ]
        self._save_data(data)
