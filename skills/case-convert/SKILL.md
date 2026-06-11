---
name: case-convert
version: 0.1.0
description: Bir metni büyük/küçük/başlık (Title) harfe çevirir.
icon: "🔤"
example_prompt: "şu metni büyük harf yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [tr]
  internet: false
tags: [text, case, transform]
---

# Case Convert Skill

Bir metnin harf büyüklüğünü değiştirir: tümü büyük, tümü küçük veya Her
Kelimenin Baş Harfi Büyük (Title Case).

> ⚠️ Metni komut satırına gömmek shell tırnak sorunları doğurur. Uzun/özel
> karakterli metin için dosyaya kaydedip oradan oku.

## Çalıştırılacak komut

Metin bir dosyada (`~/in.txt`) ise:

**Büyük harf:**

```
tr '[:lower:]' '[:upper:]' < <dosya>
```

**Küçük harf:**

```
tr '[:upper:]' '[:lower:]' < <dosya>
```

**Title Case (her kelimenin baş harfi büyük) — Python:**

```
python3 -c 'import sys; print(open(sys.argv[1]).read().title())' <dosya>
```

> Not: `tr` ASCII odaklıdır; Türkçe karakterlerde (İ/ı, Ğ, Ş) beklenmedik
> sonuç verebilir. Türkçe-doğru dönüşüm için Python'un `.upper()/.lower()`
> ve locale'i daha güvenilirdir.

## Sonuç işleme

`bash` tool'undan gelen dönüştürülmüş metni kullanıcıya aktar; hangi dönüşümün
uygulandığını belirt.

## Hata durumları

- **Türkçe karakter bozulması:** `tr` yerine Python kullan (`.upper()`/`.lower()`).
- **Dosya bulunamadı:** Yolu teyit et.
- **`python3` yok (Title için):** Python 3 kur.
