---
name: strip-exif
version: 0.1.0
description: Bir fotoğraftan EXIF/metadata'yı (konum, kamera, tarih) siler — paylaşmadan önce mahremiyet için.
icon: "📷"
example_prompt: "tatil.jpg'i paylaşmadan önce içindeki konum bilgisini temizle"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [exiftool]
  internet: false
tags: [security, privacy, exif, metadata, image]
---

# Strip EXIF Skill

Bir fotoğrafın gömülü metadata'sını (GPS **konumu**, kamera modeli, çekim
tarihi, yazılım) siler. Telefon fotoğrafları çoğu zaman **tam koordinat**
taşır — internette paylaşmadan önce temizlemek mahremiyet açısından önemlidir.

> ⚠️ Orijinali korumak için **bir kopya üzerinde** çalış. `exiftool` varsayılan
> olarak `<dosya>_original` yedeği bırakır; aşağıdaki yöntemler bunu yönetir.

## Çalıştırılacak komut

**exiftool ile (en kapsamlı) — tüm metadata'yı sil, orijinali `_original` olarak yedekle:**

```
exiftool -all= <dosya>
```

**Yedek bırakmadan, doğrudan üzerine yaz** (orijinali önceden kopyaladıysan):

```
exiftool -all= -overwrite_original <dosya>
```

**Sadece GPS/konum'u sil (geri kalan metadata kalsın):**

```
exiftool -gps:all= <dosya>
```

**exiftool yoksa — ImageMagick ile temiz kopya:**

```
magick <girdi> -strip <çıktı>
```

**Temizlendi mi doğrula** (metadata kalmamalı):

```
exiftool <dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Hangi dosyanın temizlendiğini ve yedek (`_original`) durumunu söyle
- Özellikle **GPS/konum** alanının kaldırıldığını vurgula (asıl mahremiyet riski)
- İsterse `exiftool <dosya>` ile sonucu doğrulamayı öner

## Hata durumları

- **`exiftool: command not found`:** macOS `brew install exiftool`, Linux
  `sudo apt install libimage-exiftool-perl`; ya da `magick ... -strip` alternatifi.
- **Dosya bulunamadı / desteklenmeyen format:** Yolu ve görselin geçerliliğini teyit et.
- **Metadata hâlâ var:** Bazı formatlar (HEIC) ek bayrak isteyebilir; `-all=` çıktısını
  kontrol et veya ImageMagick ile yeniden dene.
