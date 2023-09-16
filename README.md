**Nama: Muhammad Fakhri Robbani**

**NPM: 2206026252**

**Kelas: PBP C**

**Tugas 3**

**Pertanyaan:**



1. **Apa perbedaan antara form `POST` dan form `GET` dalam Django?**

    `POST` dan `GET` merupakan method HTTP yang digunakan ketika berhubungan dengan _form_. Kedua method ini memiliki beberapa perbedaan sebagai berikut.
    
    1. Penggunaan
        1. Form `POST` digunakan ketika menerima sebuah _request _yang memerlukan perubahan sistem seperti database dan server. Contohnya ketika mengirim data pengguna ke databse dari form pendaftaran.
        2.  Form `GET` digunakan ketika menerina sebuah request yang tidak memerlukan perubahan pada sistem. Contohnya ketika ingin melakukan pencarian suatu data.
    2. Kapasitas Data
        1. Form `POST` dapat mengirim data dalam jumlah yang besar karena dikirim dalam _HTTP Request Body _sehingga tidak ada batasan panjang URL.
        2. Form `GET` memiliki batasan kapaistas dalam pengiriman data karena dikirim dalam _HTTP Request Header _sehingga panjang URL terbatas.
    3. Keamanan Data
        1. Form `POST` lebih aman dalam mengirim data sensitif. Hal ini karena `POST` mengirim data melalui _request body _sehingga tidak dapat terlihat pada URL dan log server.
        2. Form `GET` lebih baik digunakan untuk data yang sifatnya tidak sensitif. Hal ini karena `GET` mengirim data melalui _request header_ sehingga data ditampilkan melalui URL dan dapat dilihat melalui log server.
    4. Idempotency
        1. Form `POST` tidak bersifat Idempoten, artinya _request_ yang sama berulang kali dapat menghasilkan _result _yang berbeda.
        2. Form `GET` bersifat Idempoten, artinya request yang sama berulang kali akan menghasilkan _result _yang sama tanpa mengubah sistem atau database. 
2.  **Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
    1. Penggunaan
    
        XML dan JSON digunakan untuk menyimpan dan mentransmisi data, sedangkan HTML digunakan untuk menampilkan data dalam struktur website.
    
    2. Syntax
        1. XML menggunakan sintaks yang mewajibkan setiap elemennya dibungkus dengan tag.
        2. JSON menggunakan kurung kurawal `{}` dan memiliki struktur `key:value`. JSON juga _support _penggunaan array menggunakan kurung siku `[]`.
        3. HTML menggunakan tag dengan banyak jenis yang masing-masing jenis tag menggambarkan elemen-elemen yang ditampilkan. Mirip seperti XML, HTML juga membungkus elemen yang ditampilkan dengan tag.
    3. Struktur Data
        1. XML memiliki struktur data yang ketat. Dokumen XML memiliki struktur seperti hirarki yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Dokumen XML harus mengandung sebuah root element yang merupakan parent dari elemen lainnya.
        2. JSON memiliki struktur data berupa _key_ dan _value_ serta format filenya dalam bentuk _text_ sehingga file JSON dapat dibuat dan dibaca menggunakan berbagai macam bahasa pemrograman.
        3. HTML memiliki struktur data yang bebas dengan aturan data atau konten yang ditampilkan menggunakan tag yang sesuai dengan fungsinya masing-masing.
3.  **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

    JSON sering digunakan dalam pertukaran data antar aplikasi web modern karena memiliki banyak keunggulan. JSON memiliki desain self-describing dan bentuk data yang merepresentasikan `key` dan `value`, sehingga JSON sangat mudah untuk dimengerti. Selain itu, struktur data yang digunakan juga mendukung untuk objek dan array sehingga mudah digunakan oleh programmer. Meskipun merupakan turunan dari bahasa JavaScript, akan tetapi JSON menggunakan format teks sehingga kode untuk membuat dan membaca file JSON terdapat di berbagai macam bahasa pemrograman.

4.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
        1. Membuat Kerangka Views

            Sebelum membuat form input data, saya membuat sebuah kerangka views untuk memastikan adanya konsistensi dalam desain web agar mengurangi kemungkinan redundansi kode. Saya membuat sebuah folder `templates` pada rood folder dan membuat sebuah template dasar pyoyek html bernama `base.html`. Pada file ini, saya menambahkan baris-baris kode sebagai tanda posisi kode dimana konten akan ditempatkan. Setelah itu, saya menyesuaikan `DIRS` pada `settings.py` agar dapat mendeteksi base.html sebagai berkas template. Selanjutnya saya mengubah kode `main.html` pada folder `templates` di folder aplikasi dengan menambahkan kode tanda bahwa file tersebut merupakan extends dari `base.html`dan kode block konten yang akan disambungkan ke template pada `base.html`.

        2. Membuat Form Input Data

            Langkah pertama yang saya lakukan dalam membuat form input data adalah membuat file struktur form baru bernama `forms.py` pada direktori `main`.saya membuat class `ItemForm` yang mengextend `ModelForm` dari `django.forms`, pada class tersebut saya melakukan inisiasi model `Item` yang saya import dari `main.models` dan melakukan inisiasi fields berupa array dari setiap instance pada model `Item`. Fields ini merupakan data-data yang akan dimintai input pada form. Setelah itu, pada `views.py` direktori `main`, saya membuat fungsi `create_item(request)` yang digunakan untuk menghasilkan formulir yang dapat menambahkan data item secara otomatis setelah data di-submit dari form. Pada fungsi ini, saya melakukan inisiasi form berdasarkan input dari user pada `request.POST` lalu melakukan validasi serta menyimpan data dari form tersebut dan melakukan _redirect_ setelah data form berhasil disimpan. Selanjutnya pada method `show_main()` pada file yang sama, saya menambahkan variabel baru `items` yang mengambil seluruh object Item yang tersimpan di database dan memasukkannya ke dictionary context dengan key `items`. Kemudian saya melakukan routing fungsi `create_item` ke `urls.py` agar dapat diakses dari proyek. 

        3. Menampilkan Form Input Data ke Peramban Web

            Untuk menampilkan form input data ke website, saya membuat file HTML baru pada folder `main/templates` bernama `create_item.html` yang merupakan extends dari `base.html`. Pada file ini, saya membuat form dengan method `POST` dan memanfaatkan kode `{% csrf_token %}` berupa token yang berfungsi sebagai security. Kemudian dalam form tersebut, saya juga membuat tabel dan menampilkan _fields_ form yang sudah dibuat pada `forms.py` sebagai tabel. Terakhir, saya membuat tombol submit untuk mengirimkan _request_ ke fungsi `create_item(request)` pada `views.py`.

        4. Menampilkan Tabel Hasil Input Data dari User

            Saya menambahkan tabel pada file `main.html` yang berisi item-item yang sudah diinput oleh user. Untuk menampilkan item-item, saya menggunakan _looping _setiap item yang ada pada database dan memasukkannya ke tabel. Saya juga menambahkan tombol `Add New Item` untuk merujuk ke halaman `create_item.html`.
            
        5. Menambahkan Informasi Banyak Item yang Tersedia pada Inventory
            Untuk menampilkan banyak item yang tersedia, saya menambahkan variabel baru bernama `items_count` pada fungsi `show_main(request)` di file `views.py` aplikasi `main`. Variabel ini saya isi dengan menghitung banyaknya objek item yang terinisiasi di model `Item` menggunakan kode `Item.objects.count()`. Kemudian saya menambahkan data `items_count` pada dictionary `context` agar dapat dirender ke file `main.html`. Setelah itu, saya menambahkan tag baru di `main.html` yang menampilkan jumlah item yang ada berdasarkan `items_count` di `context` pada `views.py`


    2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
        1. Mengembalikan Data dalam Bentuk XML dan JSON

            Saya membuat penyimpanan data agar dapat dilihat dalam bentuk XML dan JSON. Saya membuat fungsi bernama `show_xml(request)` dan `show_json(request)` yang digunakan untuk menampilkan data dalam format XML dan JSON. Pada fungsi tersebut, saya mengambil seluruh data yang ada pada `Item` dan menyimpannya pada variabel `data`. Kemudian saya mengembalikan respon HTTP yang melakukan _translate_ objek model menjadi format XML untuk fungsi `show_xml(request)` dan JSON untuk fungsi `show_json(request)`. Setelah itu, saya melakukan routing fungsi yang saya buat tadi ke `urls.py` pada direktori aplikasi agar dapat diakses melalui URL.

        2. Mengembalikan Data berdasarkan ID XML dan JSON

            Pada tahap ini, saya membuat fungsi baru bernama `show_xml_by_id(request, id)` dan `show_json_by_id(request, id)` agar dapat mengakses data dengan format XML dan JSON berdasarkan ID pada datanya. Pada fungsi ini, saya melakukan _filtering_ objek `Item` berdasarkan ID yang diinginkan dan menyimpannya ke variabel `data`. Kemudian, saya mengembalikan respon HTTP yang melakukan translate objek model yang sudah di-_filter _menjadi format XML dan JSON. Setelah itu, saya melakukan routing ke `urls.py` dan membuat _URL path_ dapat disesuaikan berdasarkan angka ID nya menggunakan `&lt;int:id>`.

5. **Screenshot hasil akses URL pada Postman**
![alt_text](images/create-item.png)
![alt_text](images/xml.png)
![alt_text](images/xml-1.png)
![alt_text](images/json.png)
![alt_text](images/json-1.png)