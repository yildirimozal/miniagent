---
name: dedup-lines
version: 0.1.0
description: Bir dosyadaki tekrar eden satırları kaldırır (sıra korunabilir).
icon: "♻️"
example_prompt: "liste.txt'teki tekrarları temizle"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [awk]
  internet: false
tags: [text, dedup, unique, file]
---

# Dedup Lines Skill

Bir dosyadaki tekrar eden satırları kaldırır. Çıktı ekrana gelir (dosya değişmez).

## Çalıştırılacak komut

**Orijinal sırayı koruyarak (önerilen):**

```
awk '!seen[$0]++' <dosya>
```

Bu, her satırın **ilk** görülüşünü tutar, sonrakileri atar.

**Sıralayıp benzersizleştir (sıra değişir):**

```
sort -u <dosya>
```

**Kaç tekrar olduğunu da görmek için:**

```
sort <dosya> | uniq -c | sort -rn
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Benzersiz satırları göster
- Kaç satırın silindiğini söyle (orijinal − benzersiz; `wc -l` ile sayılabilir)
- Hangi yöntemin (sıra-koruyan / sıralı) kullanıldığını belirt

## Hata durumları

- **Dosya bulunamadı:** Yolu teyit et.
- **`uniq` tekrarları yakalamadı:** `uniq` yalnız **bitişik** tekrarları siler;
  önce `sort` gerekir (ya da `awk` yöntemini kullan).
