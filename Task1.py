import random
import tkinter as tk
from tkinter import messagebox

# Глобальний масив
array = []


def create_array():
    global array
    array = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
    show_array()


def show_array():
    if not array:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Масив ще не створено.\n")
        return

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Масив 3x3:\n")
    for row in array:
        output.insert(tk.END, str(row) + "\n")


def sum_array():
    if not array:
        messagebox.showwarning("Попередження", "Спочатку створіть масив.")
        return

    total = sum(sum(row) for row in array)
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Масив:\n")
    for row in array:
        output.insert(tk.END, str(row) + "\n")
    output.insert(tk.END, f"\nСума всіх елементів: {total}\n")


def find_min_max():
    if not array:
        messagebox.showwarning("Попередження", "Спочатку створіть масив.")
        return

    max_val = array[0][0]
    min_val = array[0][0]
    max_index = (0, 0)
    min_index = (0, 0)

    for i in range(3):
        for j in range(3):
            if array[i][j] > max_val:
                max_val = array[i][j]
                max_index = (i, j)
            if array[i][j] < min_val:
                min_val = array[i][j]
                min_index = (i, j)

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Масив:\n")
    for row in array:
        output.insert(tk.END, str(row) + "\n")
    output.insert(tk.END, f"\nМаксимум: {max_val}, індекс: {max_index}\n")
    output.insert(tk.END, f"Мінімум: {min_val}, індекс: {min_index}\n")


def sort_rows():
    if not array:
        messagebox.showwarning("Попередження", "Спочатку створіть масив.")
        return

    sorted_array = [sorted(row) for row in array]

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Відсортований масив по рядках:\n")
    for row in sorted_array:
        output.insert(tk.END, str(row) + "\n")


# Вікно
root = tk.Tk()
root.title("Робота з двовимірним масивом")
root.geometry("500x400")
root.configure(bg="#FFD1DC")

# Заголовок
label = tk.Label(root, text="Операції з масивом 3x3", font=("Arial", 14), bg="#FFD1DC")
label.pack(pady=10)

# Кнопки
frame_buttons = tk.Frame(root, bg="#FFD1DC")
frame_buttons.pack(pady=10)

btn_create = tk.Button(frame_buttons, text="Створити масив", width=20, command=create_array, bg="#FFF0F5")
btn_create.grid(row=0, column=0, padx=5, pady=5)

btn_show = tk.Button(frame_buttons, text="Показати масив", width=20, command=show_array, bg="#FFF0F5")
btn_show.grid(row=0, column=1, padx=5, pady=5)

btn_sum = tk.Button(frame_buttons, text="Сума елементів", width=20, command=sum_array, bg="#FFF0F5")
btn_sum.grid(row=1, column=0, padx=5, pady=5)

btn_minmax = tk.Button(frame_buttons, text="Макс / Мін", width=20, command=find_min_max, bg="#FFF0F5")
btn_minmax.grid(row=1, column=1, padx=5, pady=5)

btn_sort = tk.Button(frame_buttons, text="Сортувати рядки", width=20, command=sort_rows, bg="#FFF0F5")
btn_sort.grid(row=2, column=0, padx=5, pady=5)

btn_exit = tk.Button(frame_buttons, text="Вихід", width=20, command=root.destroy, bg="#FFF0F5")
btn_exit.grid(row=2, column=1, padx=5, pady=5)

# Поле виводу
output = tk.Text(root, width=50, height=12, font=("Consolas", 11), bg="#FFF5F7")
output.pack(pady=10)

root.mainloop()