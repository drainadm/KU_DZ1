import sys
import tarfile
import os
import toml
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton


class ShellEmulatorGUI(QWidget):
    def __init__(self, config_path):
        super(ShellEmulatorGUI, self).__init__()

        self.config_path = config_path
        self.hostname = "localhost"
        self.current_path = "/"
        self.fs = []

        # Загружаем конфигурацию
        self.load_config()

        # Инициализируем UI
        self.initUI()

    def load_config(self):
        try:
            config = toml.load(self.config_path)
            self.hostname = config.get('hostname', 'localhost')
            fs_image = config.get('filesystem', '')

            # Открываем tar-архив, если путь задан
            if fs_image:
                self.load_fs_from_tar(fs_image)
            else:
                print("Error: No filesystem image path provided in config.")
                sys.exit(1)
        except Exception as e:
            print(f"Error loading config: {e}")
            sys.exit(1)

    def load_fs_from_tar(self, fs_image):
        try:
            with tarfile.open(fs_image, 'r') as tar:
                self.fs = tar.getmembers()
        except Exception as e:
            print(f"Error loading filesystem from tar: {e}")
            sys.exit(1)

    def initUI(self):
        self.setWindowTitle('Shell Emulator')

        # Создание главного макета
        layout = QVBoxLayout()

        # Добавление текстовой области для вывода
        self.outputArea = QTextEdit()
        self.outputArea.setReadOnly(True)
        layout.addWidget(self.outputArea)

        # Добавление текстового поля для ввода
        self.inputField = QLineEdit()
        layout.addWidget(self.inputField)

        # Добавление кнопки для отправки команды
        enterButton = QPushButton('Enter')
        enterButton.clicked.connect(self.onEnter)
        layout.addWidget(enterButton)

        self.setLayout(layout)

    def onEnter(self):
        command = self.inputField.text()
        self.execute_command(command)
        self.inputField.clear()

    def execute_command(self, command):
        output = ''
        if command == "exit":
            self.close()
        elif command.startswith("ls"):
            output = self.list_files(self.current_path)
        elif command.startswith("cd"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                _, path = parts
                self.change_directory(path)
                output = f'Changed to {self.current_path}'
            else:
                output = "No path provided for cd command"
        elif command.startswith("find"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                _, name = parts
                output = self.find_in_filesystem(name)
            else:
                output = "No search term provided for find command"
        elif command == "uptime":
            output = self.get_uptime()
        elif command == "whoami":
            output = "user"
        else:
            output = "command not found"

        self.outputArea.append(f"{self.hostname}:{self.current_path}$ {command}\n{output}")

    def list_files(self, path):
        entries = [m.name[len(path):].split('/')[0] for m in self.fs if m.name.startswith(path)]
        entries = set(entries)
        return '\n'.join(entries)

    def change_directory(self, path):
        if path == "/":
            self.current_path = "/"
        else:
            new_path = os.path.join(self.current_path, path)
            possible_dirs = [m for m in self.fs if m.isdir() and m.name.startswith(new_path)]
            if possible_dirs:
                self.current_path = new_path

    def find_in_filesystem(self, name):
        results = [file.name for file in self.fs if name in file.name]
        return '\n'.join(results)

    def get_uptime(self):
        return "Uptime: 1 hour"


def main(config_path):
    app = QApplication(sys.argv)
    window = ShellEmulatorGUI(config_path)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python emulator_gui.py <config_path>")
        sys.exit(1)
    config_path = sys.argv[1]
    main(config_path)