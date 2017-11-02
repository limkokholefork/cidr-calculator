## CIDR Calculator

Made by : Reinhard Linardi (13515011)  
Language : Python 2.7 

### Petunjuk penggunaan program

Run `make run` untuk menjalankan program. Masukkan NIM saat ada prompt *NIM* dan *Verify NIM*.

### Proses pengerjaan

#### Phase 1
Pada soal diketahui host, tentukan sebuah subnet yang valid untuk host yang disediakan. Soal ini tidak menyebutkan batasan subnet yang dapat digunakan, maka cukup menjawab subnet **0.0.0.0/0**.

#### Phase 2
Pada soal diketahui subnet, tentukan berapa jumlah host valid untuk subnet yang telah disediakan (termasuk *broadcast* dan *gateway*). Caranya, kita menentukan dulu panjang network address, yaitu angka pada subnet di belakang tanda slash (CIDR netmask). Angka tersebut menunjukkan panjang network address dalam bit. Pada IPv4, panjang IP total adalah 32 bit, sehingga panjang host address yang valid adalah (32 - panjang CIDR netmask) bit. Sehingga, jumlah host yang valid adalah **2^(panjang host address)**

#### Phase 3
Pada soal diberikan subnet dan host, tentukan apakah host berada dalam subnet tersebut. Caranya, pertama tentukan dulu CIDR netmask.  Lalu, ubah IP address host dan subnet menjadi integer. Setelah itu, hitung jumlah host yang valid untuk subnet dengan CIDR netmask tersebut. Host akan berada di dalam subnet jika **IP address host (integer) ⊕ IP address subnet < jumlah host valid** (⊕ merupakan lambang XOR). Karena jika hasil XOR lebih dari jumlah host valid, maka ada perbedaan pada bit network address antara host dan subnet. Jika host berada di dalam subnet, output **'T'**, jika tidak output **'F'**.
