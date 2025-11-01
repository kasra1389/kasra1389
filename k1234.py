import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QSizePolicy
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QEvent

class AdvancedCalculator(QWidget):
    """کلاس ماشین‌حساب پیشرفته با بهینه‌سازی‌های سرعت"""
    
    def __init__(self):
        """مراحل اولیه راه‌اندازی ماشین‌حساب"""
        super().__init__()
        self.memory = None  # متغیر حافظه برای ذخیره عدد
        self.initUI()       # راه‌اندازی رابط کاربری

    def initUI(self):
        """تنظیم رابط کاربری ماشین‌حساب"""
        self.setWindowTitle('ماشین حساب پیشرفته کسری شیرعلی زاده')  # عنوان پنجره
        self.setWindowIcon(QIcon('22.jpg'))  # تنظیم آیکون پنجره
        self.setStyleSheet("background-color: #2c3e50;")  # رنگ پس‌زمینه پنجره
        self.setGeometry(100, 100, 400, 600)  # تنظیم موقعیت و اندازه پنجره

        # ایجاد چیدمان عمودی برای ویجت‌ها
        layout = QVBoxLayout()

        # ایجاد و تنظیم نمایشگر ماشین‌حساب
        self.display = QLineEdit()
        self.display.setReadOnly(True)  # نمایشگر فقط خواندنی است
        self.display.setFont(QFont('Arial', 24))  # تنظیم فونت نمایشگر
        self.display.setAlignment(Qt.AlignRight)  # راست‌چین کردن متن
        self.display.setStyleSheet("background-color: #34495e; color: #ecf0f1; border: 2px solid #2c3e50; padding: 15px; border-radius: 10px;")  # استایل نمایشگر
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # تنظیم اندازه نمایشگر
        layout.addWidget(self.display)

        # تعریف دکمه‌ها و رنگ‌های آنها
        buttons = [
            ('%', '#2980b9'), ('√', '#2980b9'), ('x²', '#2980b9'), ('/', '#c0392b'),
            ('7', '#bdc3c7'), ('8', '#bdc3c7'), ('9', '#bdc3c7'), ('*', '#c0392b'),
            ('4', '#bdc3c7'), ('5', '#bdc3c7'), ('6', '#bdc3c7'), ('-', '#c0392b'),
            ('1', '#bdc3c7'), ('2', '#bdc3c7'), ('3', '#bdc3c7'), ('+', '#c0392b'),
            ('0', '#bdc3c7'), ('.', '#bdc3c7'), ('±', '#2980b9'), ('C', '#e74c3c'),
            ('=', '#27ae60'), ('sin', '#3498db'), ('cos', '#3498db'), ('tan', '#3498db'),
            ('log', '#3498db'), ('ln', '#3498db'), ('M+', '#9b59b6'), ('MR', '#9b59b6'),
        ]

        # ایجاد چیدمان شبکه‌ای برای دکمه‌ها
        grid_layout = QGridLayout()

        # افزودن دکمه‌ها به چیدمان شبکه‌ای
        row, col = 0, 0
        for text, color in buttons:
            button = QPushButton(text)  # ایجاد دکمه
            button.setStyleSheet(f"background-color: {color}; color: #ecf0f1; border: none; padding: 15px; font-size: 18px;")  # استایل دکمه
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # تنظیم اندازه دکمه
            button.clicked.connect(self.on_click)  # اتصال دکمه به تابع on_click
            grid_layout.addWidget(button, row, col)  # افزودن دکمه به چیدمان شبکه‌ای
            col += 1
            if col > 3:
                col = 0
                row += 1

        # اضافه کردن چیدمان دکمه‌ها به چیدمان عمودی
        layout.addLayout(grid_layout)
        self.setLayout(layout)
        self.installEventFilter(self)  # نصب فیلتر رویداد

    def eventFilter(self, source, event):
        """مدیریت تغییر اندازه پنجره و به‌روزرسانی رابط کاربری"""
        if event.type() == QEvent.Resize:
            self.resizeUI()  # فراخوانی تابع به‌روزرسانی اندازه رابط کاربری
        return super().eventFilter(source, event)

    def resizeUI(self):
        """تنظیم اندازه فونت و فضای داخلی در هنگام تغییر اندازه پنجره"""
        base_size = min(self.width(), self.height())  # تعیین اندازه پایه بر اساس کوچک‌ترین بعد پنجره
        font_size = base_size // 20  # تعیین اندازه فونت بر اساس اندازه پنجره
        button_padding = base_size // 30  # تعیین فاصله داخلی دکمه‌ها
        self.display.setFont(QFont('Arial', font_size))  # تنظیم فونت نمایشگر
        for button in self.findChildren(QPushButton):
            button.setFont(QFont('Arial', font_size))  # تنظیم فونت دکمه‌ها
            button.setStyleSheet(button.styleSheet() + f" padding: {button_padding}px;")  # تنظیم فاصله داخلی دکمه‌ها

    def on_click(self):
        """مدیریت کلیک دکمه‌ها و انجام عملیات مختلف"""
        button_text = self.sender().text()  # دریافت متن دکمه فشار داده شده
        try:
            if button_text == 'C':
                self.display.clear()  # پاک کردن نمایشگر
            elif button_text == '=':
                # محاسبه نتیجه و نمایش آن
                result = self.calculate_expression(self.display.text())  
                self.display.setText(result)  # نمایش نتیجه
            elif button_text == '±':
                self.change_sign()  # تغییر علامت عدد
            elif button_text == '√':
                self.display.setText(self.calculate_sqrt(self.display.text()))  # محاسبه ریشه
            elif button_text == 'x²':
                self.display.setText(self.calculate_square(self.display.text()))  # محاسبه مربع
            elif button_text in {'+', '-', '*', '/'}:
                self.display.setText(f"{self.display.text()} {button_text} ")  # افزودن عملگر به عبارت
            elif button_text in {'sin', 'cos', 'tan', 'log', 'ln'}:
                self.display.setText(self.calculate_function(self.display.text(), button_text))  # محاسبه تابع ریاضی
            elif button_text == 'M+':
                self.memory_store()  # ذخیره عدد در حافظه
            elif button_text == 'MR':
                self.memory_recall()  # بازیابی عدد از حافظه
            else:
                self.display.setText(self.display.text() + button_text)  # افزودن متن دکمه به نمایشگر
        except Exception as e:
            self.display.setText('خطا: ' + str(e))  # نمایش خطا در صورت بروز استثنا

    def calculate_expression(self, expression):
        """محاسبه عبارت ریاضی و مدیریت خطاها"""
        try:
            # استفاده از eval با تنظیم محیط محدود برای کاهش خطرات امنیتی
            result = str(eval(expression, {"__builtins__": None}, {}))  
            return self.format_result(result)  # قالب‌بندی نتیجه
        except ZeroDivisionError:
            return 'خطا: تقسیم بر صاز نیست' # مدیریت خطای تقسیم بر صفر
        except ValueError:
            return 'خطا: ورودی نامعتبر'  # مدیریت ورودی نامعتبر
        except Exception:
            return 'خطا: خطای نامشخص'  # مدیریت خطای نامشخص

    def calculate_sqrt(self, value):
        """محاسبه ریشه عدد"""
        try:
            result = math.sqrt(float(value))  # محاسبه ریشه
            return self.format_result(str(result))  # قالب‌بندی نتیجه
        except ValueError:
            return 'خطا: ورودی نامعتبر'  # مدیریت ورودی نامعتبر

    def calculate_square(self, value):
        """محاسبه مربع عدد"""
        try:
            result = float(value) ** 2  # محاسبه مربع عدد
            return self.format_result(str(result))  # قالب‌بندی نتیجه
        except ValueError:
            return 'خطا: ورودی نامعتبر'  # مدیریت ورودی نامعتبر

    def calculate_function(self, value, function):
        """محاسبه توابع ریاضی مختلف"""
        try:
            value = float(value)  # تبدیل مقدار به عدد اعشاری
            if function == 'sin':
                result = math.sin(math.radians(value))  # محاسبه سینوس
            elif function == 'cos':
                result = math.cos(math.radians(value))  # محاسبه کسینوس
            elif function == 'tan':
                result = math.tan(math.radians(value))  # محاسبه تانژانت
            elif function == 'log':
                result = math.log10(value)  # محاسبه لگاریتم بر مبنای 10
            elif function == 'ln':
                result = math.log(value)  # محاسبه لگاریتم طبیعی
            return self.format_result(str(result))  # قالب‌بندی نتیجه
        except ValueError:
            return 'خطا: ورودی نامعتبر'  # مدیریت ورودی نامعتبر

    def change_sign(self):
        """تغییر علامت عدد در نمایشگر"""
        text = self.display.text()
        if text and text[0] == '-':
            self.display.setText(text[1:])  # حذف علامت منفی
        else:
            self.display.setText('-' + text)  # افزودن علامت منفی

    def memory_store(self):
        """ذخیره مقدار نمایشگر در حافظه"""
        if self.display.text():
            self.memory = self.display.text()  # ذخیره مقدار در حافظه

    def memory_recall(self):
        """بازیابی مقدار از حافظه و نمایش آن"""
        if self.memory:
            self.display.setText(self.memory)  # نمایش مقدار حافظه

    def format_result(self, result):
        """قالب‌بندی نتیجه به صورت خوانا"""
        if 'e' in result:
            result = '{:.10f}'.format(float(result))  # قالب‌بندی علمی
        return result

    def keyPressEvent(self, event):
        """مدیریت ورودی‌های کیبورد"""
        key = event.key()
        if key == Qt.Key_Return or key == Qt.Key_Enter:
            result = self.calculate_expression(self.display.text())  # محاسبه نتیجه
            self.display.setText(result)  # نمایش نتیجه
        elif key == Qt.Key_Backspace:
            self.display.backspace()  # حذف آخرین کاراکتر
        elif key == Qt.Key_Escape:
            self.display.clear()  # پاک کردن نمایشگر
        else:
            text = event.text()
            if text in '0123456789.+-*/':
                self.display.setText(self.display.text() + text)  # افزودن کاراکتر به نمایشگر

# اجرای برنامه
if __name__ == '__main__':
    app = QApplication(sys.argv)  # راه‌اندازی برنامه
    calc = AdvancedCalculator()  # ایجاد نمونه از ماشین‌حساب
    calc.show()  # نمایش ماشین‌حساب
    sys.exit(app.exec_())  # اجرای حلقه اصلی برنامه
