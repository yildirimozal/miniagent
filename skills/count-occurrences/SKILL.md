---
name: count-occurrences
version: 0.1.0
description: Bir dosyada belirli bir kelime/desenin kaç kez geçtiğini sayar.
icon: "🔎"
example_prompt: "log.txt'te 'ERROR' kaç kez geçiyor?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [grep]
  internet: false
tags: [text, count, search, file]
---

# Count Occurrences Skill

Bir dosyada bir kelimenin/desenin kaç kez geçtiğini sayar. `grep` kullanılır.

## Çalıştırılacak komut

**Eşleşen kaç SATIR var (her satırda bir veya daha fazla geçiş):**

```
grep -c '<desen>' <dosya>
```

**Toplam kaç KEZ geçiyor (aynı satırda birden fazla dahil):**

```
grep -o '<desen>' <dosya> | wc -l
```

Faydalı bayraklar: `-i` (büyük/küçük duyarsız), `-w` (tam kelime),
`-F` (deseni düz metin say, regex değil).

> Desen özel karakter (`'`, `*`, `.`) içeriyorsa tek tırnak içinde ver;
> regex değil düz arama istiyorsan `-F` ekle.

## Sonuç işleme

`bash` tool'undan gelen sayıyı kullanıcıya **doğal Türkçe** ile aktar:
- "satır sayısı" mı yoksa "toplam geçiş" mi saydığını netleştir
- İstenirse eşleşen satırları da göstermeyi öner (`grep -n`)

## Hata durumları

- **Sonuç 0:** Desen bulunamadı; yazımı, `-i` (büyük/küçük) veya `-F` (düz metin)
  ihtiyacını kontrol et.
- **Dosya bulunamadı:** Yolu teyit et.
- **Regex hatası:** Özel karakterli düz aramada `-F` kullan.
