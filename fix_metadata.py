import os
import json

# === НАСТРОЙКИ ===
GITHUB_BASE = "https://niva37-aboba.github.io/nft-host"
metadata_folder = "metadata"

for filename in os.listdir(metadata_folder):
    if not filename.endswith(".json"):
        continue

    path = os.path.join(metadata_folder, filename)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Фиксим image
    if "image" in data:
        image_path = data["image"]
        if not image_path.startswith("http"):
            data["image"] = f"{GITHUB_BASE}/{image_path}"

    # Фиксим animation_url (если есть)
    if "animation_url" in data:
        anim_path = data["animation_url"]
        if not anim_path.startswith("http"):
            data["animation_url"] = f"{GITHUB_BASE}/{anim_path}"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ All metadata updated with full GitHub URLs.")
