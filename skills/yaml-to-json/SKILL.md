---
name: yaml-to-json
version: 0.1.0
description: YAML formatındaki metni JSON formatına çevirir.
icon: "🔄"
example_prompt: "Bu YAML'ı JSON yap: ..."
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
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
tags: [yaml, json, convert, format]
---

# YAML to JSON Skill

Kullanıcının sağladığı YAML içeriğini ayrıştırıp JSON formatına dönüştürür.

## Yöntem

Python'un `yaml` (PyYAML) ve `json` modüllerini kullanarak dönüştürme işlemini yap. (Sistemde PyYAML yüklü değilse, basit sözlük işlemlerine veya standart `json` modülüne alternatif komutlarla, örneğin `yq` yüklüyse, onu kullanarak dönüştürebilirsin.)

Eğer Python ve `yaml` modülü varsa:
```bash
python3 -c 'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read()), indent=2))' << 'EOF'
[YAM_İÇERİĞİ]
EOF
```

## Sonuç işleme

Dönüştürülen JSON çıktısını Markdown kod bloğu (`json`) içinde formatlı (indentation ile) şekilde kullanıcıya sun.
Eğer YAML parse hatası alınırsa, hatayı yakalayıp kullanıcıya hangi satırda/kısımda sözdizimi (syntax) hatası olduğunu anlaşılır bir dille söyle.
