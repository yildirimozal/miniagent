---
name: office-to-pdf
version: 0.1.0
description: Bir ofis belgesini (docx, odt, xlsx, pptx vb.) LibreOffice ile headless PDF'e çevirir.
icon: "📄"
example_prompt: "~/Desktop/rapor.docx dosyasını PDF yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, pdf, convert, file]
---

# Office to PDF Skill

Bir ofis belgesini (Word, Writer, Excel, Calc, PowerPoint, Impress) LibreOffice'in
headless modunu kullanarak PDF'e çevirir. GUI açılmaz.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to pdf --outdir <çıktı_dizini> <dosya>
```

`<dosya>` yerine girdi belgesini, `<çıktı_dizini>` yerine PDF'in kaydedileceği
klasörü koy (genelde girdiyle aynı dizin). PDF, girdi dosyasıyla aynı adı alır.

**`soffice` PATH'te değilse:**
- macOS: `/Applications/LibreOffice.app/Contents/MacOS/soffice`
- Linux: `libreoffice` veya `soffice`

**LibreOffice zaten açıksa** profil kilidi çakışabilir; izole profil ekle:

```
soffice --headless -env:UserInstallation=file:///tmp/lo_pdf --convert-to pdf --outdir <çıktı_dizini> <dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan PDF'in tam yolunu belirt (`convert ... -> ... .pdf` satırından)
- Birden fazla dosya verildiyse her birinin sonucunu sırayla göster

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil. Öner: macOS
  `brew install --cask libreoffice`, Linux `sudo apt install libreoffice` /
  `sudo dnf install libreoffice`.
- **`source file could not be loaded`:** Dosya yolu yanlış veya format
  desteklenmiyor; yolu ve uzantıyı teyit et.
- **Profil kilidi / çıktı boş:** LibreOffice GUI açık olabilir; yukarıdaki
  `-env:UserInstallation` izole profil bayrağıyla tekrar dene.
- **Yazma izni yok:** `<çıktı_dizini>`'ne yazma izninin olmadığını bildir.
