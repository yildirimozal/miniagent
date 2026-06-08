---
name: file-compare
version: 0.1.0
description: İki dosyayı karşılaştırıp aralarındaki farkları gösterir (diff).
icon: "⚖️"
example_prompt: "config.txt ile config.bak arasındaki farkları göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [diff]
  internet: false
tags: [file, compare, diff, text]
---

# File Compare Skill

İki dosya arasındaki farkları görmek için `diff` kullanılır.
Tamamlayıcı skill'ler: `file-find` (dosya arama), `hash-file`
(checksum karşılaştırma), `wc-stats` (satır sayısı).

## Çalıştırılacak komut

**Satır bazlı karşılaştırma (unified format):**

```
diff -u <dosya1> <dosya2>
```

**Yan yana karşılaştırma:**

```
diff -y --width=120 <dosya1> <dosya2>
```

**Sadece farklı olup olmadığını kontrol et:**

```
diff -q <dosya1> <dosya2>
```

Kullanıcı detay istemezse `-u` (unified) formatı kullan — en okunabilir olan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Eklenen satırları (`+` ile başlayan) ve silinen satırları (`-` ile başlayan)
  ayrı belirt
- Toplam **eklenen/silinen/değişen satır sayısını** özetle
- Dosyalar aynıysa bunu açıkça söyle
- Çok uzun diff çıktısında özet sun, kritik farkları vurgula

## Hata durumları

- **Dosya bulunamadı:** Bir veya her iki dosya mevcut değil; yolları kontrol ettir.
- **Binary dosya:** `diff` binary dosyalar için "Binary files differ" der;
  `hash-file` skill'ini öner.
- **Boş çıktı:** Dosyalar tamamen aynı — bunu belirt.
- **`diff` bulunamadı:** Hemen her sistemde yerleşik.
