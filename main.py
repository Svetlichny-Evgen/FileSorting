import os
import shutil
import tkinter as tk
from tkinter import filedialog

def sort_files():
    download_folder = selected_folder.get()

    if not os.path.exists(download_folder):
        tk.messagebox.showerror("Ошибка", "Выбранная папка не существует")
        return

    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            category = 'Прочее'

            if extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico']:
                category = 'Изображения'
            elif extension in ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx']:
                category = 'Документы'
            elif extension in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.mpeg', '.mpg', '.webm']:
                category = 'Видео'
            elif extension in ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a']:
                category = 'Аудио'
            elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz']:
                category = 'Архивы'
            elif extension in ['.exe', '.msi', '.dmg', '.pkg']:
                category = 'Установщики'

            if category != 'Прочее':
                destination_folder = category_folders[category]
                destination_path = os.path.join(destination_folder, filename)

                shutil.move(file_path, destination_path)

    tk.messagebox.showinfo("Готово", "Сортировка завершена")

def select_folder():
    folder_path = filedialog.askdirectory()
    selected_folder.set(folder_path)
    selected_folder_textbox.delete(0, tk.END)
    selected_folder_textbox.insert(0, folder_path)

root = tk.Tk()
root.title("Сортировка файлов")
root.geometry("400x200")  # Указываем размер окна

category_folders = {
    'Изображения': r'D:\Сортированные файлы\Изображения',
    'Документы': r'D:\Сортированные файлы\Документы',
    'Видео': r'D:\Сортированные файлы\Видео',
    'Аудио': r'D:\Сортированные файлы\Аудио',
    'Архивы': r'D:\Сортированные файлы\Архивы',
    'Установщики': r'D:\Сортированные файлы\Установщики',
    'Прочее': r'D:\Сортированные файлы\Прочее'
}

selected_folder = tk.StringVar()

label = tk.Label(root, text="Выберите папку для сортировки:")
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

selected_folder_textbox = tk.Entry(frame, textvariable=selected_folder, width=50)
selected_folder_textbox.pack(side=tk.RIGHT)

browse_button = tk.Button(frame, text="📁", command=select_folder)
browse_button.pack(side=tk.LEFT, padx=10)

sort_button = tk.Button(root, text="Начать сортировку", command=sort_files)
sort_button.pack(pady=10)

root.mainloop()
