---
name: image-compress
version: 0.1.0
description: Bir görselin dosya boyutunu kaliteyi ayarlayarak küçültür.
icon: "🗜️"
example_prompt: "banner.jpg'i sıkıştır, boyutu küçülsün"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sips]
  internet: false
tags: [media, image, compress, optimize, file]
---

# Image Compress Skill

Bir görselin dosya boyutunu JPEG kalite seviyesini düşürerek küçültür.
macOS'ta `sips`, diğer sistemlerde ImageMagick kullanılır.

## Çalıştırılacak komut

**macOS (sips) — JPEG kalite (düşük = daha küçük dosya):**

```
sips -s format jpeg -s formatOptions <kalite> <girdi> --out <çıktı.jpg>
```

`<kalite>`: `low`, `normal`, `high`, `best` ya da 0-100 arası bir sayı.

**Linux / ImageMagick:**

```
magick <girdi> -quality <0-100> <çıktı>
```

`-quality 75` iyi bir denge noktasıdır.

İşlem öncesi/sonrası boyutu karşılaştırmak için:
`ls -lh <girdi> <çıktı>`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Eski ve yeni dosya boyutunu karşılaştır (`ls -lh` ile)
- Ne kadar küçülme sağlandığını yüzde olarak söyle
- Çok agresif sıkıştırmada görünür kalite kaybı olabileceğini hatırlat

## Hata durumları

- **`command not found` (Linux):** `sudo apt install imagemagick`.
- **PNG'de kalite işe yaramadı:** PNG kayıpsızdır; gerçek küçülme için JPEG/WEBP'e
  çevir (`image-convert`).
- **Dosya bulunamadı:** Yolu teyit et.
