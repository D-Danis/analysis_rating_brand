# Analysis Rating Brand

Скрипт для обработки csv-файла

---

## Описание

Проект реализует чтение файлы с данными  об рейтинга брендов и формирование отчетов,
возможность получение топа и точности отчета

---

## Стек технологий

- Python 3.12
- Pytest
- pytest-cov
- tabulate
- argparse

---

## Структура проекта

```
analysis_rating_brand/
├─ app/                            # Каталог приложение
│  ├─ __init__.py
│  ├─ reports/                     # Каталог для генерации отчетов
│  │  ├─ price/                    # Каталог для генерации отчетов цены
│  │  │  ├─ __init__.py
│  │  │  ├─ average_price.py       # Генерации отчетов средней цены
│  │  │  ├─ max_price.py           # Генерации отчетов максимальной цены
│  │  │  ├─ mediana_price.py       # Генерации отчетов медианной цены
│  │  │  └─ min_price.py           # Генерации отчетов минемальной цены
│  │  ├─ rating/                   # Каталог для генерации отчетов рейтинга
│  │  │  ├─  __init__.py
│  │  │  ├─ average_rating.py       # Генерации отчетов среднего рейтинга
│  │  │  ├─ max_ratinge.py          # Генерации отчетов максимального рейтинга
│  │  │  ├─ mediana_rating.py       # Генерации отчетов медианного рейтинга
│  │  │  └─ min_rating.py           # Генерации отчетов минемального рейтинга
│  │  ├─ __init__.py
│  │  ├─ base.py                    # Базовый класс для генерации отчетов
│  │  └─ registry.py                # Класс для регистрации отчетов
│  ├─ cli.py                        # Основной код обработки
│  ├─ datastatict.py                # Классы для вычисления статистик данных
│  ├─ datastore.py                  # Классы для хранение данных
│  ├─ errors.py                     # Классы для ошибок
│  └─ reader.py                     # Классы для чтение файлов
├─ tests/                           # Каталог с тестами
│  ├─ conftest.py                   # Каталог с тестами
│  ├─ test_cli.py                   # Тест код обработки
│  ├─ test_csv_reader.py            # Тест чтение файлов
│  ├─ test_datastatict.py           # Тест вычисления статистик данных
│  ├─ test_datastore.py             # Тест хранение данных
│  └─ test_reports.py               # Тест генерации отчетов
├── .gitignore                      # gitignore
├── requirements.txt                # Зависимости проекта
├── products1.csv                   # файл для проверки 1
├── products2.csv                   # файл для проверки 2
├── README.md                       # Этот файл
└─ main.py                          # Точка входа
```

---

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/D-Danis/analysis_rating_brand.git
```

### 2. Создайте виртуальное окружение (рекомендуется)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

---

## Пример работы операции

- вывода среднего рейтинга брендов

```sh
python3 main.py --files products1.csv products2.csv --report average-rating
```

- вывода максимального рейтинга брендов, с топ 1

```sh
python3 main.py --files products1.csv products2.csv --report max-rating --top 1
```

- вывода мидиану рейтинга брендов, с топ 1

```sh
python3 main.py --files products1.csv products2.csv --report mit-rating --top 1
```

- вывода минимального рейтинга брендов, с топ 2

```sh
python3 main.py --files products1.csv products2.csv --report mit-rating --top 2
```

---

## Запуск тестов

Для запуска всех тестов используйте команду:

```bash
pytest --maxfail=1 --disable-warnings -v
```

```sh
pytest --maxfail=1 --disable-warnings -v
============================= test session starts ==============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0 -- 
*/analysis_rating_brand/.venv/bin/python3
cachedir: .pytest_cache
rootdir: */work_test/analysis_rating_brand
plugins: cov-6.2.1
collected 70 items                                                             

tests/test_cli.py::test_parse_args_basic[path0-average-rating-exeption0] PASSED [  1%]
tests/test_cli.py::test_parse_args_basic[path1-max-rating-exeption1] PASSED [  2%]
tests/test_cli.py::test_parse_args_basic[path2-min-rating-exeption2] PASSED [  4%]
tests/test_cli.py::test_parse_args_basic[path3-median-rating-exeption3] PASSED [  5%]
tests/test_cli.py::test_parse_args_basic[path4--exeption4] PASSED        [  7%]
tests/test_cli.py::test_run_unexpected_exception[path0-average-rating] PASSED [  8%]
tests/test_cli.py::test_run_unexpected_exception[path1-max-rating] PASSED [ 10%]
tests/test_cli.py::test_run_unexpected_exception[path2-min-rating] PASSED [ 11%]
tests/test_cli.py::test_run_unexpected_exception[path3-median-rating] PASSED [ 12%]
tests/test_cli.py::test_run_app_error PASSED                             [ 14%]
tests/test_csv_reader.py::test_read_single_files[headers0-expectation0] PASSED [ 15%]
tests/test_csv_reader.py::test_read_single_files[headers1-expectation1] PASSED [ 17%]
tests/test_csv_reader.py::test_read_single_files[headers2-expectation2] PASSED [ 18%]
tests/test_csv_reader.py::test_read_single_files[headers3-expectation3] PASSED [ 20%]
tests/test_csv_reader.py::test_read_single_files[headers4-expectation4] PASSED [ 21%]
tests/test_csv_reader.py::test_read_single_len_option[headers0-1] PASSED [ 22%]
tests/test_csv_reader.py::test_read_single_len_option[headers1-2] PASSED [ 24%]
tests/test_csv_reader.py::test_read_single_len_option[headers2-3] PASSED [ 25%]
tests/test_csv_reader.py::test_read_multiple_files_and_rows[header10-header20-expected_brand0] PASSED [ 27%]
tests/test_csv_reader.py::test_read_multiple_files_and_rows[header11-header21-expected_brand1] PASSED [ 28%]
tests/test_csv_reader.py::test_read_multiple_files_and_rows[header12-header22-expected_brand2] PASSED [ 30%]
tests/test_csv_reader.py::test_file_notfound_raises_FileReadError[nonexistentfile12345.csv-expectatio0] PASSED [ 31%]
tests/test_csv_reader.py::test_file_notfound_raises_FileReadError[error1-expectatio1] PASSED [ 32%]
tests/test_csv_reader.py::test_missing_header_raises_CSVFormatError PASSED [ 34%]
tests/test_datastatict.py::test_agregate_price[average-expected_price0-expectation0] PASSED [ 35%]
tests/test_datastatict.py::test_agregate_price[maximum-expected_price1-expectation1] PASSED [ 37%]
tests/test_datastatict.py::test_agregate_price[minimum-expected_price2-expectation2] PASSED [ 38%]
tests/test_datastatict.py::test_agregate_price[median-expected_price3-expectation3] PASSED [ 40%]
tests/test_datastatict.py::test_agregate_rating[average-expected_rating0-expectation0] PASSED [ 41%]
tests/test_datastatict.py::test_agregate_rating[maximum-expected_rating1-expectation1] PASSED [ 42%]
tests/test_datastatict.py::test_agregate_rating[minimum-expected_rating2-expectation2] PASSED [ 44%]
tests/test_datastatict.py::test_agregate_rating[median-expected_rating3-expectation3] PASSED [ 45%]
tests/test_datastore.py::test_add_records_param_price[apple-expected_price0-expectation0] PASSED [ 47%]
tests/test_datastore.py::test_add_records_param_price[xiaomi-expected_price1-expectation1] PASSED [ 48%]
tests/test_datastore.py::test_add_records_param_price[samsung-expected_price2-expectation2] PASSED [ 50%]
tests/test_datastore.py::test_add_records_param_rating[apple-expected_rating0-expectation0] PASSED [ 51%]
tests/test_datastore.py::test_add_records_param_rating[xiaomi-expected_rating1-expectation1] PASSED [ 52%]
tests/test_datastore.py::test_add_records_param_rating[samsung-expected_rating2-expectation2] PASSED [ 54%]
tests/test_datastore.py::test_add_record[records0-expectation0] PASSED   [ 55%]
tests/test_datastore.py::test_add_record[records1-expectation1] PASSED   [ 57%]
tests/test_datastore.py::test_add_record[records2-expectation2] PASSED   [ 58%]
tests/test_datastore.py::test_add_record[records3-expectation3] PASSED   [ 60%]
tests/test_datastore.py::test_add_records_multiple[records0] PASSED      [ 61%]
tests/test_datastore.py::test_add_records_multiple[records1] PASSED      [ 62%]
tests/test_reports.py::test_agregate_rating_reports[AverageRating-expected0-extra0-expectation0] PASSED [ 64%]
tests/test_reports.py::test_agregate_rating_reports[MaxRating-expected1-extra1-expectation1] PASSED [ 65%]
tests/test_reports.py::test_agregate_rating_reports[MinRating-expected2-extra2-expectation2] PASSED [ 67%]
tests/test_reports.py::test_agregate_rating_reports[MedianRating-expected3-extra3-expectation3] PASSED [ 68%]
tests/test_reports.py::test_agregate_render_precision[AverageRating-table0-extra0-expectation0] PASSED [ 70%]
tests/test_reports.py::test_agregate_render_precision[MaxRating-table1-extra1-expectation1] PASSED [ 71%]
tests/test_reports.py::test_agregate_render_precision[MinRating-table2-extra2-expectation2] PASSED [ 72%]
tests/test_reports.py::test_agregate_render_precision[MedianRating-table3-extra3-expectation3] PASSED [ 74%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra0] PASSED  [ 75%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra1] PASSED  [ 77%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra2] PASSED  [ 78%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra3] PASSED  [ 80%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra4] PASSED  [ 81%]
tests/test_reports.py::test_report_factory_kwargs_passed[extra5] PASSED  [ 82%]
tests/test_reports.py::test_report_factory_positive_negative[non-existent-report-expectation0] PASSED [ 84%]
tests/test_reports.py::test_report_factory_positive_negative[average-rating-expectation1] PASSED [ 85%]
tests/test_reports.py::test_report_factory_positive_negative[max-rating-expectation2] PASSED [ 87%]
tests/test_reports.py::test_report_factory_positive_negative[min-rating-expectation3] PASSED [ 88%]
tests/test_reports.py::test_report_factory_positive_negative[median-rating-expectation4] PASSED [ 90%]
tests/test_reports.py::test_report_factory_registered_reports[AverageRating-expectation0] PASSED [ 91%]
tests/test_reports.py::test_report_factory_registered_reports[MaxRating-expectation1] PASSED [ 92%]
tests/test_reports.py::test_report_factory_registered_reports[MinRating-expectation2] PASSED [ 94%]
tests/test_reports.py::test_report_factory_registered_reports[MedianRating-expectation3] PASSED [ 95%]
tests/test_reports.py::test_report_factory_registered_reports[non-existent-report-expectation4] PASSED [ 97%]
tests/test_reports.py::test_create_and_isinstance[<lambda>-True-True] PASSED [ 98%]
tests/test_reports.py::test_create_and_isinstance[<lambda>-True-False] PASSED [100%]

============================== 70 passed in 0.31s ==============================
```

---

## Проверка покрытия тестами

Для измерения покрытия кода используйте плагин `pytest-cov`. 

Запустите тесты с покрытием:

```bash
pytest --cov=tests --cov-report=term-missing:skip-covered
```

Результат
```sh
pytest --cov=tests --cov-report=term-missing:skip-covered
============================= test session starts ==============================
platform linux -- Python 3.12.7, pytest-8.4.1, pluggy-1.6.0
rootdir: */analysis_rating_brand
plugins: cov-6.2.1
collected 70 items                                                             

tests/test_cli.py ..........                                             [ 14%]
tests/test_csv_reader.py ..............                                  [ 34%]
tests/test_datastatict.py ........                                       [ 45%]
tests/test_datastore.py ............                                     [ 62%]
tests/test_reports.py ..........................                         [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.7-final-0 ________________

Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
tests/test_reports.py      83      4    95%   254-256, 258, 260
-----------------------------------------------------
TOTAL                     231      4    98%

6 files skipped due to complete coverage.
============================== 70 passed in 1.09s ==============================



```