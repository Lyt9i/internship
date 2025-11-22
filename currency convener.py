import tkinter as tk
from tkinter import ttk

# Создаем главное окно
window = tk.Tk()
window.title("Конвертер валют")
window.geometry("300x300")

# Курсы валют
exchange_rates = {
    'USD': 95.0,
    'EUR': 102.0,
    'CNY': 13.0,
    'GBP': 120.0,
    'RUB': 1.0
}


# Функция для конвертации
def convert_currency():
    try:
        # Получаем данные из полей
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        # Конвертируем через рубли
        if from_curr != 'RUB':
            rub_amount = amount * exchange_rates[from_curr]
        else:
            rub_amount = amount

        if to_curr != 'RUB':
            result = rub_amount / exchange_rates[to_curr]
        else:
            result = rub_amount

        # Показываем результат
        result_label.config(text=f"Результат: {result:.2f} {to_curr}")

    except:
        result_label.config(text="Ошибка! Введите число")


# Создаем элементы интерфейса
tk.Label(window, text="Конвертер валют", font=("Arial", 14)).pack(pady=10)

# Поле для ввода суммы
tk.Label(window, text="Сумма:").pack()
amount_entry = tk.Entry(window, width=20)
amount_entry.pack(pady=5)
amount_entry.insert(0, "100")  # Пример значения

# Выбор валют
currency_frame = tk.Frame(window)
currency_frame.pack(pady=10)

tk.Label(currency_frame, text="Из:").grid(row=0, column=0, padx=5)
from_currency = ttk.Combobox(currency_frame, values=list(exchange_rates.keys()), width=8)
from_currency.set('USD')
from_currency.grid(row=0, column=1, padx=5)

tk.Label(currency_frame, text="В:").grid(row=0, column=2, padx=5)
to_currency = ttk.Combobox(currency_frame, values=list(exchange_rates.keys()), width=8)
to_currency.set('RUB')
to_currency.grid(row=0, column=3, padx=5)

# Кнопка конвертации
convert_btn = tk.Button(window, text="Конвертировать", command=convert_currency, bg="lightblue")
convert_btn.pack(pady=10)

# Поле для результата
result_label = tk.Label(window, text="Результат: ", font=("Arial", 12))
result_label.pack()

# Запускаем приложение
window.mainloop()