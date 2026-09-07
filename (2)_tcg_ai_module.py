import math
from datetime import datetime

# =========================================================
# GOD OF FATE OPERATIONS - TCG AI & STRATEGY ANALYZER MODULE
# Framework: Inverted Pyramid & Al-Haqq Protocol
# Author: ICAM / Syams Maulana (GOD•MauL)
# =========================================================

def calculate_hypergeometric(deck_size, copies, hand_size):
    """
    Menghitung persentase peluang mendapatkan minimal 1 salinan kartu target 
    di opening hand menggunakan distribusi hipergeometrik.
    """
    if deck_size <= 0 or copies <= 0 or hand_size <= 0 or copies > deck_size or hand_size > deck_size:
        return None
    
    # P = 1 - [ C(N-K, n) / C(N, n) ]
    prob_none = math.comb(deck_size - copies, hand_size) / math.comb(deck_size, hand_size)
    prob_at_least_one = (1 - prob_none) * 100
    return prob_at_least_one

def tcg_ai_dashboard():
    while True:
        print("\n=================================================")
        print("       GOD OF FATE - TCG AI ANALYZER MODULE      ")
        print("       Inverted Pyramid & Al-Haqq Protocol       ")
        print("=================================================\n")
        print("1. Simulasi Probabilitas Opening Hand (Hipergeometrik)")
        print("2. Analisis & Rekomendasi Taktik Deck Archetype")
        print("3. Cetak Laporan Analisis Berwatermark (AI Authenticity)")
        print("4. Keluar ke Menu Utama")
        
        choice = input("\nPilih opsi AI (1-4): ").strip()
        
        if choice == '1':
            print("\n--- SIMULATOR PROBABILITAS KARTU ---")
            try:
                deck_size = int(input("Total kartu dalam Deck (Cth: 40 untuk Yu-Gi-Oh / 60 untuk Pokemon/MTG): "))
                copies = int(input("Jumlah salinan kartu target dalam Deck (Cth: 3): "))
                hand_size = int(input("Jumlah kartu di Opening Hand (Cth: 5 atau 7): "))
                
                result = calculate_hypergeometric(deck_size, copies, hand_size)
                if result is None:
                    print("[!] Kesalahan: Proporsi angka tidak valid atau melebihi ukuran deck.")
                else:
                    print(f"\n[AI Result] Peluang mendapatkan minimal 1 kopi kartu target di opening hand: {result:.2f}%")
                    print("Watermark AI: ICAM/Syams Maulana - Al-Haqq Authentic TCG Analytics")
            except ValueError:
                print("[!] Masukkan angka berupa bilangan bulat.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '2':
            print("\n--- REKOMENDASI TAKTIK & DECK ARCHETYPE ---")
            print("[i] Berdasarkan pola permainan Guild God of FATE:")
            print("   -> Archetype Aggressive / Beatdown: Maksimalkan konsistensi barisan penyerang di awal giliran.")
            print("   -> Archetype Control / Combo (Contoh: Living Death / Control): Jaga manajemen resource dan tempo graveyard.")
            print("   -> Catatan Khalifah: Evaluasi kartu tech-choice yang persentase kontribusinya rendah di bawah 50%.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '3':
            print("\n--- LAPORAN OTENTIKASI AI ---")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report_text = f"Laporan Analisis TCG AI - {timestamp}\nOtoritas: ICAM / Syams Maulana (GOD•MauL)\nStatus: Valid & Terverifikasi Al-Haqq Protocol."
            print(f"\n{report_text}")
            
            # Simpan otomatis ke file teks
            with open("tcg_ai_report.txt", "w", encoding="utf-8") as f:
                f.write(report_text)
            print("\n[+] Laporan berhasil dicetak dan disimpan ke 'tcg_ai_report.txt'.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif choice == '4':
            print("\nKeluar dari TCG AI...")
            break
        else:
            print("\n[!] Pilihan tidak valid. Masukkan angka 1 sampai 4.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    tcg_ai_dashboard()
