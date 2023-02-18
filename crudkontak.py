# Program     : crudkontak.py
# Deskripsi   : CRUD kontak 1B-D4.
# Nama/NIM    : Rafif Shabi Prasetyo/221524055
# Tanggal     : 17-02-2022
# Compiler    : Visual Studio Code
# ============================================

import os

def baca_kontak_dari_file():
    kontak = {}
    try:
        with open("kontak.txt", "r") as file:
            for line in file:
                nama, nomor = line.strip().split(":")
                kontak[nama] = nomor
    except FileNotFoundError:
        print("File kontak tidak ditemukan. Membuat file baru.")
        open("kontak.txt", "w").close()
    return kontak

def buat_kontak(nama, nomor_telepon):
    with open("kontak.txt", "a") as file:
        file.write(f"{nama}:{nomor_telepon}\n")

def lihat_kontak():
    kontak = baca_kontak_dari_file()
    if kontak:
        for nama, nomor in kontak.items():
            print(f"{nama}: {nomor}")
    else:
        print("Tidak ada kontak dalam daftar")

def cari_kontak(nama):
    kontak = baca_kontak_dari_file()
    if nama in kontak:
        print(f"{nama}: {kontak[nama]}")
    else:
        print(f"Kontak {nama} tidak ditemukan")

def update_kontak(nama, nomor_telepon):
    kontak = baca_kontak_dari_file()
    if nama in kontak:
        kontak[nama] = nomor_telepon
        with open("kontak.txt", "w") as file:
            for nama, nomor in kontak.items():
                file.write(f"{nama}:{nomor}\n")
        print("Kontak berhasil diupdate")
    else:
        print(f"Kontak {nama} tidak ditemukan")

def hapus_kontak(nama):
    kontak = baca_kontak_dari_file()
    if nama in kontak:
        del kontak[nama]
        with open("kontak.txt", "w") as file:
            for nama, nomor in kontak.items():
                file.write(f"{nama}:{nomor}\n")
        print("Kontak berhasil dihapus")
    else:
        print(f"Kontak {nama} tidak ditemukan")

pilihan = ""
while pilihan != "6":
    print("--- Phone Books Kelas ---")
    print("1. Lihat Kontak ")
    print("2. Cari Kontak")
    print("3. Buat Kontak Baru ")
    print("4. Update Kontak ")
    print("5. Hapus Kontak")
    print("6. Keluar ")

    pilihan = input("Masukkan Pilihan : ")

    if pilihan == "1":
        lihat_kontak()
    elif pilihan == "2":
        nama = input("Masukkan nama kontak yang ingin dicari: ")
        cari_kontak(nama)
    elif pilihan == "3":
        nama = input("Masukkan nama: ")
        nomor_telepon = input("Masukkan nomor telepon: ")
        buat_kontak(nama, nomor_telepon)
        print("Kontak berhasil ditambahkan")
    elif pilihan == "4":
        nama = input("Masukkan nama kontak yang ingin diupdate: ")
        nomor_telepon = input("Masukkan nomor telepon baru: ")
        update_kontak(nama, nomor_telepon)
    elif pilihan == "5":
        nama = input("Masukkan nama kontak yang ingin dihapus: ")
        hapus_kontak(nama)
    elif pilihan == "6":
        konfirmasi = input("Apakah anda yakin ingin keluar? (Y/N) ")
        if konfirmasi == "Y"or"y":
            print("Terima kasih!")
            break
    else:
        print("Input salah, silahkan coba lagi.")

