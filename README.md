# UAS-PBO
UJIAN AKHIR SEMESTER PBO

Anggota Kelompok 15:
* Attiya Dianti Fadli     (G1A022002)
* Apri Agriansyah         (G1A022056)
* Dian Ardiyanti Saputri  (G1A022084)

## Penjelasan Kode Program
Kode program di atas adalah implementasi sederhana dari aplikasi Notepad menggunakan modul tkinter dalam bahasa pemrograman Python. Aplikasi Notepad memiliki beberapa kelas dan fungsi yang menjalankan berbagai fitur dan fungsionalitas yang terkait dengan editor teks.

Berikut adalah penjelasan singkat tentang beberapa bagian penting dari kode program ini:

1. Import dan Pengaturan Awal:

* Baris pertama mengimpor modul tkinter sebagai tk, yang digunakan untuk membuat antarmuka grafis.
* Baris kedua mengimpor beberapa kelas dan fungsi dari modul tkinter seperti filedialog dan messagebox, yang digunakan untuk dialog pemilihan file dan kotak pesan.
* Kemudian, kelas utama Notepad dibuat dengan konstruktor __init__, yang menginisialisasi aplikasi Notepad dan membuat jendela utama.

2. Membuat Antar Muka Pengguna:

* Metode create_text_area digunakan untuk membuat area teks utama menggunakan objek Text dari tkinter, yang digunakan untuk menampilkan dan mengedit teks.
* Metode create_menu digunakan untuk membuat menu utama dengan submenu seperti "File", "Edit", "Format", "View", dan "Help". Setiap submenu memiliki item-menu dengan fungsi terkait.
* Metode create_status_bar digunakan untuk membuat status bar di bagian bawah jendela, yang menampilkan informasi seperti baris dan kolom saat ini pada teks area.

3. Binding Kejadian (Event Binding):

* Metode bind_events digunakan untuk melakukan binding terhadap beberapa kejadian (event), seperti penggunaan tombol keyboard dan tindakan lain pada aplikasi Notepad.

4. Operasi Utama:

* Metode new_file digunakan untuk membuat file baru dan mengosongkan teks area. Jika ada perubahan yang belum disimpan, pengguna akan diminta untuk menyimpan perubahan sebelum membuat file baru.
* Metode open_file digunakan untuk membuka file yang ada dan mengisikan teksnya ke dalam teks area. Jika ada perubahan yang belum disimpan, pengguna akan diminta untuk menyimpan perubahan sebelum membuka file.
* Metode save_file digunakan untuk menyimpan perubahan ke dalam file yang sudah ada. Jika file belum pernah disimpan sebelumnya, metode save_file_as akan dipanggil.
* Metode save_file_as digunakan untuk menyimpan perubahan ke dalam file baru dengan menggunakan dialog penyimpanan file.
* Metode exit_application digunakan untuk keluar dari aplikasi. Jika ada perubahan yang belum disimpan, pengguna akan diminta untuk menyimpan perubahan sebelum keluar.
* Metode undo dan redo digunakan untuk melakukan operasi undo dan redo pada teks area.
* Metode cut, copy, dan paste digunakan untuk melakukan operasi pemotongan, penyalinan, dan penempelan pada teks area.
* Metode select_all digunakan untuk memilih seluruh teks pada teks area.
* Metode word_wrap digunakan untuk mengaktifkan atau menonaktifkan word wrap pada teks area.

5. Metode Bantuan dan Tentang:

* Metode show_about digunakan untuk menampilkan informasi tentang aplikasi dan perancang aplikasi Notepad.

## Aplikasi Notepad
Notepad adalah sebuah aplikasi bawaan sistem Windows yang memiliki fungsi utama untuk membuat catatan kecil atau catatan sederhana. Selain itu, Notepad juga dapat digunakan untuk mengedit berbagai jenis teks seperti file HTML dan PHP. Notepad dapat diakses melalui beberapa metode, dan terdapat dua jenis Notepad yaitu Notepad biasa dan Notepad++.

Aplikasi Notepad yang dijelaskan dalam kode program tersebut merupakan sebuah program sederhana yang dibuat menggunakan modul tkinter dalam bahasa pemrograman Python. Aplikasi ini berfungsi sebagai editor teks yang memungkinkan pengguna untuk membuat, membuka, menyimpan, dan mengedit file teks. Berikut adalah penjelasan menu-menu yang ada dalam program **Notepad** tersebut:

1. Menu "File":

* "New": Membuat file baru dengan menghapus semua teks yang ada di area teks.
* "Open": Membuka file teks yang ada dan menampilkan isinya di area teks.
* "Recent Files": Menampilkan daftar file terakhir yang dibuka. Fungsionalitasnya masih sama dengan "Open".
* "Save": Menyimpan file yang sedang aktif ke file yang telah ditentukan sebelumnya.
* "Save As": Menyimpan file yang sedang aktif ke file baru dengan meminta lokasi dan nama file.
* "Exit": Keluar dari aplikasi Notepad.

2. Menu "Edit":

* "Undo": Mengembalikan perubahan terakhir yang dilakukan pada teks.
* "Redo": Mengulangi perubahan terakhir yang telah di-undo.
* "Cut": Memotong teks yang dipilih dan menyimpannya ke clipboard.
* "Copy": Menyalin teks yang dipilih dan menyimpannya ke clipboard.
* "Paste": Menempel teks yang ada di clipboard ke posisi kursor.
* "Select All": Memilih seluruh teks yang ada di area teks.

3. Menu "Format":

* "Word Wrap": Mengaktifkan atau menonaktifkan word wrap, yaitu fitur yang membuat teks otomatis pindah ke baris baru ketika mencapai batas lebar area teks.
* "Font": Memilih jenis font yang digunakan untuk teks pada area teks.

4. Menu "View":

* "Zoom In": Memperbesar ukuran teks pada area teks.
* "Zoom Out": Memperkecil ukuran teks pada area teks.
* "Status Bar": Menampilkan atau menyembunyikan status bar yang menunjukkan informasi baris dan kolom saat ini.

5. Menu "Help":

* "About": Menampilkan informasi tentang aplikasi Notepad, termasuk versi dan pembuatnya.

Dengan adanya menu-menu tersebut, pengguna dapat melakukan berbagai tindakan seperti membuat, membuka, dan menyimpan file teks, melakukan pengeditan teks seperti memotong, menyalin, dan menempel teks, mengatur tampilan teks dengan word wrap dan perubahan font, serta melihat informasi tentang aplikasi Notepad.

## Authors
- [https://github.com/dianardiyantii](https://www.github.com/octokatherine)
