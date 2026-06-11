---
name: git-blame
version: 0.1.0
description: Bir dosyanın her satırını kimin, hangi commit'te değiştirdiğini gösterir.
icon: "👤"
example_prompt: "agent.py'nin 50-60. satırlarını kim yazmış?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, blame, history, vcs]
---

# Git Blame Skill

Bir dosyanın her satırının son kez hangi commit ve yazar tarafından
değiştirildiğini gösterir. Hata kaynağını veya bir kararın geçmişini bulmak için.

## Çalıştırılacak komut

**Tüm dosya:**

```
git -C <dizin> blame <dosya>
```

**Belirli satır aralığı (büyük dosyalarda önerilir):**

```
git -C <dizin> blame -L <başlangıç>,<bitiş> <dosya>
```

Örn. `-L 50,60`. Daha okunaklı/özet için: `-L 50,60 --date=short`.

`<dizin>` belirtilmezse `.` kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar.
Her satır: kısa commit hash, yazar, tarih ve satır içeriği içerir.
- İlgili satırların **kim/ne zaman** değiştirdiğini özetle
- Aynı commit birden çok satırı etkilediyse onu öne çıkar

## Hata durumları

- **`no such path`:** Dosya bu repoda izlenmiyor veya yol yanlış.
- **`not a git repository`:** Dizin Git reposu değil.
- **Satır aralığı dosya boyunu aşıyor:** `-L` değerlerini dosya satır sayısına göre ayarla.
