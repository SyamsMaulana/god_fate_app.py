import math

def menu_tcg_ai_assistant():
    print_header()
    print("--- 13. MODUL TCG AI & STRATEGY ANALYZER ---")
    print("1. Analisis Probabilitas Opening Hand (Hypergeometric)")
    print("2. Rekomendasi Taktik Deck Berdasarkan Win-Rate")
    print("3. Kembali ke Menu Utama")
    
    sub_choice = input("\nPilih opsi AI (1-3): ").strip()
    
    if sub_choice == '1':
        print("\n--- SIMULATOR PROBABILITAS KARTU ---")
        try:
            deck_size = int(input("Total kartu dalam Deck (Cth: 40 atau 60): "))
            copies = int(input("Jumlah salinan kartu target dalam Deck (Cth: 3): "))
            hand_size = int(input("Jumlah kartu di Opening Hand (Cth: 5 atau 7): "))
            
            if deck_size <= 0 or copies <= 0 or hand_size <= 0 or copies > deck_size or hand_size > deck_size:
                print("[!] Angka tidak valid. Pastikan proporsi logis.")
            else:
                # Rumus Hipergeometrik: P = 1 - [ C(N-K, n) / C(N, n) ]
                # Menggunakan math.comb untuk Python 3.8+
                prob_none = math.comb(deck_size - copies, hand_size) / math.comb(deck_size, hand_size)
                prob_at_least_one = (1 - prob_none) * 100
                
                print(f"\n[AI Analysis] Peluang mendapatkan minimal 1 kopi kartu target di opening hand adalah: {prob_at_least_one:.2f}%")
                print("Watermark AI: ICAM/Syams Maulana - Al-Haqq Authentic TCG Analytics")
        except ValueError:
            print("[!] Masukkan angka berupa bilangan bulat.")
        input("\nTekan Enter untuk kembali...")
        
    elif sub_choice == '2':
        print("\n--- REKOMENDASI TAKTIK & DECK ARCHETYPE ---")
        print("[i] Berdasarkan analisis data historis guild God of FATE:")
        print("   -> Archetype Aggressive (Contoh: Dragapult ex / Yu-Gi-Oh Beatdown): Pertahankan tempo awal di turn 1-2.")
        print("   -> Archetype Control / Combo (Contoh: Living Death / Control Deck): Fokus manajemen resource *graveyard* dan *hand advantage*.")
        print("   -> Rekomendasi Khalifah: Pertajam konsistensi mesin deck dengan memangkas kartu *tech choice* yang jarang efektif.")
        input("\nTekan Enter untuk kembali...")
    else:
        return
