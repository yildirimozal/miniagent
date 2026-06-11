---
name: epoch-convert
version: 0.1.0
description: Unix timestamp ile insan-okunur tarih arasında çevirir.
icon: "⏱️"
example_prompt: "1700000000 timestamp'i hangi tarih?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [date]
  internet: false
tags: [time, date, epoch, timestamp]
---

# Epoch Convert Skill

Unix timestamp (epoch — 1970'ten beri geçen saniye) ile okunabilir tarih
arasında dönüşüm yapar. macOS (BSD) ve Linux (GNU) `date` sözdizimi farklıdır.

## Çalıştırılacak komut

**Timestamp → tarih:**
- macOS: `date -r <epoch>`
- Linux: `date -d @<epoch>`

Belirli format: sonuna `+"%Y-%m-%d %H:%M:%S"` ekle.

**Tarih → timestamp:**
- macOS: `date -j -f "%Y-%m-%d %H:%M:%S" "<tarih>" +%s`
- Linux: `date -d "<tarih>" +%s`

**Şu anki timestamp:**

```
date +%s
```

Önce macOS varyantını dene; `illegal option`/`invalid` dönerse Linux'a geç.

## Sonuç işleme

`bash` tool'undan gelen sonucu kullanıcıya **doğal Türkçe** ile aktar:
- Dönüşümün yönünü belirt (timestamp→tarih veya tersi)
- Sonucun **yerel saat diliminde** olduğunu hatırlat; UTC istenirse macOS'ta
  `TZ=UTC date -r ...`, Linux'ta `date -u -d @...`

## Hata durumları

- **`illegal option -- r`:** GNU date kullanıyorsun (Linux); `-d @<epoch>` dene.
- **`invalid date`:** Tarih dizesi formatı yanlış; `%Y-%m-%d %H:%M:%S` biçimine uy.
- **Milisaniye timestamp:** 13 haneliyse milisaniyedir; saniyeye çevir (÷1000).
