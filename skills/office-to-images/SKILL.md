---
name: office-to-images
version: 0.1.0
description: Bir sunumun/belgenin her sayfasını LibreOffice + pdftoppm ile PNG görsele çevirir.
icon: "🖼️"
example_prompt: "sunum.pptx slaytlarını PNG yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice, pdftoppm]
  internet: false
tags: [libreoffice, office, image, png, slides, file]
---

# Office to Images Skill

Bir sunumun (pptx/odp) veya belgenin her sayfasını ayrı PNG görsele çevirir —
slayt önizlemesi, thumbnail veya web'de paylaşım için. Sağlam yol: önce
LibreOffice ile PDF'e, sonra `pdftoppm` ile sayfa-başına-görsel.

## Çalıştırılacak komut

`bash` tool'u ile iki adımı çalıştır:

**1. PDF'e çevir:**

```
soffice --headless --convert-to pdf --outdir <çıktı_dizini> <dosya>
```

**2. Her sayfayı PNG yap:**

```
pdftoppm -png -r 150 <çıktı_dizini>/<dosya_adı>.pdf <çıktı_dizini>/<önek>
```

`-r 150` çözünürlük (DPI); `<önek>` çıktı adı önekidir (`önek-1.png`,
`önek-2.png` …). Tek sayfa/ilk slayt yeterliyse `-f 1 -l 1` ekle.

**Alternatif (tek sayfa, sadece LibreOffice):**
`soffice --headless --convert-to png --outdir <dir> <dosya>` — yalnız **ilk
sayfayı** verir; çok sayfa için yukarıdaki PDF yolu gerekir.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Kaç görsel oluştuğunu ve dosya adı desenini (`önek-N.png`) belirt
- Çıktı dizinini söyle
- İstenen DPI farklıysa `-r` değerini ayarlamayı öner

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **`pdftoppm: command not found`:** poppler kurulu değil; macOS
  `brew install poppler`, Linux `apt install poppler-utils`.
- **Tek PNG bekledin ama çok çıktı (veya tersi):** `-f`/`-l` ile sayfa aralığı
  ver; tek sayfa için `-f 1 -l 1`.
- **`source file could not be loaded`:** Girdi yolu/format hatalı.
