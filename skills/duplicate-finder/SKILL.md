---
name: duplicate-finder
version: 0.1.0
description: Bir klasördeki içerikçe aynı (yinelenen) dosyaları hash'e göre bulur.
icon: "👯"
example_prompt: "~/Downloads'taki aynı dosyaların kopyalarını bul"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [shasum, find]
  internet: false
tags: [file, duplicate, hash, cleanup]
---

# Duplicate Finder Skill

Bir klasördeki **içeriği birebir aynı** dosyaları bulur — isimleri farklı olsa
bile. Her dosyanın hash'i hesaplanır; aynı hash = aynı içerik. Disk temizliği
ve düzen için. Sadece **bulur**, hiçbir şey silmez.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
find <klasör> -type f -exec shasum {} + | sort | awk '$1==h{if(p){print p;p=""}print;next}{p=$0;h=$1}'
```

- `shasum` her dosyanın SHA-1'ini (40 hex karakter) hesaplar
- `sort` hash'e göre sıralar
- `awk` aynı hash'e sahip **tüm yinelenen** satırları yan yana yazdırır (BSD/macOS ve Linux'ta çalışır; `uniq -w` yalnız GNU'dadır, taşınabilir değil)

Aynı hash'e sahip satırlar gruplanır → o dosyalar birbirinin kopyasıdır.

**Büyük klasörlerde önce sadece boyutla ön-eleme** (daha hızlı, isteğe bağlı):
çok sayıda dosyada `find ... -size` ile filtrelemek mantıklı olabilir.

**Yalnız hangi hash'lerin tekrarladığını özetlemek için:**

```
find <klasör> -type f -exec shasum {} + | awk '{print $1}' | sort | uniq -d
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Yinelenen dosya **gruplarını** göster (aynı hash → aynı içerik)
- Kaç grup ve toplam kaç fazladan kopya olduğunu belirt
- **Silmeyi asla otomatik yapma**; hangi kopyanın tutulacağına kullanıcı karar verir

## Hata durumları

- **Çıktı boş:** Yinelenen dosya yok (her dosya benzersiz).
- **Çok yavaş:** Klasör çok büyük; daha dar bir alt klasörden başla veya boyut
  ön-elemesi uygula.
- **`Permission denied`:** Bazı dosyalar okunamayabilir; `find ... 2>/dev/null`
  ile sustur.
- **`shasum` yoksa (Linux):** `sha1sum` kullan (`-exec sha1sum {} +`); awk kısmı aynı kalır.
