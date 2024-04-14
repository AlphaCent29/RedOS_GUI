import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QSlider, QHBoxLayout, QSpinBox
from PyQt5 import QtGui
from PyQt5 import QtCore


class ToggleButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(60, 30)  # Уменьшаем ширину кнопок
        self.setStyleSheet("""
            QPushButton {
                width: 60px;
                height: 30px;
                background-color: #888;
                color: #fff;
                border: none;
                border-radius: 15px;
                text-align: center;  /* Выравниваем текст по центру */
            }
            QPushButton:checked {
                background-color: #FFA500;
            }
        """)
        self.setCheckable(True)
        self.setChecked(False)
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        if self.isChecked():
            print(f"Button '{self.text()}' is ON")
        else:
            print(f"Button '{self.text()}' is OFF")


class Window3(QMainWindow):
    def __init__(self, window_title):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("""
            background-color: #222;
            color: #fff;
            border: 2px solid #555;
            border-radius: 10px;
        """)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(5)  # Уменьшаем отступы между элементами

        # Создаем горизонтальные макеты для каждой кнопки с описанием
        buttons_layout = QHBoxLayout()
        label1 = QLabel("Уведомления", self)
        label1.setAlignment(QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        buttons_layout.addWidget(label1)
        self.toggle_button1 = ToggleButton("", self)
        buttons_layout.addWidget(self.toggle_button1)

        label2 = QLabel("Отображение кнопки блокировки экрана", self)
        label2.setAlignment(QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        buttons_layout.addWidget(label2)
        self.toggle_button2 = ToggleButton("", self)
        buttons_layout.addWidget(self.toggle_button2)

        layout.addLayout(buttons_layout)

        # Добавляем слайдеры
        sliders_layout = QVBoxLayout()

        # Слайдер 1
        slider_layout1 = QHBoxLayout()
        slider_label1 = QLabel("Хранитель экрана", self)  # Добавляем подпись к слайдеру
        slider_label1.setFixedWidth(150)  # Устанавливаем фиксированную ширину для подписи
        slider_label1.setAlignment(QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        slider_layout1.addWidget(slider_label1)
        slider1 = QSlider(QtCore.Qt.Horizontal, self)
        slider1.setMinimum(0)
        slider1.setMaximum(60)  # Устанавливаем максимальное значение слайдера
        slider1.setTickInterval(10)
        slider1.setTickPosition(QSlider.TicksBelow)
        self.slider_label1 = QSpinBox(self)  # Заменяем QLabel на QSpinBox
        self.slider_label1.setFixedWidth(40)
        self.slider_label1.setReadOnly(True)
        slider1.valueChanged.connect(self.slider_label1.setValue)
        slider_layout1.addWidget(slider1)
        slider_layout1.addWidget(self.slider_label1)
        sliders_layout.addLayout(slider_layout1)

        # Слайдер 2
        slider_layout2 = QHBoxLayout()
        slider_label2 = QLabel("Блокировка экрана", self)  # Добавляем подпись к слайдеру
        slider_label2.setFixedWidth(150)  # Устанавливаем фиксированную ширину для подписи
        slider_label2.setAlignment(QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        slider_layout2.addWidget(slider_label2)
        slider2 = QSlider(QtCore.Qt.Horizontal, self)
        slider2.setMinimum(0)
        slider2.setMaximum(60)  # Устанавливаем максимальное значение слайдера
        slider2.setTickInterval(10)
        slider2.setTickPosition(QSlider.TicksBelow)
        self.slider_label2 = QSpinBox(self)  # Заменяем QLabel на QSpinBox
        self.slider_label2.setFixedWidth(40)
        self.slider_label2.setReadOnly(True)
        slider2.valueChanged.connect(self.slider_label2.setValue)
        slider_layout2.addWidget(slider2)
        slider_layout2.addWidget(self.slider_label2)
        sliders_layout.addLayout(slider_layout2)

        # Слайдер 3
        slider_layout3 = QHBoxLayout()
        slider_label3 = QLabel("Скрытие панели", self)  # Добавляем подпись к слайдеру
        slider_label3.setFixedWidth(150)  # Устанавливаем фиксированную ширину для подписи
        slider_label3.setAlignment(QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        slider_layout3.addWidget(slider_label3)
        slider3 = QSlider(QtCore.Qt.Horizontal, self)
        slider3.setMinimum(0)
        slider3.setMaximum(60)  # Устанавливаем максимальное значение слайдера
        slider3.setTickInterval(10)
        slider3.setTickPosition(QSlider.TicksBelow)
        self.slider_label3 = QSpinBox(self)  # Заменяем QLabel на QSpinBox
        self.slider_label3.setFixedWidth(40)
        self.slider_label3.setReadOnly(True)
        slider3.valueChanged.connect(self.slider_label3.setValue)
        slider_layout3.addWidget(slider3)
        slider_layout3.addWidget(self.slider_label3)
        sliders_layout.addLayout(slider_layout3)

        layout.addLayout(sliders_layout)

        # Добавляем виджет с цветом заднего фона внизу
        bottom_widget = QWidget()
        bottom_widget.setStyleSheet("background-color: #222;")  # Задаем цвет фона
        layout.addWidget(bottom_widget)

        # Применяем макет к виджету
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = Window3("Настройки пользователя")
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
