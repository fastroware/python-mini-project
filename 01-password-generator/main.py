import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.style = tb.Style("cosmo")  # Tema colorful dan modern

        self.createWidgets()

    def createWidgets(self):
        mainFrame = ttk.Frame(self.root, padding=20)
        mainFrame.pack(fill="both", expand=True)

        titleLabel = ttk.Label(mainFrame, text="🎉 Generator Kata Sandi", font=("Segoe UI", 18, "bold"), anchor="center")
        titleLabel.pack(pady=10)

        self.lengthVar = tk.IntVar(value=12)
        lengthLabel = ttk.Label(mainFrame, text="Panjang Kata Sandi:")
        lengthLabel.pack(pady=(20, 5))
        lengthSlider = ttk.Scale(mainFrame, from_=4, to=32, orient="horizontal", variable=self.lengthVar, command=self.updateLengthLabel)
        lengthSlider.pack()
        self.lengthValueLabel = ttk.Label(mainFrame, text="12 karakter")
        self.lengthValueLabel.pack(pady=5)

        self.includeUppercase = tk.BooleanVar(value=True)
        self.includeLowercase = tk.BooleanVar(value=True)
        self.includeDigits = tk.BooleanVar(value=True)
        self.includeSymbols = tk.BooleanVar(value=False)

        optionsFrame = ttk.Frame(mainFrame)
        optionsFrame.pack(pady=10)

        ttk.Checkbutton(optionsFrame, text="Huruf Besar (A-Z)", variable=self.includeUppercase).grid(row=0, column=0, sticky="w", padx=10)
        ttk.Checkbutton(optionsFrame, text="Huruf Kecil (a-z)", variable=self.includeLowercase).grid(row=1, column=0, sticky="w", padx=10)
        ttk.Checkbutton(optionsFrame, text="Angka (0-9)", variable=self.includeDigits).grid(row=0, column=1, sticky="w", padx=10)
        ttk.Checkbutton(optionsFrame, text="Simbol (!@#$)", variable=self.includeSymbols).grid(row=1, column=1, sticky="w", padx=10)

        generateButton = ttk.Button(mainFrame, text="🔐 Buat Kata Sandi", bootstyle="success", command=self.generatePassword)
        generateButton.pack(pady=20)

        self.passwordEntry = ttk.Entry(mainFrame, font=("Segoe UI", 12), justify="center")
        self.passwordEntry.pack(pady=10, ipady=5, fill="x")

        copyButton = ttk.Button(mainFrame, text="📋 Salin", bootstyle="info", command=self.copyToClipboard)
        copyButton.pack()

    def updateLengthLabel(self, event):
        self.lengthValueLabel.config(text=f"{self.lengthVar.get()} karakter")

    def generatePassword(self):
        length = self.lengthVar.get()
        characterPool = ""

        if self.includeUppercase.get():
            characterPool += string.ascii_uppercase
        if self.includeLowercase.get():
            characterPool += string.ascii_lowercase
        if self.includeDigits.get():
            characterPool += string.digits
        if self.includeSymbols.get():
            characterPool += string.punctuation

        if not characterPool:
            messagebox.showwarning("Peringatan", "Pilih minimal satu jenis karakter!")
            return

        password = ''.join(random.choice(characterPool) for _ in range(length))
        self.passwordEntry.delete(0, tk.END)
        self.passwordEntry.insert(0, password)

    def copyToClipboard(self):
        password = self.passwordEntry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Disalin", "Kata sandi berhasil disalin!")
        else:
            messagebox.showwarning("Kosong", "Belum ada kata sandi untuk disalin.")

if __name__ == "__main__":
    root = tb.Window(themename="cosmo")  # Bisa ganti tema: solar, flatly, morph, vapor, cyborg, dll.
    app = PasswordGeneratorApp(root)
    root.mainloop()
