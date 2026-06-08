---
name: spreadsheet-to-csv
version: 0.1.0
description: Bir hesap tablosunu (xlsx, ods, xls) LibreOffice ile CSV'ye çevirir.
icon: "📊"
example_prompt: "veriler.xlsx dosyasını CSV'ye çevir"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, spreadsheet, csv, data, file]
---

# Spreadsheet to CSV Skill

Bir hesap tablosunu (Excel `.xlsx`, LibreOffice Calc `.ods`, eski `.xls`)
headless olarak CSV'ye çevirir — veriyi script'lere veya `csv-preview` /
`json-to-csv` gibi skill'lere beslemek için ideal.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to csv --outdir <çıktı_dizini> <dosya>
```

Çıktı, girdiyle aynı adı alır, `.csv` uzantılı olur.

**Birden fazla sayfa (sheet) varsa:** LibreOffice varsayılan olarak yalnız
**ilk sayfayı** dışa aktarır. Tüm sayfalar gerekiyorsa kullanıcıyı uyar; her
sayfa ayrı CSV için daha gelişmiş filtre/makro gerekir.

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan CSV'nin tam yolunu belirt
- Yalnız ilk sayfanın aktarıldığını (çok sayfalıysa) hatırlat
- İstenirse `csv-preview` ile ilk satırları göstermeyi öner

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **Türkçe karakter/ayraç sorunu:** Varsayılan ayraç virgül, kodlama UTF-8;
  farklı ayraç gerekiyorsa tam filtre adıyla
  (`csv:Text - txt - csv (StarCalc)`) seçenekler verilebilir.
- **Çok sayfalı dosyada eksik veri:** Yalnız ilk sayfa aktarılmıştır.
- **`source file could not be loaded`:** Yol/format hatalı veya dosya bozuk.
