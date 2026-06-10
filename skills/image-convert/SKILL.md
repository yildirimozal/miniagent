---
name: image-convert
version: 0.1.0
description: Bir görseli formatlar arası çevirir (png↔jpg↔webp↔heic vb.).
icon: "🖼️"
example_prompt: "foto.png'i jpg yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sips]
  internet: false
tags: [media, image, convert, format, file]
---

# Image Convert Skill

Bir görseli bir formattan diğerine çevirir (PNG, JPEG, WEBP, HEIC, TIFF, GIF).
macOS'ta `sips`, diğer sistemlerde ImageMagick kullanılır.

## Çalıştırılacak komut

**macOS (sips):**

```
sips -s format <format> <girdi> --out <çıktı>
```

`<format>`: `jpeg`, `png`, `tiff`, `gif`, `heic`. Örnek:
`sips -s format jpeg foto.png --out foto.jpg`.

**Linux / ImageMagick (uzantıdan formatı anlar):**

```
magick <girdi> <çıktı.uzantı>
```

Örn. `magick foto.png foto.webp`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan dosyanın yolunu ve yeni formatını belirt
- WEBP/HEIC gibi formatlarda dosya boyutunun belirgin düştüğünü not edebilirsin

## Hata durumları

- **`sips` WEBP yazamıyor:** Eski macOS sürümlerinde `sips` WEBP desteklemez;
  ImageMagick (`magick`) kullan.
- **`command not found` (Linux):** `sudo apt install imagemagick`.
- **Dosya bulunamadı / geçersiz görsel:** Yolu ve formatı teyit et.
