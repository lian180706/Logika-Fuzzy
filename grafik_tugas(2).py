import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# 1. BAYI / ANAK USIA DINI
# =========================================================

x = np.linspace(0, 5, 500)

mu_bayi = np.zeros_like(x)

mu_bayi[x <= 2.5] = 1

kondisi = (x > 2.5) & (x < 5)
mu_bayi[kondisi] = (-x[kondisi] + 5) / 2.5

plt.figure(figsize=(8, 5))
plt.plot(x, mu_bayi, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Bayi / Anak Usia Dini")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(0, 5)
plt.ylim(0, 1.1)
plt.xticks(np.arange(0, 5.1, 0.5))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# 2. ANAK-ANAK
# =========================================================

x = np.linspace(0, 12, 500)

mu_anak = np.zeros_like(x)

mu_anak[x <= 8] = 1

kondisi = (x > 8) & (x < 12)
mu_anak[kondisi] = (-x[kondisi] + 12) / 4

plt.figure(figsize=(8, 5))
plt.plot(x, mu_anak, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Anak-anak")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(0, 12)
plt.ylim(0, 1.1)
plt.xticks(np.arange(0, 13, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# 3. REMAJA
# =========================================================

x = np.linspace(10, 20, 500)

mu_remaja = np.zeros_like(x)

kondisi = (x > 10) & (x < 12)
mu_remaja[kondisi] = (x[kondisi] - 10) / 2

kondisi = (x >= 12) & (x <= 18)
mu_remaja[kondisi] = 1

kondisi = (x > 18) & (x < 20)
mu_remaja[kondisi] = (-x[kondisi] + 20) / 2

plt.figure(figsize=(8, 5))
plt.plot(x, mu_remaja, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Remaja")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(10, 20)
plt.ylim(0, 1.1)
plt.xticks(np.arange(10, 21, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# 4. PEMUDA
# =========================================================

x = np.linspace(15, 25, 500)

mu_pemuda = np.zeros_like(x)

kondisi = (x > 15) & (x < 18)
mu_pemuda[kondisi] = (x[kondisi] - 15) / 3

kondisi = (x >= 18) & (x <= 22)
mu_pemuda[kondisi] = 1

kondisi = (x > 22) & (x < 25)
mu_pemuda[kondisi] = (-x[kondisi] + 25) / 3

plt.figure(figsize=(8, 5))
plt.plot(x, mu_pemuda, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Pemuda")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(15, 25)
plt.ylim(0, 1.1)
plt.xticks(np.arange(15, 26, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# 5. DEWASA
# =========================================================

x = np.linspace(18, 65, 500)

mu_dewasa = np.zeros_like(x)

kondisi = (x > 18) & (x < 20)
mu_dewasa[kondisi] = (x[kondisi] - 18) / 2

kondisi = (x >= 20) & (x <= 60)
mu_dewasa[kondisi] = 1

kondisi = (x > 60) & (x < 65)
mu_dewasa[kondisi] = (-x[kondisi] + 65) / 5

plt.figure(figsize=(8, 5))
plt.plot(x, mu_dewasa, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Dewasa")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(18, 65)
plt.ylim(0, 1.1)
plt.xticks(np.arange(20, 66, 5))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# 6. LANJUT USIA / LANSIA
# =========================================================

x = np.linspace(60, 80, 500)

mu_lansia = np.zeros_like(x)

kondisi = (x > 60) & (x < 65)
mu_lansia[kondisi] = (x[kondisi] - 60) / 5

kondisi = (x >= 65) & (x <= 75)
mu_lansia[kondisi] = 1

kondisi = (x > 75) & (x < 80)
mu_lansia[kondisi] = (-x[kondisi] + 80) / 5

plt.figure(figsize=(8, 5))
plt.plot(x, mu_lansia, linewidth=2)

plt.title("Grafik Fungsi Keanggotaan Lanjut Usia (Lansia)")
plt.xlabel("Usia (tahun)")
plt.ylabel("Nilai Keanggotaan")
plt.xlim(60, 80)
plt.ylim(0, 1.1)
plt.xticks(np.arange(60, 81, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


# =========================================================
# TAMPILKAN SEMUA GRAFIK
# =========================================================

plt.show()