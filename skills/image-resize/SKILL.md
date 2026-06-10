---
name: image-resize
version: 0.1.0
description: Bir görseli belirtilen boyuta veya yüzdeye göre yeniden boyutlandırır.
icon: "📐"
example_prompt: "foto.jpg'i 800px genişliğe küçült"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sips]
  internet: false
tags: [media, image, resize, file]
---

# Image Resize Skill

Bir görseli yeniden boyutlandırır. macOS'ta yerleşik `sips`, diğer sistemlerde
ImageMagick (`magick`/`convert`) kullanılır.

## Çalıştırılacak komut

**macOS (sips) — en uzun kenarı N piksele sığdır:**

```
sips -Z <N> <dosya>
```

`-Z` en-boy oranını korur. Sabit genişlik için: `sips --resampleWidth <N> <dosya>`.

> ⚠️ `sips` dosyayı **yerinde değiştirir**. Orijinali korumak için önce kopyala:
> `cp <dosya> <yeni>` sonra `sips -Z <N> <yeni>`.

**Linux / ImageMagick:**

```
magick <girdi> -resize <N>x <çıktı>
```

`-resize 50%` ile yüzde, `-resize 800x600` ile kutu içine sığdırma yapılır.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Yeni boyutu (genişlik×yükseklik) ve dosya yolunu belirt
- `sips` yerinde değiştirdiyse bunu hatırlat (kopya öneriyorsan söyle)

## Hata durumları

- **`sips: command not found` (Linux):** ImageMagick dene (`magick`/`convert`);
  yoksa `sudo apt install imagemagick`.
- **Dosya bulunamadı:** Yolu teyit et.
- **Desteklenmeyen format:** Girdinin geçerli bir görsel olduğundan emin ol.
