from players import FootballPlayer, Goalkeeper
from saveSystem import SaveSystem
import random
import time

class FootballMatch:
    def __init__(self, duration_minutes=90):
        self.duration = duration_minutes
        self.current_minute = 0
        self.team_goals = 0
        self.enemy_goals = 0
        self.team_name = "Nankatsu"
        self.enemy_name = "Ankaragücü"
        self.players = {
            "tsubasa": FootballPlayer("Tsubasa", "Forvet", ["Drive Shot", "Overhead Kick", "Basic Kick"], 100),
            "misaki": FootballPlayer("Misaki", "Orta Saha", ["Through Pass", "Shot", "World Class SHOT"], 90),
            "hyuga": FootballPlayer("Hyuga", "Forvet", ["Tiger Shot", "Raiju Shot", "Basic Kick"], 110) # Yeni oyuncu eklendi
        }
        self.goalkeeper = Goalkeeper("Wakabayashi", "Kaleci", [], 100)
        self.fan_cheering = False

    def taraftar_bagirisi(self, current_player):
        self.fan_cheering = random.random() < 0.6  # %60 ihtimalle taraftarlar bağırır
        if self.fan_cheering:
            print("📣 Taraftarlar tezahürat yapıyor! Tribünler coşmuş durumda!")
            if current_player == "tsubasa":
                print("🔥 Tsubasa'nın gol atma şansı arttı!")
            elif current_player == "misaki":
                print("⚠️ Misaki baskı altında, hata yapma ihtimali arttı!")
            elif current_player == "hyuga": # Hyuga için taraftar etkisi
                print("🐅 Hyuga'ya coşkulu destek var! Şutları daha isabetli olabilir!")

    def simulate_enemy_attack(self):
        print(f"🔴 Dakika {self.current_minute}: {self.enemy_name} atağa kalktı!")
        time.sleep(1)
        if not self.goalkeeper.save_goal():
            self.enemy_goals += 1
            SaveSystem.save_goal(self.current_minute, "Ankaragücü", self.match_id)

    def ball_possession(self):
        print(f"🟢 Dakika {self.current_minute}: Top {self.team_name} takımında!")
        for key, player in self.players.items():
            print(f"- {player.name} (stamina: {player.current_stamina}/{player.max_stamina})")

        possession_done = False
        misaki_pass_successful = False

        while not possession_done:
            choice = input("Hangi oyuncu hareket yapacak? (tsubasa / misaki / hyuga): ").strip().lower() # Oyuncu seçimi güncellendi
            if choice not in self.players:
                print("Geçersiz oyuncu seçimi.")
                continue

            self.taraftar_bagirisi(choice)

            player = self.players[choice]
            print(f"{player.name} için hareketler: {player.skills}")
            move = input(f"{player.name} hangi hareketi yapsın?: ").strip()

            scored, pass_success = player.perform_action(move)

            # Taraftar etkisi
            if self.fan_cheering:
                if choice == "tsubasa" and ("Shot" in move or "Kick" in move):
                    print("🔥 Taraftarların desteğiyle şut daha isabetli!")
                    if random.random() < 0.3:  # Ekstra %30 başarı
                        print("⚽ TARAFTAR DESTEĞİYLE GOOOOOL!")
                        self.team_goals += 1
                        player.goals += 1
                        SaveSystem.save_goal(self.current_minute, player.name, self.match_id)
                        possession_done = True
                        continue
                elif choice == "misaki" and ("Pass" in move):
                    if random.random() < 0.3:  # %30 hata şansı artar
                        print("😖 Taraftar baskısıyla Misaki topu kaptırdı!")
                        possession_done = True
                        continue
                elif choice == "hyuga" and ("Shot" in move or "Kick" in move): # Hyuga için taraftar etkisi
                    print("🐅 Hyuga'ya destek var! Şutu daha güçlü!")
                    if random.random() < 0.2: # Örneğin %20 ekstra şut başarısı
                        print("⚽ TARAFTAR DESTEĞİYLE HYUGA'DAN GOL!")
                        self.team_goals += 1
                        player.goals += 1
                        SaveSystem.save_goal(self.current_minute, player.name, self.match_id)
                        possession_done = True
                        continue

            if scored:
                self.team_goals += 1
                SaveSystem.save_goal(self.current_minute, player.name, self.match_id)
                possession_done = True
            elif pass_success and player.name == "Misaki":
                misaki_pass_successful = True
                possession_done = True
            else:
                possession_done = True

        if misaki_pass_successful:
            print("🔄 Misaki uzun oynuyor...")
            print("🔄 Misaki'nin pası başarılı! Top Tsubasa'ya doğru geliyor...")
            use_twin_shot = input("⚡ 'Twin Shot' (Ortak Şut) kullanılsın mı? (evet/hayır): ").strip().lower()
            if use_twin_shot == "evet":
                tsubasa = self.players["tsubasa"]
                misaki = self.players["misaki"]
                if tsubasa.current_stamina >= 25 and misaki.current_stamina >= 25:
                    tsubasa.current_stamina -= 25
                    misaki.current_stamina -= 25
                    print("🔥 Tsubasa ve Misaki birlikte şut çekti! Twin Shot geliyor!")
                    roll = random.randint(1, 100)
                    if roll <= 90:
                        print("⚽ Twin Shot GOOOOOL!!! Rakip kaleci çaresiz kaldı!\n")
                        self.team_goals += 1
                        tsubasa.goals += 1
                        SaveSystem.save_goal(self.current_minute, "Tsubasa & Misaki", self.match_id)
                    else:
                        print("😱 Twin Shot kaleciden döndü! İnanılmaz bir kurtarış!\n")
                else:
                    print("⚠️ Oyuncuların staminası Twin Shot için yeterli değil. Normal şut deneniyor...")
            else:
                move = input("Tsubasa hangi şutu yapsın? (Drive Shot / Overhead Kick): ").strip()
                boost = 20
                original_skills = self.players["tsubasa"].skills

                if move in original_skills:
                    print(f"Tsubasa şut çekiyor... (başarı şansı artırıldı)")
                    success_chance = random.randint(1, 100) + boost
                    if success_chance > 60:
                        print("⚽ Tsubasa GOLÜ ATTI! Muhteşem bir atak!\n")
                        self.players["tsubasa"].goals += 1
                        self.team_goals += 1
                        SaveSystem.save_goal(self.current_minute, player.name, self.match_id)

                    else:
                        print("Tsubasa'nın şutu kalecide kaldı...\n")
                else:
                    print("Tsubasa bu hareketi bilmiyor.")

    def start(self):
        self.match_id = SaveSystem.create_new_save()

        print(f"Ankara belediyesinin katkılarıyla kıtalararası dostluk maçı: 🏁 {self.team_name} vs {self.enemy_name} BAŞLADI!\n")
        while self.current_minute < self.duration:
            self.current_minute += random.randint(5, 15)
            time.sleep(0.5)

            if random.random() < 0.5:
                self.ball_possession()
            else:
                self.simulate_enemy_attack()

        print("🏁 MAÇ SONA ERDİ!\n")
        print(f"SKOR: {self.team_name} {self.team_goals} - {self.enemy_goals} {self.enemy_name}")
        if self.team_goals > self.enemy_goals:
            print("🎉 MAÇI KAZANDINIZ! Ankaragücü Başkanı Tsubasa'yı özellikle beğendiğini ve seneye Ankaragücü'nde görmek istediğini söyledi.")
        elif self.team_goals < self.enemy_goals:
            print("😢 MAÇI KAYBETTİNİZ... Ancak üzülmeyin, hepinize Sucuk Ekmek dağıtıldı.")
        else:
            print("🤝 BERABERLİK. DOSTLUK KAZANDI!")

        # Maç sonunda kayıtlı golleri göster
        show = input("\nMaç kayıtlarını görmek ister misiniz? (evet/hayır): ").strip().lower()
        if show == "evet":
            SaveSystem.show_all_matches()
            SaveSystem.export_summary()

if __name__ == "__main__":
    match = FootballMatch()
    match.start()