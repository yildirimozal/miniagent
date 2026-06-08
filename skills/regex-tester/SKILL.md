---
name: regex-tester
version: 0.1.0
description: Verilen bir metin üzerinde Regex (düzenli ifade) eşleşmelerini test eder.
icon: "🔍"
example_prompt: "Şu metinde e-posta adreslerini bul: metin..., regex: [a-z]+@[a-z]+.com"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, regex_test]
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
tags: [developer, regex, testing, text]
---

# Regex Tester Skill

Kullanıcının verdiği bir düzenli ifade (Regex) kalıbını, yine kullanıcının sağladığı hedef metin üzerinde test eder ve eşleşen kısımları gösterir.

## Yöntem

Bunu Python'un standart `re` modülü ile kolayca yapabiliriz. `bash` tool'unu kullanarak aşağıdaki gibi bir inline Python scripti çalıştır:

```bash
python3 -c '
import sys, re, json
try:
    pattern = sys.argv[1]
    text = sys.argv[2]
    matches = [{"match": m.group(), "start": m.start(), "end": m.end()} for m in re.finditer(pattern, text)]
    print(json.dumps({"success": True, "count": len(matches), "matches": matches}, indent=2))
except re.error as e:
    print(json.dumps({"success": False, "error": f"Regex Hatası: {e}"}))
' "REGEX_DESENI" "HEDEF_METİN"
```

Not: Çift tırnak kaçışlarına (escaping) çok dikkat et.

## Sonuç işleme

Dönen JSON çıktısını oku. Eğer başarı durumunda eşleşmeler varsa, eşleşen kelimeleri bir liste halinde (veya metin içindeki konumlarıyla birlikte) göster. Hata varsa (geçersiz regex gibi), hatayı Türkçe olarak kullanıcıya açıkla.
