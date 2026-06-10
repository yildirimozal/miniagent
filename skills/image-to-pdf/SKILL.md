---
name: image-to-pdf
version: 0.1.0
description: Bir veya birden fazla görseli tek bir PDF dosyasında birleştirir.
icon: "📑"
example_prompt: "tarama1.jpg ve tarama2.jpg'i tek PDF yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [magick]
  internet: false
tags: [media, image, pdf, convert, file]
---

# Image to PDF Skill

Bir veya birden fazla görseli (her biri bir sayfa olacak şekilde) tek bir PDF'te
birleştirir — taranmış sayfaları tek belgede toplamak için ideal. ImageMagick
(`magick`/`convert`) kullanılır.

## Çalıştırılacak komut

**Tek görsel:**

```
magick <görsel> <çıktı.pdf>
```

**Birden fazla görsel (sıraya dikkat — dosya adına göre sıralanır):**

```
magick <g1.jpg> <g2.jpg> <g3.jpg> <çıktı.pdf>
```

**Bir klasördeki tüm JPG'ler (ada göre sıralı):**

```
magick $(ls <klasör>/*.jpg | sort) <çıktı.pdf>
```

> Eski ImageMagick'te komut `convert <...> out.pdf` şeklindedir.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan PDF'in yolunu ve kaç sayfa/görsel içerdiğini belirt
- Sayfa sırasının dosya adı sırasına göre olduğunu hatırlat

## Hata durumları

- **`magick: command not found`:** `brew install imagemagick` /
  `sudo apt install imagemagick`.
- **`not authorized ... PDF` (ImageMagick policy):** Bazı dağıtımlar PDF yazımını
  `policy.xml` ile kısıtlar; politikayı gevşetmek gerekir ya da alternatif
  (`img2pdf`) kullanılır — kullanıcıya bunu bildir.
- **Görsel bulunamadı:** Yolları ve glob eşleşmesini teyit et.
