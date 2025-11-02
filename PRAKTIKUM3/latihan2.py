modal_awal = 100_000_000
laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

total_keuntungan = 0

for bulan, persen in enumerate(laba, start=1):
    keuntungan_bulan = modal_awal * persen
    total_keuntungan += keuntungan_bulan
    print(f"Bulan {bulan}: Laba {persen*100:.0f}% = Rp{keuntungan_bulan:,.0f}")

print(f"\nTotal keuntungan selama 8 bulan = Rp{total_keuntungan:,.0f}")

