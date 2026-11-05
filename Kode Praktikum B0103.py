# ==========================================
# LANGKAH 1: Membuat Variabel Profil Karakter
# ==========================================
nama_hero = "Lancelot"                  # String
level = 10                              # Integer
hp = 1500.5                             # Float
is_alive = True                         # Boolean
inventory = ["Pedang Baja", "Perisai Kayu", "Panah Api"] # List (min 3 item)
atribut = {                             # Dictionary
    "kekuatan": 80,
    "kelincahan": 65
}

# ==========================================
# LANGKAH 2: Menampilkan Informasi Karakter
# ==========================================
print("=== INFORMASI KARAKTER ===")
print(f"Nama Hero : {nama_hero}")
print(f"Level     : {level}")
print(f"HP        : {hp}")
print(f"Status    : {is_alive}")
print(f"Inventory : {inventory}")
print(f"Atribut   : {atribut}")

# ==========================================
# LANGKAH 3: Menampilkan Tipe Data Variabel
# ==========================================
print("\n=== TIPE DATA ===")
print(f"Tipe nama_hero : {type(nama_hero)}")
print(f"Tipe level     : {type(level)}")
print(f"Tipe hp        : {type(hp)}")
print(f"Tipe is_alive  : {type(is_alive)}")
print(f"Tipe inventory : {type(inventory)}")
print(f"Tipe atribut   : {type(atribut)}")

# ==========================================
# LANGKAH 4: Aksi (Tambah Item & Naik Level)
# ==========================================
# Aksi 1: Karakter mendapat item baru (tambah ke list inventory)
inventory.append("Ramuan HP")

# Aksi 2: Karakter naik level (konversi ke float, tambah 0.5)
level = float(level) + 0.5

# ==========================================
# LANGKAH 5: Cetak Informasi Terbaru
# ==========================================
print("\n=== INFORMASI KARAKTER SETELAH UPDATE ===")
print(f"Nama Hero : {nama_hero}")
print(f"Level Baru: {level} (Tipe sekarang: {type(level)})")
print(f"Inventory Baru: {inventory}")