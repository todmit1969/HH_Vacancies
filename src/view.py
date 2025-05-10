from typing import NoReturn

from config import JSON_PATH
from src.file_manager import SaveToJSON
from src.user_functions import get_vacancies_by_salary
from src.vacancy import Vacancy
from src.vacancy_platform_api import HH_API

"""Функция для взаимодействия с пользователем через консоль."""


def user_interaction() -> NoReturn:
    platform = HH_API()
    storage = SaveToJSON(JSON_PATH)

    if not platform.connect():
        print("Не удалось подключиться к API hh.ru")
        return

    while True:
        print("\n1. Ввести поисковый запрос")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Найти вакансии по ключевому слову в описании")
        print("4. Найти вакансии по зарплате")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies = platform.get_vacancies(search_query, 10)
            vacancies_list = Vacancy.from_platform(vacancies)
            storage.add_vacancy(vacancies_list)
            print(f"Добавлено {len(vacancies_list)} вакансий.")

        elif choice == "2":
            n = int(input("Сколько вакансий вывести?: "))
            data = storage._load_data()
            vacancies_list = [Vacancy(**vacancy) for vacancy in data]
            #sorted_vacancies = sorted(
            #    vacancies_list,
            #    key=lambda x: (x.salary_from + x.salary_to) / 2,
            #    reverse=True,
            #)
            sorted_vacancies = sorted(
                vacancies_list,
                reverse=True,
            )
            for vacancy in sorted_vacancies[:n]:
                print(vacancy)

        elif choice == "3":
            keyword = input("Введите ключевое слово: ")
            data = storage._load_data()
            filtered = [v for v in data if keyword.lower() in v["description"].lower()]
            for vacancy in filtered:
                print(Vacancy(**vacancy))

        elif choice == "4":
            salary_range = input("Введите диапазон зарплаты: ")
            data = storage._load_data()
            salary_filtered = get_vacancies_by_salary(data, salary_range)
            # print(salary_filtered)
            for vacancy in salary_filtered:
                print(Vacancy(**vacancy))


        elif choice == "5":
            break

        else:
            print("Неверный выбор, попробуйте снова.")
