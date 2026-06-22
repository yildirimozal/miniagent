---
name: keep-awake
version: 0.1.0
description: Bilgisayarı belirli bir süre veya bir komut bitene kadar uyku moduna geçmekten alıkoyar.
icon: "☕"
example_prompt: "bilgisayarı 1 saat uyutma"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [caffeinate]
  internet: false
tags: [system, power, sleep, caffeinate]
---

# Keep Awake Skill

Uzun bir indirme, derleme ya da işlem sırasında bilgisayarın uykuya geçmesini
engeller. macOS'ta yerleşik `caffeinate` kullanılır.

> ℹ️ `caffeinate` **uykuyu** engeller; zamanlı **kapanmayı (shutdown) veya kapak
> kapatınca clamshell uykusunu** her zaman yenemez. Kapak açık / güce bağlıyken
> en güvenilirdir.

## Çalıştırılacak komut

**Belirli bir süre uyutma (arka planda — terminali bloklamaz):**

```
caffeinate -dimsu -t <saniye> &
```

`<saniye>` = dakika × 60 (örn. 1 saat → `3600`). Bayraklar: `-d` ekran, `-i`
boşta-uyku, `-m` disk, `-s` sistem (güce bağlıyken), `-u` kullanıcı aktif.
`&` arka plana atar; süre dolunca kendiliğinden biter.

**Bir komut bitene kadar uyanık tut (en temiz kullanım):**

```
caffeinate -dimsu <komut>
```

Örn. `caffeinate -dimsu ./uzun-derleme.sh` — komut biter bitmez uyanık tutma da biter.

**Süresiz (elle durdurana kadar):**

```
caffeinate -dimsu &
```

Durdurmak için: `pkill -x caffeinate` (veya `kill <PID>`).

**Çalışıyor mu / kalan:** `pgrep -x caffeinate` (PID dönerse aktif).

**Linux'ta** `caffeinate` yoktur; karşılığı: `systemd-inhibit --what=idle:sleep sleep <saniye>`.

## Sonuç işleme

`bash` tool'undan gelen çıktıyı kullanıcıya aktar:
- Ne kadar süre (veya hangi komut bitene kadar) uyanık tutulacağını söyle
- Arka planda başlatıldıysa PID'i ve nasıl durduracağını (`pkill -x caffeinate`) belirt
- `-t` ile başlatıldıysa süre sonunda otomatik biteceğini hatırlat

## Hata durumları

- **`caffeinate: command not found` (Linux):** macOS'a özeldir; Linux'ta
  `systemd-inhibit ...` kullan.
- **Mac yine uyudu:** Kapak kapalı + pilde clamshell uykusu `caffeinate`'i
  yenebilir; kapağı açık tut veya güce bağla.
- **Zaten çalışan caffeinate var:** `pgrep -x caffeinate` ile kontrol et;
  gerekirse eskisini `pkill -x caffeinate` ile durdur.
