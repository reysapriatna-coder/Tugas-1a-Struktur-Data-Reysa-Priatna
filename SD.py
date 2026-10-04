
# 1. KEBUTUHAN: Penyimpanan Data Secara Berurutan (Menggunakan Array/List)

class PenyimpananBerurutan:
    def __init__(self):
        # Menggunakan list bawaan Python sebagai representasi Array Konkret
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, nama):
        self.data_mahasiswa.append(nama)
        print(f"[ARRAY] Berhasil menyimpan: {nama}")

    def tampilkan_semua(self):
        print(f"[ARRAY] Daftar Urutan Mahasiswa: {self.data_mahasiswa}")



# 2. KEBUTUHAN: Fitur Undo (Menggunakan ADT Stack - Prinsip LIFO)

class FiturUndoStack:
    def __init__(self):
        self.stack = []

    def simpan_aksi(self, aksi):
        # Operasi Push (Menaruh aksi/kegiatan terbaru di tumpukan atas)
        self.stack.append(aksi)
        print(f"[STACK] Aksi dicatat: {aksi}")

    def undo(self):
        # Operasi Pop (Mengambil/membatalkan aksi terakhir - LIFO)
        if not self.is_empty():
            aksi_dibatalkan = self.stack.pop()
            print(f"[STACK] UNDO BERHASIL: Membatalkan {aksi_dibatalkan}")
            return aksi_dibatalkan
        print("[STACK] Tidak ada aksi yang bisa di-undo.")
        return None

    def is_empty(self):
        return len(self.stack) == 0



# 3. KEBUTUHAN: Sistem Antrean Pengolahan Data (Menggunakan ADT Queue - Prinsip FIFO)

class AntreanAkademikQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, nama_mahasiswa):
        # Memasukkan mahasiswa ke barisan antrean paling belakang
        self.queue.append(nama_mahasiswa)
        print(f"[QUEUE] {nama_mahasiswa} masuk ke dalam antrean pendaftaran.")

    def dequeue(self):
        # Mengeluarkan/melayani mahasiswa yang datang pertama kali (FIFO)
        if not self.is_empty():
            mahasiswa_diproses = self.queue.pop(0)
            print(f"[QUEUE] PROSES: Melayani pendaftaran {mahasiswa_diproses}")
            return mahasiswa_diproses
        print("[QUEUE] Antrean kosong.")
        return None

    def is_empty(self):
        return len(self.queue) == 0



# 4. Pencarian Data Berdasarkan Key (Menggunakan Hash Table/Dictionary)

class PencarianKeyHash:
    def __init__(self):
        # Menggunakan Dictionary Python sebagai implementasi praktis Hash Table
        self.database_mahasiswa = {}

    def registrasi_mahasiswa(self, nim, nama, prodi):
        # NIM bertindak sebagai 'Key' unik
        self.database_mahasiswa[nim] = {"nama": nama, "prodi": prodi}
        print(f"[HASH TABLE] Data Teregistrasi -> NIM: {nim} | Nama: {nama}")

    def cari_by_nim(self, nim):
        # Pencarian langsung O(1) menggunakan Key
        if nim in self.database_mahasiswa:
            data = self.database_mahasiswa[nim]
            print(f"[HASH TABLE] DATA DITEMUKAN -> NIM: {nim} | Nama: {data['nama']} | Prodi: {data['prodi']}")
            return data
        print(f"[HASH TABLE] Data dengan NIM {nim} TIDAK ditemukan.")
        return None


# ==============================================================================
# KODE DRIVER / SIMULASI PENGGUNAAN DI SISTEM AKADEMIK
# ==============================================================================
if __name__ == "__main__":
    print("=== SIMULASI SISTEM AKADEMIK MAHASISWA ===\n")

    # --- Pengujian 1: Penyimpanan Berurutan (Array) ---
    print("--- 1. Uji Coba Penyimpanan Berurutan (Array) ---")
    sys_array = PenyimpananBerurutan()
    sys_array.tambah_mahasiswa("Reysa Priatna")
    sys_array.tambah_mahasiswa("Taufickurahman Mirza")
    sys_array.tampilkan_semua()
    print()

    # --- Pengujian 2: Fitur Undo (Stack - LIFO) ---
    print("--- 2. Uji Coba Fitur Undo (Stack LIFO) ---")
    sys_undo = FiturUndoStack()
    sys_undo.simpan_aksi("Input KRS Semester 3")
    sys_undo.simpan_aksi("Ubah Pilihan Kelas Struktur Data")
    sys_undo.undo()  # Harusnya membatalkan aksi "Ubah Pilihan Kelas Struktur Data"
    print()

    # --- Pengujian 3: Antrean (Queue - FIFO) ---
    print("--- 3. Uji Coba Antrean Validasi Dokumen (Queue FIFO) ---")
    sys_queue = AntreanAkademikQueue()
    sys_queue.enqueue("Yahya Abiyu")
    sys_queue.enqueue("Prasetyo Tri Haryadi")
    sys_queue.dequeue()  # Yahya Abiyu harusnya diproses duluan
    print()

    # --- Pengujian 4: Pencarian Cepat Berdasarkan NIM (Hash Table) ---
    print("--- 4. Uji Coba Pencarian Berdasarkan NIM (Hash Table) ---")
    sys_hash = PencarianKeyHash()
    sys_hash.registrasi_mahasiswa("12550111074", "Reysa Priatna", "Teknik Informatika")
    sys_hash.registrasi_mahasiswa("12550111099", "M Rafiq", "Sistem Informasi")
    
    # Melakukan pencarian langsung dengan key NIM
    sys_hash.cari_by_nim("12550111074")
    sys_hash.cari_by_nim("12550111111") # Uji coba jika NIM tidak ada
    print("\n=== Simulasi Selesai ===")
