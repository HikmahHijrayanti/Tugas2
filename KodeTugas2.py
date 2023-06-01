# Membuat kelas Mahasiswa
class Mahasiswa:

    # Membuat init function atau constructor dari kelas Mahasiswa, 
    #sehingga dapat langsung mendefinisikan atribut dari objek yang dibuat, 
    #dalam metode ini memuat dua parameter yaitu 'nama' dan 'nim'
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    # Membuat fungsi untuk menampilkan informasi 'nama' dan 'NIM'
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)

# Membuat kelas Jurusan
class Jurusan:

    # Membuat init function atau constructor dari kelas Jurusan, 
    #sehingga dapat langsung mendefinisikan atribut dari objek yang dibuat, 
    #dalam metode ini memuat dua parameter yaitu 'nama jurusan'
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []
    
    # Membuat fungsi untuk menambahkan objek mahasiswa 
    #ke dalam daftar mahasiswa pada jurusan.
    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
    
     # Membuat fungsi untuk menampilkan daftar mahasiswa dalam jurusan. 
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.nama_jurusan)
        for mahasiswa in self.daftar_mahasiswa:
            print("- Nama:", mahasiswa.nama)
            print("  NIM:", mahasiswa.nim)

# Membuat Kelas Universitas
class Universitas:

    # Membuat init function atau constructor dari kelas Universitas, 
    #sehingga dapat langsung mendefinisikan atribut dari objek yang dibuat, 
    #dalam metode ini memuat dua parameter yaitu 'nama Universitas'
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []
    
    # Membuat fungsi untuk menambahkan objek jurusan ke dalam
    #daftar jurusan pada universitas.
    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)
    
    # Membuat fungsi untuk menampilkan daftar jurusan dalam Universitas. 
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print("- Nama Jurusan:", jurusan.nama_jurusan)


# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan "Teknik Informatika" dan daftar mahasiswa
jurusan_ti = Jurusan("Teknik Informatika")
mahasiswa_1 = Mahasiswa("Hikmah", "G1A022026")
jurusan_ti.tambah_mahasiswa(mahasiswa_1)

# Membuat objek Jurusan "Sistem Informasi" dan daftar mahasiswa
jurusan_si = Jurusan("Sistem Informasi")
mahasiswa_2 = Mahasiswa("Della", "G1F022019")
jurusan_si.tambah_mahasiswa(mahasiswa_2)

# Membuat objek Jurusan "Teknik Elektro" dan daftar mahasiswa
jurusan_te = Jurusan("Teknik Elektro")
mahasiswa_3 = Mahasiswa("Dubes", "G1D022051")
jurusan_te.tambah_mahasiswa(mahasiswa_3)

# Menambahkan jurusan ke dalam Universitas
universitas_xyz.tambah_jurusan(jurusan_ti)
universitas_xyz.tambah_jurusan(jurusan_si)
universitas_xyz.tambah_jurusan(jurusan_te)

# Menampilkan daftar jurusan di Universitas
universitas_xyz.tampilkan_daftar_jurusan()
print("==================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Informatika"
jurusan_ti.tampilkan_daftar_mahasiswa()
print("==================================")

# Menampilkan daftar mahasiswa di Jurusan "Sistem Informasi"
jurusan_si.tampilkan_daftar_mahasiswa()
print("==================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Elektro"
jurusan_te.tampilkan_daftar_mahasiswa()
print("==================================")
