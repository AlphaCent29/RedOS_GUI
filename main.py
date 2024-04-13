import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QFrame, QPushButton, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtGui

class User:
    def __init__(self, full_name, position):
        self.full_name = full_name
        self.position = position

class UserInformationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kiosk')
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet("background-color: #222; color: #fff; border: 1px solid black;")

        self.initUI()

    def initUI(self):
        # Создаем topbar
        self.topbar = QFrame(self)
        self.topbar.setGeometry(0, 0, 1600, 50)
        self.topbar.setStyleSheet("background-color: #333;")

        #Иконка
        self.setWindowIcon(QtGui.QIcon("pics/logo.png"))

        # Логотип
        self.logo_label = QLabel(self.topbar)
        self.logo_label.setGeometry(10, 10, 100, 30)
        self.logo_label.setPixmap(QtGui.QPixmap("pics/logo.png"))

        # Кнопки в topbar
        self.button1 = QPushButton("Кнопка 1", self.topbar)
        self.button1.setGeometry(130, 10, 75, 30)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #555;
                color: #fff;
                border: none;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #444; /* Цвет при наведении */
                color: #fff;
            }
            QPushButton:pressed {
                background-color: #FF0000; /* Цвет при нажатии */
            }
        """)
        self.button1.clicked.connect(self.openWindow1)

        self.button2 = QPushButton("Кнопка 2", self.topbar)
        self.button2.setGeometry(220, 10, 75, 30)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #555;
                color: #fff;
                border: none;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #444; /* Цвет при наведении */
                color: #fff;
            }
            QPushButton:pressed {
                background-color: #FF0000; /* Цвет при нажатии */
            }
        """)
        self.button2.clicked.connect(self.openWindow2)


        # Создаем виджеты
        self.menu_tree1 = QTreeWidget(self)
        self.menu_tree1.setHeaderLabels(["Отдел разработки"])
        self.menu_tree1.setStyleSheet(
            """
            QTreeWidget {
                color: #fff;
                background-color: #333;
                border: none;
            }
            QTreeWidget::item {
                height: 40px;
                border: none;
            }
            QTreeWidget::item:selected {
                background-color: #555;
            }
            QTreeWidget::header {
                background-color: #000;
                color: #fff;
            }
            """
        )
        self.menu_tree1.itemClicked.connect(lambda: self.displayUsers(self.menu_tree1))

        self.menu_tree2 = QTreeWidget(self)
        self.menu_tree2.setHeaderLabels(["Отдел тестирования"])
        self.menu_tree2.setStyleSheet(
            """
            QTreeWidget {
                color: #fff;
                background-color: #333;
                border: none;
            }
            QTreeWidget::item {
                height: 40px;
                border: none;
            }
            QTreeWidget::item:selected {
                background-color: #555;
            }
            QTreeWidget::header {
                background-color: #000;
                color: #fff;
            }
            """
        )
        self.menu_tree2.itemClicked.connect(lambda: self.displayUsers(self.menu_tree2))

        self.menu_tree3 = QTreeWidget(self)
        self.menu_tree3.setHeaderLabels(["Отдел системной администрации"])
        self.menu_tree3.setStyleSheet(
            """
            QTreeWidget {
                color: #fff;
                background-color: #333;
                border: none;
            }
            QTreeWidget::item {
                height: 40px;
                border: none;
            }
            QTreeWidget::item:selected {
                background-color: #555;
            }
            QTreeWidget::header {
                background-color: #000;
                color: #fff;
            }
            """
        )
        self.menu_tree3.itemClicked.connect(lambda: self.displayUsers(self.menu_tree3))

        self.menu_tree4 = QTreeWidget(self)
        self.menu_tree4.setHeaderLabels(["Отдел дизайна"])
        self.menu_tree4.setStyleSheet(
            """
            QTreeWidget {
                color: #fff;
                background-color: #333;
                border: none;
            }
            QTreeWidget::item {
                height: 40px;
                border: none;
            }
            QTreeWidget::item:selected {
                background-color: #555;
            }
            QTreeWidget::header {
                background-color: #000;
                color: #fff;
            }
            """
        )
        self.menu_tree4.itemClicked.connect(lambda: self.displayUsers(self.menu_tree4))

        self.user_info_display = QWidget(self)
        self.user_info_layout = QVBoxLayout(self.user_info_display)
        self.user_info_display.setStyleSheet("background-color: #333; color: #fff; border: 1px solid #555; border-radius: 5px;")

        # Создаем список пользователей
        self.users_group1 = [
            User("Иванов Иван Иванович", "IT-специалист"),
            User("Петров Петр Петрович", "Администратор баз данных"),
            User("Сидоров Сидор Сидорович", "Системный администратор"),
        ]

        self.users_group2 = [
            User("Иванова Анна Ивановна", "Frontend-разработчик"),
            User("Петрова Мария Петровна", "Бэкенд-разработчик"),
            User("Сидорова Елена Сидоровна", "Тестировщик"),
        ]

        self.users_group3 = [
            User("Смирнов Иван Иванович", "IT-специалист"),
            User("Кузнецов Петр Петрович", "Системный администратор"),
            User("Васильев Сидор Сидорович", "Администратор баз данных"),
        ]

        self.users_group4 = [
            User("Новикова Анна Петровна", "Web-дизайнер"),
            User("Лебедева Мария Сергеевна", "UX/UI дизайнер"),
            User("Федоров Сергей Анатольевич", "Графический дизайнер"),
        ]

        # Заполняем раскрывающиеся списки
        self.fillTreeWidget(self.menu_tree1, self.users_group1)
        self.fillTreeWidget(self.menu_tree2, self.users_group2)
        self.fillTreeWidget(self.menu_tree3, self.users_group3)
        self.fillTreeWidget(self.menu_tree4, self.users_group4)

        self.resizeEvent(None)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustSizes()

    def adjustSizes(self):
        window_width = self.width()
        window_height = self.height()

        # Адаптируем размеры topbar
        self.topbar.setGeometry(0, 0, window_width, 50)
        self.logo_label.setGeometry(10, 10, 100, 30)
        self.button1.setGeometry(window_width - 200, 10, 75, 30)
        self.button2.setGeometry(window_width - 100, 10, 75, 30)

        # Адаптируем размеры списков
        list_width = 230
        list_height = (window_height - 50) // 4 - 20
        self.menu_tree1.setGeometry(20, 70, list_width, list_height)
        self.menu_tree2.setGeometry(20, 70 + list_height + 10, list_width, list_height)
        self.menu_tree3.setGeometry(20, 70 + 2 * (list_height + 10), list_width, list_height)
        self.menu_tree4.setGeometry(20, 70 + 3 * (list_height + 10), list_width, list_height)

        # Адаптируем размеры окна информации о пользователе
        user_info_width = window_width - 290
        user_info_height = window_height - 70
        user_info_left = 270
        user_info_top = 60
        self.user_info_display.setGeometry(user_info_left, user_info_top, user_info_width, user_info_height)

    def fillTreeWidget(self, tree_widget, users):
        root = QTreeWidgetItem(tree_widget)
        root.setText(0, "Выберите пользователя")
        for user in users:
            item = QTreeWidgetItem(root)
            item.setText(0, user.full_name)

    def displayUsers(self, tree_widget):
        selected_items = tree_widget.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            user_name = selected_item.text(0)
            for i in reversed(range(self.user_info_layout.count())):
                widget = self.user_info_layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

            user_group = None
            if tree_widget == self.menu_tree1:
                user_group = self.users_group1
            elif tree_widget == self.menu_tree2:
                user_group = self.users_group2
            elif tree_widget == self.menu_tree3:
                user_group = self.users_group3
            elif tree_widget == self.menu_tree4:
                user_group = self.users_group4

            for user in user_group:
                if user.full_name == user_name:
                    attributes = [
                        ("ФИО", user.full_name),
                        ("Должность", user.position),
                        ("Время бездействия", "10 минут"),
                        ("Маска подсети", "255.255.255.0"),
                        ("Шлюз", "192.168.1.1"),
                        ("DNS-серверы", "8.8.8.8, 8.8.4.4"),
                        ("Разрешенные приложения", "Браузер, Текстовый редактор")
                    ]
                    for attribute, value in attributes:
                        label = QLabel(f"<b>{attribute}:</b> {value}", self.user_info_display)
                        label.setStyleSheet("color: #fff;")
                        self.user_info_layout.addWidget(label)

                    # Добавляем кнопку "включить режим киоска"
                    self.kiosk_button = QPushButton("Включить режим киоска", self.user_info_display)
                    self.kiosk_button.setStyleSheet("background-color: #FFA500; color: #fff; border: none; border-radius: 5px; padding: 5px;")
                    self.user_info_layout.addWidget(self.kiosk_button)
                    self.kiosk_button.clicked.connect(self.toggleKioskMode)
                    self.kiosk_button.installEventFilter(self)
                    break

    def eventFilter(self, obj, event):
        if obj == self.kiosk_button and event.type() == event.Enter:
            self.kiosk_button.setStyleSheet("background-color: #666; color: #fff; border: none; border-radius: 5px; padding: 5px;")
        elif obj == self.kiosk_button and event.type() == event.Leave:
            self.kiosk_button.setStyleSheet("background-color: #FFA500; color: #fff; border: none; border-radius: 5px; padding: 5px;")
        return super().eventFilter(obj, event)

    def toggleKioskMode(self):
        if self.kiosk_button.text() == "Включить режим киоска":
            self.kiosk_button.setText("Выключить режим киоска")
            self.kiosk_button.setStyleSheet("background-color: #FF0000; color: #fff; border: none; border-radius: 5px; padding: 5px;")
            # Добавьте здесь код для включения режима киоска
            print("Режим киоска включен")
        else:
            self.kiosk_button.setText("Включить режим киоска")
            self.kiosk_button.setStyleSheet("background-color: #FFA500; color: #fff; border: none; border-radius: 5px; padding: 5px;")
            # Добавьте здесь код для выключения режима киоска
            print("Режим киоска выключен")

    def openWindow1(self):
        self.new_window = NewWindow("Профиль")
        self.new_window.show()

    def openWindow2(self):
        self.new_window = NewWindow("Настройки")
        self.new_window.show()

class NewWindow(QMainWindow):
    def __init__(self, window_title):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet("background-color: #fff;")

def main():
    app = QApplication(sys.argv)
    user_info_app = UserInformationApp()
    user_info_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
