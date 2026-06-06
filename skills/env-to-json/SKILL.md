---
name: env-to-json
version: 0.1.0
description: .env dosyası formatındaki key-value çiftlerini JSON formatına dönüştürür.
icon: "⚙️"
example_prompt: "Bu env değişkenlerini JSON'a çevir: PORT=3000\nNODE_ENV=dev"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, env_json]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [python3]
  internet: false
tags: [env, json, convert, developer]
---

# Env to JSON Skill

Kullanıcının verdiği veya bir dosyadan okunan `.env` yapılandırma metnini ayrıştırarak JSON objesine çevirir. Çoğu yapılandırma yönetimi aracıyla uyumluluk sağlamak için faydalıdır.

## Yöntem

Python kullanarak yorum (comment) satırlarını (`#`) ve boş satırları atlayan, key=value çiftlerini JSON objesine dönüştüren basit bir script çalıştır:

```bash
python3 -c '
import sys, json

env_text = sys.stdin.read()
result = {}
for line in env_text.splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if "=" in line:
        key, val = line.split("=", 1)
        # Çift veya tek tırnakları temizle
        val = val.strip()
        if (val.startswith("\"") and val.endswith("\"")) or (val.startswith("\x27") and val.endswith("\x27")):
            val = val[1:-1]
        result[key.strip()] = val

print(json.dumps(result, indent=2))
' << 'EOF'
ENV_ICERIGI_BURAYA
EOF
```

## Sonuç işleme

Oluşan JSON çıktısını formatlı olarak Markdown `json` kod bloğu içinde göster. Yorum satırlarının otomatik olarak atlandığını bilgi olarak verebilirsin.
