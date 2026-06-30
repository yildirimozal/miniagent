---
name: extract-links
version: 0.1.0
description: Bir dosyadan (veya HTML/metinden) tüm URL'leri çıkarıp benzersiz liste halinde verir.
icon: "🔗"
example_prompt: "rapor.md içindeki tüm linkleri çıkar"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [grep]
  internet: false
tags: [text, url, links, extract]
---

# Extract Links Skill

Bir dosyadaki (Markdown, HTML, log, düz metin) tüm `http`/`https` bağlantılarını
bulup **benzersiz** bir liste olarak çıkarır. Dosyayı okur, ağa çıkmaz.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
grep -oE 'https?://[^[:space:]"'\''<>)]+' <dosya> | sort -u
```

- `-o` yalnız eşleşen kısmı (tüm satırı değil) yazar
- `-E` genişletilmiş regex; desen `http://` veya `https://` ile başlayıp
  boşluk/tırnak/`<>`/`)` görene kadar sürer (Markdown ve HTML'de güvenli sınırlar)
- `sort -u` tekrarları eler, alfabetik sıralar

**Sadece benzersiz domain'leri çıkarmak için:**

```
grep -oE 'https?://[^/[:space:]"'\''<>)]+' <dosya> | sort -u
```

**Birden fazla dosyada:** `<dosya>` yerine `<klasör>/*.md` ya da
`-r <klasör>` (recursive).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Bulunan benzersiz link sayısını belirt, listeyi düzenli sun
- Çok sayıda link varsa domain'e göre gruplayabilir veya ilk N tanesini gösterip
  devamını özetleyebilirsin
- Not: linkin **geçerli/erişilebilir** olup olmadığını kontrol etmez; bunun için
  `api-health-check` veya `expand-url` kullanılabilir

## Hata durumları

- **Çıktı boş:** Dosyada `http(s)://` ile başlayan link yok; `www.` veya şemasız
  linkler bu desene uymaz (gerekirse deseni genişlet).
- **Dosya bulunamadı:** Yolu teyit et.
- **Linkin sonuna fazladan karakter takılıyor:** Markdown'da `](...)` veya
  cümle sonu noktası; sınır sınıfını (`[^...]`) ihtiyaca göre ayarla.
