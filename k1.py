# وارد کردن کتابخانه‌های مورد نیاز
import sys  # کتابخانه sys برای دسترسی به متغیرها و توابع مربوط به مفسر پایتون
import math  # کتابخانه math برای انجام محاسبات ریاضی مانند جذر، توابع مثلثاتی و غیره

# وارد کردن کلاس‌ها و ویجت‌های مورد نیاز از PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QIcon  # وارد کردن کلاس‌های مربوط به فونت و آیکون
from PyQt5.QtCore import Qt  # وارد کردن تنظیمات متفرقه مانند ترازبندی متن و غیره

# تعریف کلاس AdvancedCalculator که از QWidget ارث‌بری می‌کند
class AdvancedCalculator(QWidget):
    # سازنده‌ی کلاس که هنگام ایجاد شیء از این کلاس فراخوانی می‌شود
    def __init__(self):
        super().__init__()  # فراخوانی سازنده‌ی کلاس والد (QWidget)

        # تعریف و مقداردهی اولیه متغیرهای مورد نیاز
        self.last_operator = None  # نگهداری آخرین عملگر استفاده شده
        self.last_operand = None  # نگهداری آخرین عدد وارد شده
        self.memory = None  # نگهداری مقدار حافظه برای استفاده در عملیات حافظه (M+ و MR)

        # فراخوانی تابع initUI برای تنظیم رابط کاربری
        self.initUI()

    # تابع initUI برای تنظیمات رابط کاربری گرافیکی
    def initUI(self):
        self.setWindowTitle('ماشین حساب پیشرفته کسری شیر علی زاده')  # تنظیم عنوان پنجره
        self.setWindowIcon(QIcon('calculator_icon.png'))  # تنظیم آیکون پنجره
        self.setStyleSheet("background-color: #2c3e50;")  # تنظیم رنگ پس‌زمینه‌ی پنجره با استفاده از CSS

        # ایجاد یک لایه‌ی عمودی برای چیدمان ویجت‌ها
        layout = QVBoxLayout()

        # ایجاد ویجت نمایشگر (QLineEdit) و تنظیمات آن
        self.display = QLineEdit()
        self.display.setReadOnly(True)  # تنظیم نمایشگر به حالت فقط خواندنی
        self.display.setFont(QFont('Arial', 28))  # تنظیم فونت نمایشگر به Arial با اندازه 28
        self.display.setAlignment(Qt.AlignRight)  # ترازبندی متن نمایشگر به سمت راست
        self.display.setStyleSheet(
            "background-color: #34495e; color: #ecf0f1; border: 2px solid #2c3e50; padding: 15px; border-radius: 10px;"
        )  # تنظیم ظاهر نمایشگر با استفاده از CSS
        layout.addWidget(self.display)  # اضافه کردن نمایشگر به لایه‌ی عمودی

        # تعریف لیستی از دکمه‌ها و رنگ‌های آن‌ها
        buttons = [
            ('%', '#2980b9'),  # دکمه درصد
            ('√', '#2980b9'),  # دکمه جذر
            ('x²', '#2980b9'),  # دکمه توان دو
            ('/', '#c0392b'),  # دکمه تقسیم
            ('7', '#bdc3c7'),  # دکمه عدد 7
            ('8', '#bdc3c7'),  # دکمه عدد 8
            ('9', '#bdc3c7'),  # دکمه عدد 9
            ('*', '#c0392b'),  # دکمه ضرب
            ('4', '#bdc3c7'),  # دکمه عدد 4
            ('5', '#bdc3c7'),  # دکمه عدد 5
            ('6', '#bdc3c7'),  # دکمه عدد 6
            ('-', '#c0392b'),  # دکمه تفریق
            ('1', '#bdc3c7'),  # دکمه عدد 1
            ('2', '#bdc3c7'),  # دکمه عدد 2
            ('3', '#bdc3c7'),  # دکمه عدد 3
            ('+', '#c0392b'),  # دکمه جمع
            ('0', '#bdc3c7'),  # دکمه عدد 0
            ('.', '#bdc3c7'),  # دکمه نقطه اعشاری
            ('±', '#2980b9'),  # دکمه تغییر علامت
            ('C', '#e74c3c'),  # دکمه پاک کردن
            ('=', '#27ae60'),  # دکمه مساوی
            ('sin', '#3498db'),  # دکمه تابع سینوس
            ('cos', '#3498db'),  # دکمه تابع کسینوس
            ('tan', '#3498db'),  # دکمه تابع تانژانت
            ('M+', '#9b59b6'),  # دکمه اضافه کردن به حافظه
            ('MR', '#9b59b6'),  # دکمه بازیابی حافظه
        ]

        # ایجاد یک لایه‌ی جدولی برای چیدمان دکمه‌ها
        grid_layout = QGridLayout()

        # شمارنده‌های ردیف و ستون برای قرار دادن دکمه‌ها در جدول
        row = 0
        col = 0

        # حلقه‌ی تکرار برای ایجاد و تنظیم دکمه‌ها
        for btn_text, btn_color in buttons:
            btn = QPushButton(btn_text)  # ایجاد یک دکمه جدید با متن مشخص شده
            btn.clicked.connect(self.onButtonClick)  # اتصال رویداد کلیک دکمه به تابع onButtonClick
            btn.setStyleSheet(f"background-color: {btn_color}; color: white; font-size: 18px; padding: 15px; border-radius: 10px;")  # تنظیم ظاهر دکمه
            grid_layout.addWidget(btn, row, col)  # اضافه کردن دکمه به لایه‌ی جدولی در مکان مشخص شده
            
            # افزایش شمارنده ستون
            col += 1
            
            # اگر ستون به چهار رسید، به ردیف بعدی بروید و شمارنده ستون را صفر کنید
            if col > 3:
                col = 0
                row += 1

        # اضافه کردن لایه‌ی جدولی به لایه‌ی عمودی
        layout.addLayout(grid_layout)

        # تنظیم لایه‌ی اصلی ویجت به لایه‌ی عمودی
        self.setLayout(layout)

    # تابع onButtonClick برای مدیریت رویداد کلیک دکمه‌ها
    def onButtonClick(self):
        button = self.sender()  # دریافت دکمه‌ای که کلیک شده
        button_text = button.text()  # دریافت متن روی دکمه

        # انجام عملیات مختلف بر اساس متن دکمه
        if button_text == 'C':
            self.display.clear()  # اگر دکمه 'C' کلیک شد، نمایشگر پاک می‌شود
        elif button_text == '=':
            try:
                result = str(eval(self.display.text()))  # محاسبه عبارت وارد شده و تبدیل نتیجه به رشته
                self.display.setText(result)  # نمایش نتیجه در نمایشگر
            except Exception as e:
                self.display.setText('Error')  # در صورت خطا، نمایش 'Error'
        elif button_text == '±':
            current_value = self.display.text()
            if current_value.startswith('-'):
                self.display.setText(current_value[1:])  # اگر عدد منفی است، علامت منفی را حذف کن
            else:
                self.display.setText('-' + current_value)  # اگر عدد مثبت است، علامت منفی اضافه کن
        elif button_text == 'M+':
            try:
                self.memory = eval(self.display.text())  # مقدار فعلی را در حافظه ذخیره کن
            except:
                pass  # در صورت بروز خطا، هیچ کاری انجام نده
        elif button_text == 'MR':
            if self.memory is not None:
                self.display.setText(str(self.memory))  # مقدار حافظه را در نمایشگر نشان بده
        else:
            self.display.setText(self.display.text() + button_text)  # متن دکمه را به نمایشگر اضافه کن

# نقطه ورود به برنامه
if __name__ == '__main__':
    app = QApplication(sys.argv)  # ایجاد یک نمونه از QApplication
    calc = AdvancedCalculator()  # ایجاد یک نمونه از کلاس ماشین حساب
    calc.show()  # نمایش رابط کاربری ماشین حساب
    sys.exit(app.exec_())  # اجرای حلقه اصلی برنامه و خروج امن
