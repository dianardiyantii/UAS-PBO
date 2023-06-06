# Nama: Dian Ardiyanti Saputri
# Npm : G1A022084
# UAS PBO

import tkinter as tk # Mengimpor modul tkinter sebagai tk
from tkinter import filedialog, messagebox # Mengimpor beberapa kelas dan fungsi dari modul tkinter

# Membuat kelas Notepad
class Notepad:
    def __init__(self, root):
        # Membuat frame utama
        self.root = root # Inisialisasi atribut root
        self.root.title("Notepad") # Mengatur judul jendela menjadi "Notepad"
        self.root.geometry('925x500+300+200') # Mengatur ukuran dan posisi jendela

        self.filename = None # Inisialisasi atribut filename dengan None
        self.text_changed = False # Inisialisasi atribut text_changed dengan False
        
        # Membuat teks area
        self.create_text_area()  # Memanggil fungsi create_text_area untuk membuat area teks
        self.create_menu()  # Memanggil fungsi create_menu untuk membuat menu
        self.create_status_bar()  # Memanggil fungsi create_status_bar untuk membuat status bar

        self.bind_events()  # Memanggil fungsi bind_events untuk melakukan binding terhadap event
        
    def create_text_area(self):
        self.textarea = tk.Text(self.root, undo=True, bg="light blue", fg="black")  # Membuat objek TextArea dengan atribut tertentu
        self.textarea.pack(expand=True, fill="both") # Menempatkan objek TextArea di jendela
    
    # Membuat objek Menu
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar) # Mengatur menu utama jendela
        # Membuat menu file
        file_menu = tk.Menu(menubar, tearoff=0) # Membuat submenu "File" pada menu utama
        file_menu.add_command(label="New", command=self.new_file)  # Menambahkan item "New" ke submenu "File"
        file_menu.add_command(label="Open", command=self.open_file) # Menambahkan item "Open" ke submenu "File"
        file_menu.add_command(label="Recent Files", command=self.open_file) # Menambahkan item "Recent Files" ke submenu "File"
        file_menu.add_separator() # Menambahkan garis pemisah di submenu "File"
        file_menu.add_command(label="Save", command=self.save_file)  # Menambahkan item "Save" ke submenu "File"
        file_menu.add_command(label="Save As", command=self.save_file_as) # Menambahkan item "Save As" ke submenu "File"
        file_menu.add_separator() # Menambahkan garis pemisah di submenu "File"
        file_menu.add_command(label="Exit", command=self.exit_application) # Menambahkan item "Exit" ke submenu "File"
        
        menubar.add_cascade(label="File", menu=file_menu)  # Menambahkan submenu "File" ke menu utama
        
        # Membuat menu edit
        edit_menu = tk.Menu(menubar, tearoff=0) # Membuat submenu "Edit" pada menu utama
        edit_menu.add_command(label="Undo", command=self.undo) # Menambahkan item "Undo" ke submenu "Edit"
        edit_menu.add_command(label="Redo", command=self.redo) # Menambahkan item "Redo" ke submenu "Edit"
        edit_menu.add_separator() # Menambahkan garis pemisah di submenu "Edit"
        edit_menu.add_command(label="Cut", command=self.cut) # Menambahkan item "Cut" ke submenu "Edit"
        edit_menu.add_command(label="Copy", command=self.copy) # Menambahkan item "Copy" ke submenu "Edit"
        edit_menu.add_command(label="Paste", command=self.paste) # Menambahkan item "Paste" ke submenu "Edit"
        edit_menu.add_separator() # Menambahkan garis pemisah di submenu "Edit"
        edit_menu.add_command(label="Select All", command=self.select_all) # Menambahkan item "Select All" ke submenu "Edit"
        
        menubar.add_cascade(label="Edit", menu=edit_menu) # Menambahkan submenu "Edit" ke menu utama
        
        # Membuat menu format
        format_menu = tk.Menu(menubar, tearoff=0) # Membuat submenu "Format" pada menu utama
        format_menu.add_checkbutton(label="Word Wrap", command=self.word_wrap) # Menambahkan checkbutton "Word Wrap" ke submenu "Format"
        font_menu = tk.Menu(format_menu, tearoff=0) # Membuat submenu "Font" pada submenu "Format"
        # Menambahkan jenis item font ke dalam submenu "Font"
        font_menu.add_command(label="Arial", command=lambda: self.change_font("Arial"))
        font_menu.add_command(label="Times New Roman", command=lambda: self.change_font("Times New Roman"))
        font_menu.add_command(label="Courier", command=lambda: self.change_font("Courier"))
        # Menambahkan submenu "Font" ke submenu "Format"
        format_menu.add_cascade(label="Font", menu=font_menu)
        # Menambahkan submenu "Format" ke menu utama
        menubar.add_cascade(label="Format", menu=format_menu)
        
        # Membuat menu view
        view_menu = tk.Menu(menubar, tearoff=0) # Membuat submenu "View" pada menu utama
        view_menu.add_command(label="Zoom In", command=self.zoom_in) # Menambahkan item "Zoom In" ke submenu "View"
        view_menu.add_command(label="Zoom Out", command=self.zoom_out) # Menambahkan item "Zoom Out" ke submenu "View"
        view_menu.add_separator() # Menambahkan garis pemisah di submenu "View"
        view_menu.add_checkbutton(label="Status Bar", command=self.toggle_status_bar) # Menambahkan checkbutton "Status Bar" ke submenu "View"
        menubar.add_cascade(label="View", menu=view_menu) # Menambahkan submenu "View" ke menu utama
        
        # Membuat menu help
        help_menu = tk.Menu(menubar, tearoff=0) # Membuat submenu "Help" pada menu utama
        help_menu.add_command(label="About", command=self.show_about) # Menambahkan item "About" ke submenu "Help"
        menubar.add_cascade(label="Help", menu=help_menu) # Menambahkan submenu "Help" ke menu utama

        self.show_status_bar = tk.BooleanVar() # Membuat variabel boolean untuk status bar
        self.show_status_bar.set(True) # Mengatur nilai awal variabel show_status_bar menjadi True

        self.status_bar = tk.Label(self.root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W) # Membuat objek Label untuk status bar
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X) # Menempatkan objek Label status bar di jendela

        # Membuat binding untuk menampilkan baris dan kolom pada status bar
        self.textarea.bind("<Key>", self.update_status_bar)

        # Membuat variabel untuk zoom
        self.zoom = 100

    # Membuat status bar
    def create_status_bar(self): 
        self.status_bar = tk.Label(self.root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W) # Membuat objek Label untuk status bar
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X) # Menempatkan objek Label status bar di jendela
    
    # Membuat binding untuk kontrol keyboard
    def bind_events(self):
        self.textarea.bind("<Key>", self.update_status_bar) # Membuat binding untuk menampilkan baris dan kolom pada status bar
        # Membuat binding untuk tombol Ctrl + "N, O, A, Shift+S, Z, Y, X, C, V"
        self.textarea.bind("<Control-n>", lambda event: self.new_file())
        self.textarea.bind("<Control-o>", lambda event: self.open_file())
        self.textarea.bind("<Control-s>", lambda event: self.save_file())
        self.textarea.bind("<Control-Shift-s>", lambda event: self.save_file_as())
        self.textarea.bind("<Control-z>", lambda event: self.undo())
        self.textarea.bind("<Control-y>", lambda event: self.redo())
        self.textarea.bind("<Control-x>", lambda event: self.cut())
        self.textarea.bind("<Control-c>", lambda event: self.copy())
        self.textarea.bind("<Control-v>", lambda event: self.paste())
    
    # Metode untuk membuat file baru
    def new_file(self):
        if self.text_changed:
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
            if response is None:
                return
            elif response:
                self.save_file()
        self.textarea.delete("1.0", "end")
        self.filename = None
        self.text_changed = False
        
    # Metode untuk membuka file
    def open_file(self):
        if self.text_changed:
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
            if response is None:
                return
            elif response:
                self.save_file()
        file = filedialog.askopenfile(mode="r", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file is not None:
            self.filename = file.name
            self.textarea.delete("1.0", "end")
            self.textarea.insert("1.0", file.read())
            self.text_changed = False
    
    # Membuat metode untuk membuka file terbaru
    def open_recent_file(self, filename):
        with open(filename, "r") as file:
            self.textarea.delete("1.0", "end")
            self.textarea.insert("1.0", file.read())
    
    # Membuat metode untuk menyimpan file
    def save_file(self):
        if self.filename is None:
            self.save_file_as()
        else:
            with open(self.filename, "w") as file:
                file.write(self.textarea.get("1.0", "end-1c"))
            self.text_changed = False
    
    # Metode untuk menyimpan file dalam bentuk yang diinginkan
    def save_file_as(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file is not None:
            self.filename = file.name
            file.write(self.textarea.get("1.0", "end-1c"))
            self.text_changed = False
            file.close()
    
    # Metode untuk keluar dari aplikasi
    def exit_application(self):
        if self.text_changed:
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
            if response is None:
                return
            elif response:
                self.save_file()
        
        self.root.quit()
    
    # Metode untuk mengembalikan perubahan yang terakhir
    def undo(self):
        self.textarea.event_generate("<<Undo>>")

    # Metode untuk mengulangi perubahan terakhir 
    def redo(self):
        self.textarea.event_generate("<<Redo>>")

    # Metode untuk memotong teks yang diseleksi 
    def cut(self):
        self.textarea.event_generate("<<Cut>>")
    
    # Metode untuk menyalin teks yang diseleksi
    def copy(self):
        self.textarea.event_generate("<<Copy>>")
    
    # Metode untuk menempel teks di clipboard
    def paste(self):
        self.textarea.event_generate("<<Paste>>")
    
    # Metode untuk memiliki seluruh teks pada teks area
    def select_all(self):
        self.textarea.tag_add(tk.SEL, "1.0", tk.END)
        self.textarea.mark_set(tk.INSERT, "1.0")
        self.textarea.see(tk.INSERT)
        return "break"
    
    # Metode untuk mengaktifkan dan menonaktifkan word wrap
    def word_wrap(self):
        if self.textarea["wrap"] == "none":
            self.textarea["wrap"] = "word"
        else:
            self.textarea["wrap"] = "none"

    # Metode untuk mengubah jenis font 
    def change_font(self, font_name):
        self.textarea.configure(font=(font_name, 12))
    
    # Metode untuk memperbesar teks pada teks area
    def zoom_in(self):
        self.zoom(0.9)
        
    # Metode untuk memperkecil teks pada teks area
    def zoom_out(self):
        self.zoom(0.9)
        
    def zoom(self, factor):
        current_font = self.textarea["font"]
        font_name, font_size = current_font.split()
        new_size = int(float(font_size) * factor)
        self.textarea.configure(font=(font_name, new_size))
    
    # Metode untuk menampilkan atau menyembunyikan status bar
    def toggle_status_bar(self):
        self.show_status_bar.set(not self.show_status_bar.get())
        if self.show_status_bar.get():
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.status_bar.pack_forget()
    
    # Metode untuk memperbarui status bar dengan jumlah baris dan kolom
    def update_status_bar(self, event):
        row, col = self.textarea.index(tk.INSERT).split(".")
        self.status_bar.config(text=f"Line: {row} | Column: {col}")
        self.text_changed = True
    
    # Metode untuk menampilkan informasi tentang aplikasi
    def show_about(self):
        messagebox.showinfo("About", "Notepad v1.0\nCreated by Team 15\nAtiya Dianti Fadli (G1A022002)\nDian Ardiyanti Saputri (G1A022084)\nApri Agriansyah (G1A022056)")

# Menjalankan program
root = tk.Tk()
notepad = Notepad(root)
root.mainloop()

