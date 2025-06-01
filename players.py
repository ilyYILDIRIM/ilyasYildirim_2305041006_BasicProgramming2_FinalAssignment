import random
import time


class FootballPlayer:
    def __init__(self, name, position, skills, stamina):
        self.name = name
        self.position = position
        self.skills = skills
        self.max_stamina = stamina
        self.current_stamina = stamina
        self.goals = 0

    def perform_action(self, skill_name):
        if skill_name not in self.skills:
            print(f"{self.name} böyle bir hareket bilmiyor!")
            return False, False

        if self.current_stamina <= 0:
            print(f"{self.name} çok yorgun, hareketi yapamıyor.")
            return False, False

        stamina_cost = 0 # Varsayılan maliyet

        # Yeteneklere göre stamina maliyetini belirle
        if skill_name == "Drive Shot":
            stamina_cost = random.randint(15, 40)
        elif skill_name == "Overhead Kick":
            stamina_cost = random.randint(30, 50)
        elif skill_name == "Basic Kick":
            stamina_cost = random.randint(10, 25)
        elif skill_name == "Through Pass":
            stamina_cost = random.randint(10, 20)
        elif skill_name == "Shot": # Misaki'nin genel şutu
            stamina_cost = random.randint(20, 35)
        elif skill_name == "World Class SHOT":
            stamina_cost = random.randint(50, 70)
        elif skill_name == "Tiger Shot": # Hyuga'nın yeni yeteneği
            stamina_cost = random.randint(40, 60)
        elif skill_name == "Raiju Shot": # Hyuga'nın daha güçlü yeteneği
            stamina_cost = random.randint(60, 80)
        else: # Diğer yetenekler için varsayılan
            stamina_cost = random.randint(15, 30)

        self.current_stamina -= stamina_cost
        success_chance = random.randint(1, 100)

        print(f"{self.name} → {skill_name} yapıyor! (Kalan stamina: {self.current_stamina}/{self.max_stamina})")

        is_goal = False
        is_pass_successful = False

        if "Shot" in skill_name or "Kick" in skill_name:
            if skill_name == "World Class SHOT":
                if success_chance > 20: # Daha yüksek başarı şansı, örneğin %80
                    print(f"⚽ O NASIL BİR GOL ÖYLE!!! {self.name} ağları DELDİ!\n")
                    self.goals += 1
                    is_goal = True
                else:
                    print(f"⚽ OLAĞANÜSTÜ BİR KURTARIŞ. KALECİNİN ELİ KOPMUŞ OLSA GEREK!")
            elif skill_name == "Tiger Shot":
                if success_chance > 40: # Nispeten yüksek başarı
                    print(f"🐅 Kaplan Şutu! {self.name} rakip kaleciyi delip geçti!\n")
                    self.goals += 1
                    is_goal = True
                else:
                    print(f"{self.name}'nin Tiger Şutu dışarı çıktı...\n")
            elif skill_name == "Raiju Shot":
                if success_chance > 70: # Daha zor ama daha etkili
                    print(f"⚡ Raikiri Şutu! Kalecinin göremeyeceği bir hızla ağlarla buluştu!\n")
                    self.goals += 1
                    is_goal = True
                else:
                    print(f"Kaleci son anda Raikiri Şutunu kurtardı!\n")
            else: # Diğer genel şutlar
                if success_chance > 60:
                    print(f"⚽ GOOOOOOL!!! {self.name} ağları havalandırdı!\n")
                    self.goals += 1
                    is_goal = True
                else:
                    print(f"{self.name}'nin şutu dışarı çıktı...\n")
        elif "Pass" in skill_name:
            if success_chance > 50:
                print(f"{self.name}'nin pası başarılı!\n")
                is_pass_successful = True
            else:
                print(f"{self.name}'nin pası rakipte kaldı!\n")
        else:
            print(f"{self.name} {skill_name} hareketini başarıyla yaptı.\n")

        return is_goal, is_pass_successful

class Goalkeeper(FootballPlayer):
    def __init__(self, name, position, skills, stamina):
        super().__init__(name, position, skills, stamina)
        self.skills = ["God Hand", "Super Catch", "With HAT"]

    def save_goal(self):
        print(f"⚠️ Ankaragücü atağa geçti! Wakabayashi'nin müdahale zamanı!")
        print(f"Hareketler: {self.skills}")
        move = input("Hangi kurtarışı yapmak istersin? ").strip()

        if move not in self.skills:
            print("⚠️ Geçersiz hareket! Wakabayashi tereddüt etti... Ankaragücü için kolay bir gol oldu.")
            return False

        if move == "God Hand":
            success_chance = 70
            stamina_cost = 20
        elif move == "Super Catch":
            success_chance = 50
            stamina_cost = 10
        elif move =="With HAT":
            success_chance = 85
            stamina_cost = 40
        if self.current_stamina < stamina_cost:
            print("Wakabayashi'nin yeterli staminası yok! Top ağlarla buluştu...\n")
            return False

        self.current_stamina -= stamina_cost
        roll = random.randint(1, 100)

        print(f"Wakabayashi → {move} kullanıyor! (Kalan stamina: {self.current_stamina}/{self.max_stamina})")
        time.sleep(1)

        if roll <= success_chance:
            print("🧤 Muhteşem bir kurtarış! Golü önledi!\n")
            return True
        else:
            print("❌ Wakabayashi kurtaramadı, GOL oldu...\n")
            return False