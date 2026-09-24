import mysql.connector

# ==========================================
# 1. KONEKSI KE MYSQL
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="180706",
    database="db_logika_fuzzy"
)

cursor = db.cursor()


# ==========================================
# 2. FUNGSI KEANGGOTAAN PYTHON
# ==========================================

def bayi_turun(x):
    return (-x + 5) / 2.5


def anak_turun(x):
    return (-x + 12) / 4


def remaja_naik(x):
    return (x - 10) / 2


def remaja_turun(x):
    return (-x + 20) / 2


def pemuda_naik(x):
    return (x - 15) / 3


def pemuda_turun(x):
    return (-x + 25) / 3


def dewasa_naik(x):
    return (x - 18) / 2


def dewasa_turun(x):
    return (-x + 65) / 5


def lansia_naik(x):
    return (x - 60) / 5


def lansia_turun(x):
    return (-x + 80) / 5


# ==========================================
# 3. DAFTAR FUNGSI
# ==========================================

fungsi_python = {
    "(-x+5)/2.5": bayi_turun,
    "(-x+12)/4": anak_turun,
    "(x-10)/2": remaja_naik,
    "(-x+20)/2": remaja_turun,
    "(x-15)/3": pemuda_naik,
    "(-x+25)/3": pemuda_turun,
    "(x-18)/2": dewasa_naik,
    "(-x+65)/5": dewasa_turun,
    "(x-60)/5": lansia_naik,
    "(-x+80)/5": lansia_turun
}


# ==========================================
# 4. DAFTAR TABEL
# ==========================================

tabel = [
    "tb_domain_usia_bayi",
    "tb_domain_usia_anak",
    "tb_domain_usia_remaja",
    "tb_domain_usia_pemuda",
    "tb_domain_usia_dewasa",
    "tb_domain_usia_lansia"
]


# ==========================================
# 5. DAFTAR USIA UNTUK PENGUJIAN
# ==========================================

daftar_usia = [
    2, 4,
    9, 11,
    11, 15,
    17, 23,
    30, 63,
    62, 70
]


# ==========================================
# 6. PROSES PENGUJIAN
# ==========================================

nomor = 1

for usia in daftar_usia:

    print()
    print("==========================================")
    print("PENGUJIAN KE-", nomor)
    print("USIA :", usia)
    print("==========================================")

    for nama_tabel in tabel:

        cursor.execute(
            f"""
            SELECT b_bawah, b_atas, nilai_keanggotaan, fungsi
            FROM {nama_tabel}
            WHERE %s >= b_bawah AND %s <= b_atas
            """,
            (usia, usia)
        )

        data = cursor.fetchall()

        for row in data:

            b_bawah, b_atas, nilai_db, nama_fungsi = row

            if nama_fungsi == "0":

                nilai_mu = 0

            elif nama_fungsi == "1":

                nilai_mu = 1

            elif nama_fungsi in fungsi_python:

                nilai_mu = fungsi_python[nama_fungsi](usia)

            else:

                continue

            nilai_mu = max(0, min(1, nilai_mu))

            print()
            print("Variabel :", nama_tabel)
            print("Interval:", b_bawah, "-", b_atas)
            print("Fungsi   :", nama_fungsi)
            print("μ(x)     :", f"{nilai_mu:.2f}")

    nomor += 1


# ==========================================
# 7. TUTUP KONEKSI
# ==========================================

cursor.close()
db.close()

print()
print("==========================================")
print("SEMUA PENGUJIAN SELESAI")
print("==========================================")