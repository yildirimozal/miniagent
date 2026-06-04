---
name: memory-usage
version: 0.1.0
description: Sistemin RAM kullanım detayını gösterir (toplam, kullanılan, boş, swap).
icon: "🧠"
example_prompt: "RAM'im ne durumda?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, system_info]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [vm_stat, sysctl]
  internet: false
tags: [memory, ram, system, monitoring]
---

# Memory Usage Skill

Sistemin bellek (RAM) kullanım detayını görmek için platforma göre uygun
komutlar kullanılır. Tamamlayıcı skill'ler: `cpu-stats` (CPU yükü),
`process-top` (en aktif süreçler), `system-info` (genel sistem bilgisi).

## Çalıştırılacak komut

**macOS:**

```
echo "=== Memory ===" && vm_stat && echo "=== Total RAM ===" && sysctl -n hw.memsize && echo "=== Swap ===" && sysctl vm.swapusage
```

**Linux:**

```
free -h
```

Önce `free -h` dene. Komut bulunamazsa macOS komutlarını kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:

**macOS için** (`vm_stat` çıktısı):
- `Pages active` × sayfa boyutu (genelde 16384 byte) = aktif bellek
- `Pages free` × sayfa boyutu = boş bellek
- Toplam RAM'i `hw.memsize`'dan GB olarak hesapla
- Swap kullanımını göster
- Kullanım yüzdesini hesapla

**Linux için** (`free -h` çıktısı):
- Toplam, kullanılan, boş ve önbellek (buff/cache) değerlerini göster
- Swap durumunu belirt
- Kullanım yüzdesini hesapla

Her iki durumda da kullanımın yüksek olup olmadığını yorumla (%80+ uyarı).

## Hata durumları

- **`vm_stat` bulunamadı:** macOS'ta yerleşik olmalı; Linux'ta `free` kullan.
- **`free` bulunamadı:** macOS'ta yoktur; `vm_stat` kullan.
- **Swap yüksek:** Fiziksel RAM yetersiz olabilir; uyar.
