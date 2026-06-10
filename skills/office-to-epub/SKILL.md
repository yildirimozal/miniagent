---
name: office-to-epub
version: 0.1.0
description: Bir metin belgesini (odt, docx) LibreOffice ile EPUB e-kitaba çevirir.
icon: "📖"
example_prompt: "kitap.odt dosyasını epub yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, epub, ebook, file]
---

# Office to EPUB Skill

Bir metin belgesini (Writer `.odt`, Word `.docx`) EPUB e-kitap formatına çevirir
— e-okuyucularda (Kindle, Apple Books, Kobo) okumak için. LibreOffice 6.0+ EPUB
dışa aktarımını destekler.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to epub --outdir <çıktı_dizini> <dosya>
```

Çıktı, girdiyle aynı adlı bir `.epub` dosyasıdır.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan EPUB'ın tam yolunu belirt
- En iyi sonucun başlık stilleri (Heading 1/2…) kullanılmış belgelerde
  alındığını not düş — bölüm yapısı bu stillerden üretilir

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **`epub` filtresi tanınmadı:** LibreOffice sürümü 6.0'dan eski olabilir;
  güncelle ya da önce `office-convert` ile başka formata çevir.
- **Bölümler/içindekiler düzgün değil:** Belge başlık stilleri kullanmıyordur;
  Heading stilleri eklenince yapı düzelir.
- **`source file could not be loaded`:** Girdi yolu/format hatalı veya hesap
  tablosu/sunum verildi (EPUB yalnız metin belgeleri için anlamlı).
