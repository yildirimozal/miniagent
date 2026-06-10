---
name: csv-to-xlsx
version: 0.1.0
description: Bir CSV dosyasını LibreOffice ile Excel (xlsx) veya Calc (ods) tablosuna çevirir.
icon: "📈"
example_prompt: "veriler.csv dosyasını xlsx yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, csv, spreadsheet, xlsx, file]
---

# CSV to XLSX Skill

Ham bir CSV dosyasını sunulabilir bir hesap tablosuna (`.xlsx` veya `.ods`)
çevirir — `spreadsheet-to-csv`'nin ters yönü.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

**xlsx (Excel) için:**

```
soffice --headless --convert-to xlsx --outdir <çıktı_dizini> <dosya.csv>
```

**ods (LibreOffice Calc) için:**

```
soffice --headless --convert-to ods --outdir <çıktı_dizini> <dosya.csv>
```

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan tablo dosyasının tam yolunu ve formatını belirt
- CSV'deki sütunların düzgün ayrıştığını varsay; karmaşık/alıntılı CSV'de
  hücre kayması olursa kullanıcıya kontrol etmesini öner

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **Sütunlar tek hücrede toplandı:** CSV ayracı virgül değil (örn. `;` veya
  tab); LibreOffice'in ayraç algısı şaşmış olabilir. Tam filtre adıyla ayraç
  belirtmek gerekebilir.
- **Türkçe karakter bozulması:** Girdi CSV'nin UTF-8 olduğundan emin ol.
- **`source file could not be loaded`:** Yol hatalı veya dosya CSV değil.
