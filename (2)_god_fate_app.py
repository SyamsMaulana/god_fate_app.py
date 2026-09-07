import os
import json
import csv
from datetime import datetime

# ==========================================
# GOD OF FATE OPERATIONS - CORE CLI SYSTEM
# Framework: Inverted Pyramid & Al-Haqq Protocol
# Author: ICAM / Syams Maulana (GOD•MauL)
# ==========================================

TEAM_FILE = "team_registry.json"
MATCH_FILE = "match_history.json"
TOURNAMENT_FILE = "tournament_registry.json"
PAIRING_ARCHIVE = "pairing_archive.json"

def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    print("=================================================")
    print("       GOD OF FATE OPERATIONS - DASHBOARD        ")
    print("                                                 ")
    print("       Inverted Pyramid & Al-Haqq Protocol       ")
    print("=================================================\n")

def menu_registrasi_tim():
    print_header()
    print("--- 1. REGISTRASI TIM / AGEN BARU ---")
    teams = load_data(TEAM_FILE)
    name = input("Masukkan Nama Tim / Agen (GOD•MauL / Lainnya): ").strip()
    if not name:
        print("[!] Nama tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        return
    
    deck = input("Masukkan Archetype Deck Andalan (Cth: Dragapult ex / Living Death): ").strip()
    new_entry = {
        "id": len(teams) + 1,
        "name": name,
        "deck": deck,
        "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "watermark": "ICAM/Syams Maulana - Al-Haqq Authentic"
    }
    teams.append(new_entry)
    save_data(TEAM_FILE, teams)
    print(f"\n[+] Sukses mendaftarkan: {name} ({deck})!")
    input("\nTekan Enter untuk kembali ke menu...")

def menu_lihat_tim():
    print_header()
    print("--- 2. DAFTAR TIM & AGEN AKTIF ---")
    teams = load_data(TEAM_FILE)
    if not teams:
        print("[i] Belum ada tim terdaftar dalam sistem.")
    else:
        for t in teams:
            print(f"[{t['id']}] {t['name']} | Deck: {t['deck']} | Waktu: {t['registered_at']}")
    input("\nTekan Enter untuk kembali...")

def menu_catat_duel():
    print_header()
    print("--- 3. CATAT REKOR DUEL / PERTANDINGAN TCG ---")
    matches = load_data(MATCH_FILE)
    p1 = input("Nama Agen / Pemain 1: ").strip()
    p2 = input("Nama Agen / Pemain 2: ").strip()
    winner = input("Pemenang (P1/P2/Draw): ").strip().upper()
    
    match_record = {
        "id": len(matches) + 1,
        "player_1": p1,
        "player_2": p2,
        "winner": winner,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    matches.append(match_record)
    save_data(MATCH_FILE, matches)
    print("\n[+] Rekor duel berhasil dicatat!")
    input("\nTekan Enter untuk kembali...")

def menu_match_history():
    print_header()
    print("--- 4. RIWAYAT DUEL (MATCH HISTORY) ---")
    matches = load_data(MATCH_FILE)
    if not matches:
        print("[i] Belum ada riwayat duel tercatat.")
    else:
        for m in matches:
            print(f"[{m['timestamp']}] {m['player_1']} vs {m['player_2']} --> Pemenang: {m['winner']}")
    input("\nTekan Enter untuk kembali...")

def menu_leaderboard():
    print_header()
    print("--- 5. STATISTIK WIN-RATE & LEADERBOARD ---")
    matches = load_data(MATCH_FILE)
    if not matches:
        print("[i] Belum cukup data untuk kalkulasi win-rate.")
    else:
        stats = {}
        for m in matches:
            p1, p2, winner = m["player_1"], m["player_2"], m["winner"]
            for p in [p1, p2]:
                if p not in stats:
                    stats[p] = {"wins": 0, "losses": 0, "draws": 0, "total": 0}
            
            stats[p1]["total"] += 1
            stats[p2]["total"] += 1
            
            if winner == "P1":
                stats[p1]["wins"] += 1
                stats[p2]["losses"] += 1
            elif winner == "P2":
                stats[p2]["wins"] += 1
                stats[p1]["losses"] += 1
            else:
                stats[p1]["draws"] += 1
                stats[p2]["draws"] += 1
        
        print(f"{'Nama Agen':<15} | {'Main':<5} | {'Menang':<6} | {'Kalah':<6} | {'Win-Rate':<8}")
        print("-" * 50)
        for player, data in stats.items():
            wr = (data["wins"] / data["total"] * 100) if data["total"] > 0 else 0
            print(f"{player:<15} | {data['total']:<5} | {data['wins']:<6} | {data['losses']:<6} | {wr:.1f}%")
    input("\nTekan Enter untuk kembali...")

def menu_pendaftaran_turnamen():
    print_header()
    print("--- 6. PENDAFTARAN PESERTA TURNAMEN ---")
    tourney = load_data(TOURNAMENT_FILE)
    name = input("Nama Peserta / Agen: ").strip()
    event = input("Kategori Turnamen (Star Chip / Season Master): ").strip()
    
    tourney.append({"name": name, "event": event, "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    save_data(TOURNAMENT_FILE, tourney)
    print(f"\n[+] Peserta {name} berhasil didaftarkan ke {event}!")
    input("\nTekan Enter untuk kembali...")

def menu_lihat_peserta():
    print_header()
    print("--- 7. LIHAT DAFTAR PESERTA TURNAMEN ---")
    tourney = load_data(TOURNAMENT_FILE)
    if not tourney:
        print("[i] Belum ada peserta terdaftar.")
    else:
        for idx, p in enumerate(tourney, 1):
            print(f"{idx}. {p['name']} - Kategori: {p['event']}")
    input("\nTekan Enter untuk kembali...")

def menu_swiss_pairing():
    print_header()
    print("--- 8. GENERATE SWISS-PAIRING & BAGAN ---")
    tourney = load_data(TOURNAMENT_FILE)
    if not tourney:
        print("[!] Daftar peserta kosong. Daftarkan peserta terlebih dahulu di menu 6.")
        input("\nTekan Enter untuk kembali...")
        return
    
    participants = [p["name"] for p in tourney]
    if len(participants) % 2 != 0:
        participants.append("--- BYE (Free Win) ---")
    
    print("Bagan Pairing Babak Ini:")
    pairings = []
    for i in range(0, len(participants), 2):
        p1 = participants[i]
        p2 = participants[i+1]
        pairing_str = f"Meja {i//2 + 1}: {p1} vs {p2}"
        print(f"  > {pairing_str}")
        pairings.append(pairing_str)
    
    archives = load_data(PAIRING_ARCHIVE)
    archives.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "pairings": pairings})
    save_data(PAIRING_ARCHIVE, archives)
    print("\n[+] Bagan Swiss-Pairing berhasil digenerate dan diarsipkan!")
    input("\nTekan Enter untuk kembali...")

def menu_arsip_pairing():
    print_header()
    print("--- 9. LIHAT ARSIP BAGAN PAIRING ---")
    archives = load_data(PAIRING_ARCHIVE)
    if not archives:
        print("[i] Belum ada arsip pairing tersimpan.")
    else:
        for arc in archives:
            print(f"\nWaktu: {arc['timestamp']}")
            for p in arc["pairings"]:
                print(f"   - {p}")
    input("\nTekan Enter untuk kembali...")

def menu_ekspor_laporan():
    print_header()
    print("--- 10. EKSPOR LAPORAN DOKUMEN (CSV & MASTER JSON) ---")
    matches = load_data(MATCH_FILE)
    if not matches:
        print("[!] Tidak ada data duel untuk diekspor.")
    else:
        csv_filename = "match_report_export.csv"
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Player 1", "Player 2", "Winner", "Timestamp"])
            for m in matches:
                writer.writerow([m["id"], m["player_1"], m["player_2"], m["winner"], m["timestamp"]])
        print(f"[+] Laporan berhasil diekspor ke file CSV: {csv_filename}")
    input("\nTekan Enter untuk kembali...")

def main():
    while True:
        print_header()
        print("1. Registrasi Tim Baru")
        print("2. Lihat Daftar Tim Aktif")
        print("3. Catat Rekor Duel / Pertandingan TCG")
        print("4. Lihat Riwayat Duel (Match History)")
        print("5. Statistik Win-Rate & Leaderboard")
        print("6. Pendaftaran Turnamen (Star Chip / Season)")
        print("7. Lihat Daftar Peserta Turnamen")
        print("8. Generate Swiss-Pairing & Bagan Turnamen")
        print("9. Lihat Arsip Bagan Pairing")
        print("10. Ekspor Laporan Dokumen (CSV & Master JSON)")
        print("11. Info Modul TCG AI (Gunakan tcg_ai_module.py)")
        print("12. Keluar")
        
        choice = input("\nPilih menu (1-12): ").strip()
        
        if choice == '1': menu_registrasi_tim()
        elif choice == '2': menu_lihat_tim()
        elif choice == '3': menu_catat_duel()
        elif choice == '4': menu_match_history()
        elif choice == '5': menu_leaderboard()
        elif choice == '6': menu_pendaftaran_turnamen()
        elif choice == '7': menu_lihat_peserta()
        elif choice == '8': menu_swiss_pairing()
        elif choice == '9': menu_arsip_pairing()
        elif choice == '10': menu_ekspor_laporan()
        elif choice == '11':
            print_header()
            print("--- MODUL TCG AI TERPISAH ---")
            print("[i] Jalankan file terpisah dengan perintah: python tcg_ai_module.py")
            input("\nTekan Enter untuk kembali...")
        elif choice == '12':
            print("\nAlhamdulillah, life is good. Sesi terminal diakhiri. Tetap semangat, ICAM!")
            break
        else:
            print("\n[!] Peringatan: Pilihan tidak valid. Silakan masukkan angka 1 sampai 12.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
