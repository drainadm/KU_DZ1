import sys
import unittest
from PyQt5.QtWidgets import QApplication, QWidget

# Предполагаемый виджет, который вы тестируете
class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Widget")
        self.some_value = 10

    def increment_value(self):
        self.some_value += 1

    def reset_value(self):
        self.some_value = 0

    def get_value(self):
        return self.some_value

# Тестовый класс
class TestYourWidget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Убедитесь, что QApplication не создается ранее
        cls.app = QApplication.instance()
        if cls.app is None:
            cls.app = QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        if QApplication.instance():
            QApplication.instance().quit()

    def test_widget_creation(self):
        widget = YourWidget()
        self.assertIsNotNone(widget)
        self.assertEqual(widget.windowTitle(), "Test Widget")

    def test_widget_show(self):
        widget = YourWidget()
        widget.show()
        self.assertTrue(widget.isVisible())

    def test_default_value(self):
        widget = YourWidget()
        self.assertEqual(widget.get_value(), 10)

    def test_increment_value(self):
        widget = YourWidget()
        widget.increment_value()
        self.assertEqual(widget.get_value(), 11)

    def test_reset_value(self):
        widget = YourWidget()
        widget.increment_value()
        widget.reset_value()
        self.assertEqual(widget.get_value(), 0)

# Запуск тестов, если скрипт запускается напрямую
if __name__ == '__main__':
    unittest.main()