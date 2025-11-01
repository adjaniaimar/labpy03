saldo = 1_000_000 

while True:
    print("\n=== MESIN ATM SEDERHANA ===")
    print("Saldo saat ini:",saldo)
    print("1. TARIK TUNAI")
    print("2. KELUAR")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        try:
            tarik = int(input("Masukkan jumlah tunai yang ingin ditarik:Rp"))
            if tarik <= 0:
                print("Jumlah harus lebih dari 0.")
            elif tarik > saldo:
                print("Saldo tidak mencukupi!")
            else:
                saldo -= tarik
                print(f"Penarikan berhasil. SISA SALDO:Rp{saldo:,}")
        except ValueError:
            print("Input tidak valid, masukkan angka.")
    
    elif pilihan == "2":
        print("Terima kasih telah menggunakan mesin ATM by Nevillaz!")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    if saldo == 0:
        print("\nSaldo Anda habis!")
        break
