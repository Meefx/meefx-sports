**Nama: Muhammad Fakhri Robbani**

**NPM: 2206026252**

**Kelas: PBP C**

**Link Adaptable: https://meefx-sports.adaptable.app/main/**

**Pertanyaan:**

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    1. **Membuat Project Django**

        Pertama-tama, saya membuat sebuah direktori lokal yang saya beri nama `meefx_sports` untuk menyimpan proyek Django baru yang akan saya buat. Selanjutnya, saya membuat virtual environment dengan nama folder `env` dan mengaktifkannya menggunakan perintah yang sesuai untuk sistem operasi saya. Setelah mengaktifkan virtual environment, langkah selanjutnya adalah menginstal library-library yang dibutuhkan untuk proyek saya. Ini penting agar proyek dapat berjalan dengan baik dan memenuhi kebutuhan fungsionalitasnya. Kemudian, saya membuat proyek Django dengan perintah `django-admin startproject meefx_sports .`, di mana `meefx_sports` adalah nama proyek saya. Proyek ini akan dibuat di dalam direktori yang telah saya persiapkan sebelumnya. Setelah proyek terbentuk, saya mengizinkan akses dari semua host melalui pengaturan pada berkas `settings.py`. Ini memungkinkan aplikasi yang akan saya kembangkan dapat diakses dari berbagai alamat IP. Setelah semua pengaturan awal selesai, saya memastikan bahwa proyek Django dapat berjalan dengan baik dengan menjalankan server Django pada localhost. Setelah proyek berjalan dengan sukses, saya mematikan virtual environment, dan langkah berikutnya adalah membuat berkas `.gitignore` untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git. Ini membantu menghindari masalah dengan repositori Git yang tidak perlu. Terakhir, saya membuat repositori GitHub dengan nama `meefx-sports` dan melakukan inisiasi direktori utama proyek lokal sebagai repositori Git dengan perintah `git init`. Setelah itu, saya menambahkan perubahan dengan menggunakan `git add`, melakukan commit, dan melakukan push ke branch `main` pada repositori yang telah saya buat.

    2. **Membuat aplikasi dengan nama main pada proyek tersebut.**

        Setelah project django terbentuk, saya mengaktifkan kembali virtual environment dan menjalankan perintah `python manage.py startapp main` untuk membuat direktori baru bernama `main` di dalam direktori proyek. Direktori ini akan menjadi struktur awal dalam proyek saya.

    3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**

        Setelah direktori `main` terbentuk, saya melakukan routing direktori aplikasi main agar dapat dijalankan pada proyek. Saya melakukan routing dengan menambahkan direktori aplikasi `main` pada `INSTALLED_APP` di file `settings.py`.  Saya juga membuat direktori `templates` pada direktori aplikasi `main` yang berisi `main.html` yang berisi judul, nama, npm, dan kelas. `main.html` ini dibuat sebagai template yang akan digunakan untuk menampilkan halaman web.

    4. **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib tertentu.**

        Pada direktori aplikasi `main`, saya membuat model pada file `models.py`. Model yang saya buat bernama `Item` yang berisi atribut-atribut `name` dengan tipe `CharField`, `amount` dengan tipe `IntegerField`. `description` dengan tipe `TextField`. Setelah model dibentuk, saya melakukan migrasi untuk melacak perubahan pada model basis data.

    5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**

        Pada tahap ini, saya mengintegrasikan komponen MVT dengan menggunakan fungsi `render` dari `django.shortcut`. Setelah itu saya membuat fungsi `show_main` yang menerima parameter `request`. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. Pada fungsi ini saya membuat dictionary `context` sebagai struktur yang mengemas data yang akan ditampilkan berdasarkan request yang diberikan. Kemudian pada fungsi ini saya mengembalikan fungsi render yang menerima tiga parameter yaitu `request` yang merupakan request dari user, lalu `main.html` yang merupakan halaman html yang ingin ditampilkan, dan dictionary `context` berisi data yang akan diteruskan ke tampilan untuk digunakan sebagai tampilan dinamis. Setelah fungsi tersebut terbentuk, saya melakukan perubahan template pada `main.html` agar dapat menangkap tampilan data dinamis yang diberikan oleh fungsi `show_main`.

    6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**

        Selanjutnya, saya melakukan routing url agar aplikasi `main` dapat dijalankan melalui peramban web. Pertama, saya membuat file `urls.py` pada direktori aplikasi `main`. File `urls.py` tingkat aplikasi ini bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main. Saya membuat variabel `app_name = “main”` yang diberikan untuk memberikan nama unik pada pola URL dalam aplikasi. Selanjutnya saya memanfaatkan fungsi `path` dari `django.urls` untuk membuat pola URL dan memanfaatkan fungsi `show_main` dari `main.views` pada parameter path untuk ditampilkan. Setelah itu, saya menambahkan rute url aplikasi `main` pada `urls.py` yang berada pada direktori proyek agar rute URL pada tingkat proyek dapat terhubung dengan tampilan aplikasi `main`. 

    7. **Membuat dan Melakukan Unit Testing**

        Sebelum melakukan deploy, saya melakukan unit testing terlebih dahulu. Unit testing digunakan untuk mengecek apakah kode yang dibuat bekerja sesuai dengan keinginan. Pertama, saya membuat tes untuk mengecek apakah path URL `/main/` dapat diakses. Kedua, saya membuat  tes untuk mengecek apakah halaman `/main/` di-render menggunakan template `main.html`. Lalu saya menambahkan 3 test case baru dengan membuat sebuah objek `Item` dengan nama `Air Mineral`, dengan jumlah `100` dan deksripsi `Minuman yang ada manis-manisnya.`. 3 Test case ini dilakukan dengan menguji masing-masing atribut Item `name`, `amount`, dan `description` apakah sudah sesuai dengan yang dibuat atau tidak. Terakhir, saya menambahkan testcase apakah output dari `main.html` sesuai dengan ekspektasi.

    8. **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

        Setelah melakukan semua hal diatas, saya melakukan `git push` ke branch `main` untuk mengupdate repositori di GitHub. Selanjutnya saya mendeploy proyek `meefx-sports` pada repo github ke Adaptable.  Saya memilih template `Python App`, `PostgreSQL` sebagai _database_, dan `Python 3.10`. Saya menjalankan perintah `python manage.py migrate && gunicorn meefx_sports.wsgi` digunakan sebagai start command konfigurasi Adaptable. Setelah itu saya mendeploy dengan nama domain `meefx-sports`.

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![alt_text](images/nomor2.png)


3. **Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

    Virtual Environment digunakan untuk menghindari konflik jika kita memiliki proyek lain dalam sistem lokal yang sama. Virtual Environment dapat mencegah terjadinya konflik versi library yang digunakan dalam setiap proyek yang kita buat. Selain itu, virtual environment membuat kita mudah dalam manajemen setiap proyeknya karena proyek kita sudah terisolasi satu dengan yang lain. Dalam membuat aplikasi web berbasis Django, kita dapat membuat proyek tanpa harus menggunakan virtual environment. Namun, hal ini merupakan suatu hal yang lebih baik dihindari karena dapat menyebabkan konflik apabila terdapat proyek-proyek django yang memiliki perbedaan versi library yang digunakan.

4. **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**

    Model-View-Controller (MVC), Model-View-Presenter (MVT), dan Model-View-ViewModel (MVVM) merupakan rancangan arsitektur yang digunakan untuk  memisahkan fungsi aplikasi antara visualisasi, pemrosesan, dan manajemen data (Musyaffa, 2021). Model arsitektur ini dirancang agar mudah untuk diuji dan membuat pemeliharaan menjadi lebih sederhana. Masing-masing arsitektur memiliki perbedaan dalam pendekatan yang digunakan untuk mengelola suatu aplikasi.

    * MVC memanfaatkan Controller sebagai pengontrol Model dan View. View pada MVC ini merupakan tampilan yang akan ditampilkan pada halaman aplikasi yang dibuat.
    * MVT memanfaatkan View sebagai pengontrol Model dan Template. View pada MVT berbeda dengan MVC, dimana View pada MVC berfungsi sebagai Template, sedangkan View pada MVT berfungsi menggantikan Controller pada MVC.
    * MVVM mirip seperti MVC, namun View-Model pada MVVM terhubung langsung dengan view dan menggunakan teknik _databinding_ sehingga memungkinkan perubahan tampilan yang sesuai secara otomatis.

**References**



* Musyaffa, I. (2021, June 2). _MVC vs MVP vs MVVM : Apa Perbedaannya & Mana yang terbaik diantara ketiganya?a_. Agus Hermanto. Retrieved September 9, 2023, from https://agus-hermanto.com/blog/detail/mvc-vs-mvp-vs-mvvm-apa-perbedaannya-mana-yang-terbaik-diantara-ketiganya-a