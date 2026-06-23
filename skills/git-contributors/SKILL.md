---
name: git-contributors
version: 0.1.0
description: Bir Git reposundaki katkıcıları commit sayısına göre sıralı listeler.
icon: "👥"
example_prompt: "bu repoya kim ne kadar katkı vermiş?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, contributors, stats, vcs]
---

# Git Contributors Skill

Bir repodaki katkıcıları, commit sayılarına göre sıralı şekilde listeler —
"kim ne kadar emek vermiş?" sorusunun hızlı cevabı. Sadece **okur**.

## Çalıştırılacak komut

**Commit sayısına göre sıralı katkıcılar:**

```
git -C <dizin> shortlog -sn --no-merges HEAD
```

> ⚠️ Sondaki `HEAD` şart: `git shortlog` interaktif olmayan (pipe/agent) ortamda onsuz **stdin'den okur ve boş döner**. Bir revizyon (`HEAD`) vermek bunu çözer.

- `-s` özet (her kişi için sadece sayı), `-n` çoktan aza sırala,
  `--no-merges` merge commit'lerini sayma. `<dizin>` boşsa `.`.

**E-posta de göster:**

```
git -C <dizin> shortlog -sne --no-merges HEAD
```

**Tüm branch'ler dahil:** sona `--all` ekle.

**Belirli bir dönem (örn. son 1 ay):**

```
git -C <dizin> shortlog -sn --no-merges --since="1 month ago" HEAD
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Katkıcıları commit sayısıyla, çoktan aza sıralı sun
- En aktif 3-5 kişiyi öne çıkar; toplam katkıcı sayısını belirt
- Aynı kişi farklı isim/mail ile görünebilir (`.mailmap` yoksa); birden çok
  satırda aynı kişi varsa bunu not et

## Hata durumları

- **`not a git repository`:** Dizin Git reposu değil.
- **Boş çıktı:** Komuta `HEAD` eklemeyi unuttuysan `shortlog` stdin bekliyordur (en sık sebep); ya da repo'da hiç commit yok.
- **Aynı kişi birden çok kez:** Farklı isim/e-posta kullanımı; doğru birleştirme
  için repo'da bir `.mailmap` dosyası gerekir.
