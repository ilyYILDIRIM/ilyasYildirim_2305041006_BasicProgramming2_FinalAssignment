import json
import os
from datetime import datetime

class SaveSystem:
    SAVE_DIR = "saves"
    INDEX_FILE = os.path.join(SAVE_DIR, "index.json")

    @staticmethod
    def _ensure_save_dir():
        if not os.path.exists(SaveSystem.SAVE_DIR):
            os.makedirs(SaveSystem.SAVE_DIR)

    @staticmethod
    def _get_next_match_id():
        SaveSystem._ensure_save_dir()
        if not os.path.exists(SaveSystem.INDEX_FILE):
            with open(SaveSystem.INDEX_FILE, "w", encoding="utf-8") as f:
                json.dump({"last_match_id": 0}, f)

        with open(SaveSystem.INDEX_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["last_match_id"] += 1
        with open(SaveSystem.INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return data["last_match_id"]

    @staticmethod
    def _get_match_filename(match_id):
        return os.path.join(SaveSystem.SAVE_DIR, f"match_{match_id}.json")

    @staticmethod
    def create_new_save():
        match_id = SaveSystem._get_next_match_id()
        file_path = SaveSystem._get_match_filename(match_id)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({"match_id": match_id, "goals": [], "timestamp": datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)
        return match_id

    @staticmethod
    def save_goal(minute, player_name, match_id):
        file_path = SaveSystem._get_match_filename(match_id)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["goals"].append({"minute": minute, "player": player_name})

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def show_all_matches():
        SaveSystem._ensure_save_dir()
        files = sorted(f for f in os.listdir(SaveSystem.SAVE_DIR) if f.startswith("match_") and f.endswith(".json"))

        if not files:
            print("Hiç kayıtlı maç bulunamadı.")
            return

        print("\n📂 Kayıtlı Maçlar:")
        for file in files:
            with open(os.path.join(SaveSystem.SAVE_DIR, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"\n📁 Maç {data['match_id']} ({data['timestamp']}):")
                if not data["goals"]:
                    print(" - Gol yok")
                else:
                    for g in data["goals"]:
                        print(f" - {g['minute']}. dakikada {g['player']} gol attı.")
    def export_summary():
        SaveSystem._ensure_save_dir()
        files = sorted(f for f in os.listdir(SaveSystem.SAVE_DIR) if f.startswith("match_") and f.endswith(".json"))

        summary = []

        for file in files:
            with open(os.path.join(SaveSystem.SAVE_DIR, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                summary.append({
                    "match_id": data.get("match_id"),
                    "timestamp": data.get("timestamp"),
                    "total_goals": len(data.get("goals", [])),
                    "scorers": [g["player"] for g in data.get("goals", [])]
                })

        summary_path = os.path.join(SaveSystem.SAVE_DIR, "summary.json")
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"📤 Özet dosyası oluşturuldu: {summary_path}")