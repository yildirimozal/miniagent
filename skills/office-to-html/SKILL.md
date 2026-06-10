---
name: office-to-html
version: 0.1.0
description: Bir ofis belgesini (docx, odt) LibreOffice ile HTML'e çevirir.
icon: "🌐"
example_prompt: "yazi.docx dosyasını HTML yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, html, web, file]
---

# Office to HTML Skill

Bir ofis belgesini (Word `.docx`, Writer `.odt`) HTML'e çevirir — web'de
yayımlamak, statik siteye gömmek veya mail gövdesi hazırlamak için.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to html --outdir <çıktı_dizini> <dosya>
```

Çıktı, girdiyle aynı adlı bir `.html` dosyasıdır. Belgede görsel varsa,
LibreOffice görselleri ayrı dosyalar olarak aynı dizine çıkarabilir.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan HTML'in tam yolunu belirt
- Görseller ayrı çıktıysa onları da hatırlat
- LibreOffice'in ürettiği HTML'in inline stil içerdiğini, modern/temiz markup
  gerekiyorsa elden geçirme gerekebileceğini not düş

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **Görseller eksik/bozuk:** Gömülü görseller dışa aktarılamamış olabilir;
  çıktı dizinini kontrol et.
- **`source file could not be loaded`:** Yol/format hatalı.
- **Profil kilidi:** GUI açıksa `-env:UserInstallation=file:///tmp/lo_html` ekle.
