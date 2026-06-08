---
name: json-to-csv
version: 0.1.0
description: JSON verisini CSV formatına dönüştürür veya tersini yapar.
icon: "🔄"
example_prompt: "data.json dosyasını CSV'ye çevir"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [json, csv, convert, dev, data]
---

# JSON to CSV Skill

JSON ile CSV arasında dönüşüm yapmak için `python3` kullanılır.
Tamamlayıcı skill'ler: `json-format` (JSON biçimlendirme),
`csv-preview` (CSV önizleme).

## Çalıştırılacak komut

**JSON → CSV (dosyadan):**

```
python3 -c "
import json, csv, sys
data = json.load(open('<dosya.json>'))
if isinstance(data, dict): data = [data]
if not data: print('Boş veri'); sys.exit(0)
w = csv.DictWriter(sys.stdout, fieldnames=data[0].keys())
w.writeheader()
w.writerows(data)
"
```

**CSV → JSON (dosyadan):**

```
python3 -c "
import csv, json, sys
reader = csv.DictReader(open('<dosya.csv>'))
print(json.dumps(list(reader), ensure_ascii=False, indent=2))
"
```

Kullanıcı çıktıyı dosyaya kaydetmek isterse komutun sonuna `> <çıktı>` ekle.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Dönüştürülen **satır sayısını** belirt
- Sütun (alan) isimlerini listele
- Çıktı dosyaya yazıldıysa dosya yolunu göster

## Hata durumları

- **`json.decoder.JSONDecodeError`:** JSON formatı bozuk; `json-format` skill'i
  ile doğrulamasını öner.
- **İç içe JSON:** Düz (flat) olmayan JSON nesne dizisi CSV'ye doğrudan
  dönüştürülemez; kullanıcıyı uyar.
- **Boş dosya:** Dosya boş veya geçerli veri yok; bildir.
- **`python3` bulunamadı:** Python 3 kurulu olmalı.
