# Проект: Эмулятор языка оболочки ОС с использованием PyQt

Этот проект направлен на разработку эмулятора для языка оболочки операционной системы, предназначенного для максимально точного воспроизведения сеанса shell в UNIX-подобной операционной системе. Эмулятор запускается из реальной командной строки и функционирует в режиме графического интерфейса (GUI) с использованием PyQt.

## Основные возможности

- **Эмуляция shell**: Поведение эмулятора максимально приближено к сеансам shell в UNIX-подобных системах, предоставляя пользователям привычные команды и окружение.
  
- **Запуск из командной строки**: Эмулятор запускается непосредственно из командной строки операционной системы, обеспечивая удобство интеграции и запуска.

- **Поддержка виртуальных файловых систем**: Эмулятор принимает образ виртуальной файловой системы в виде архива файла формата `.tar`, который используется без распаковки пользователем. Это позволяет симулировать файловую структуру и операции без необходимости в физической установке или изменении файловой системы.

- **Графический интерфейс пользователя**: Для обеспечения более удобного и наглядного управления эмулятором используется GUI на базе PyQt, который предоставляет графический интерфейс для взаимодействия.

## Установка

Перед началом работы убедитесь, что у вас установлены следующие зависимости:

- Python 3.x
- PyQt5

Для установки PyQt5 выполните следующую команду:
```bash
pip install PyQt5
```
## Используйте виртуальную среду для управления зависимостями:
```
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.\.venv\Scripts\activate  # Для Windows
```
## Структура проекта:

```ku1/
├── .venv/                    # Виртуальная среда
├── config.toml               # Конфигурационный файл
├── filesystem.tar            # Пример архива
├── main.py                   # Основной файл приложения
├── README.md                 # Документация проекта
└── test.py                   # Файл с тестами```
```
## Запуск приложения
На данный момент основной код приложения располагается в main.py. Чтобы запустить виджет, откройте этот файл и выполните:
```python test.py```

## Тестирование
В проекте используются тесты, написанные на базе unittest. Чтобы запустить тесты, выполните следующую команду:
```python test.py```
