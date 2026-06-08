---
name: office-to-text
version: 0.1.0
description: Bir ofis belgesinden (docx, odt, rtf) LibreOffice ile düz metin çıkarır.
icon: "📝"
example_prompt: "rapor.docx dosyasının metnini çıkar"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [soffice]
  internet: false
tags: [libreoffice, office, text, extract, file]
---

# Office to Text Skill

Bir ofis belgesinden (Word `.docx`, Writer `.odt`, `.rtf`) düz metni çıkarır —
mevcut `pdf-text` skill'inin ofis kuzeni. grep'lemek, okumak veya başka skill'lere
beslemek için.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
soffice --headless --convert-to txt:Text --outdir <çıktı_dizini> <dosya>
```

Çıktı, girdiyle aynı adı alan bir `.txt` dosyasıdır. İçeriği hemen göstermek
için ardından:

```
cat <çıktı_dizini>/<dosya_adı>.txt
```

**`soffice` PATH'te değilse:** macOS
`/Applications/LibreOffice.app/Contents/MacOS/soffice`, Linux `libreoffice`.

## Sonuç işleme

`bash` tool'undan gelen gerçek metni kullanıcıya aktar:
- Metin uzunsa ilk birkaç paragrafı göster, sonra "tamamını ister misin?" diye sor
- Oluşan `.txt` dosyasının yolunu da belirt
- Biçimlendirme (tablo, görsel) kaybolur; sadece düz metin gelir — bunu hatırlat

## Hata durumları

- **`soffice: command not found`:** LibreOffice kurulu değil.
- **Çıktı boş:** Belge görsel/taranmış içerik olabilir (gömülü metin yok);
  OCR gerekebilir.
- **`txt:Text` filtresi tanınmadı:** Yalnız `txt` dene; bazı sürümlerde kısa ad yeterli.
- **`source file could not be loaded`:** Yol/format hatalı.
