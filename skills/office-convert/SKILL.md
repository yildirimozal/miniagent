---
name: office-convert
version: 0.1.0
description: Ofis belgelerini formatlar arası dönüştürür (docx↔odt, xlsx↔ods, pptx↔odp vb.) LibreOffice ile.
icon: "🔄"
example_prompt: "rapor.docx dosyasını odt formatına çevir"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, convert, format, file]
---

# Office Convert Skill

Ofis belgelerini bir formattan diğerine çevirmek için LibreOffice headless
kullanır. Genel dönüştürücü: Writer (docx/odt/rtf/txt), Calc (xlsx/ods/csv),
Impress (pptx/odp) formatları arası geçiş.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to <hedef_format> --outdir <çıktı_dizini> <dosya>
```

`<hedef_format>` örnekleri: `odt`, `docx`, `rtf`, `ods`, `xlsx`, `odp`, `pptx`,
`pdf`, `html`, `txt`.

Filtre belirsizse tam filtre adı gerekebilir (örn. xlsx için
`xlsx:Calc MS Excel 2007 XML`). Önce kısa adı dene.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan dosyanın tam yolunu ve yeni formatını belirt
- Kaynak ve hedef format farkını kısaca özetle (örn. "docx → odt")

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil (kurulum
  `office-to-pdf` skill'inde).
- **Beklenen çıktı oluşmadı:** Hedef format adı yanlış olabilir; tam LibreOffice
  filtre adını kullan.
- **`source file could not be loaded`:** Girdi yolu/format hatalı.
- **Profil kilidi:** GUI açıksa `-env:UserInstallation=file:///tmp/lo_conv` ekle.
