---
name: office-batch-pdf
version: 0.1.0
description: Bir klasördeki tüm ofis belgelerini LibreOffice ile toplu olarak PDF'e çevirir.
icon: "📚"
example_prompt: "~/Belgeler/sunumlar klasöründeki tüm dosyaları PDF yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, pdf, batch, file]
---

# Office Batch PDF Skill

Bir klasördeki birden fazla ofis belgesini tek seferde headless olarak PDF'e
çevirir. LibreOffice `--convert-to` birden çok girdi dosyasını kabul eder.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır (girdi klasöründeki tüm desteklenen dosyalar):

```
soffice --headless --convert-to pdf --outdir <çıktı_dizini> <klasör>/*.docx <klasör>/*.odt <klasör>/*.xlsx <klasör>/*.pptx
```

Yalnız belirli bir uzantı isteniyorsa tek glob bırak (örn. sadece `*.docx`).
Hiç eşleşme yoksa shell hata vermesin diye gerekiyorsa `2>/dev/null` ekle.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

**Çok sayıda dosyada profil kilidini önlemek için** izole profil kullan:
`-env:UserInstallation=file:///tmp/lo_batch`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Kaç dosyanın dönüştürüldüğünü say ve özetle
- Başarısız olan dosya varsa ayrıca belirt
- Çıktı PDF'lerin `<çıktı_dizini>`'nde olduğunu söyle

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil (kurulum için
  `office-to-pdf` skill'indeki öneriler).
- **`no such file` / glob eşleşmedi:** Klasörde o uzantıda dosya yok; mevcut
  dosyaları `ls` ile teyit et.
- **Bazı dosyalar dönüşmedi:** Bozuk veya parola korumalı olabilir; tek tek
  `office-to-pdf` ile dene.
- **Profil kilidi:** LibreOffice GUI'yi kapat ya da izole profil bayrağını kullan.
