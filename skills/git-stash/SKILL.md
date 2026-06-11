---
name: git-stash
version: 0.1.0
description: Git stash'lerini listeler ve içeriğini gösterir (geçici kaydedilmiş değişiklikler).
icon: "📦"
example_prompt: "bu repoda stash'te ne var?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, stash, vcs]
---

# Git Stash Skill

Git stash'lerini (geçici olarak bir kenara konmuş değişiklikler) listeler ve
içeriğini gösterir. Bu skill **okuma** odaklıdır; uygulama/silme dikkat ister.

## Çalıştırılacak komut

**Stash listesi:**

```
git -C <dizin> stash list
```

**Belirli bir stash'in özeti / tam diff'i:**

```
git -C <dizin> stash show stash@{0}
git -C <dizin> stash show -p stash@{0}
```

`stash@{0}` en son stash'tir; listeden numarayı al.

**Değişiklikleri kenara koymak (yeni stash):**

```
git -C <dizin> stash push -m "<açıklama>"
```

> ⚠️ `stash pop`/`drop`/`clear` çalışan dizini değiştirir veya stash'i SİLER.
> Bunları kullanıcı onayı olmadan çalıştırma; önce `stash show` ile içeriği göster.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Kaç stash olduğunu ve her birinin mesajını/branch'ini listele
- `show` çıktısında hangi dosyaların değiştiğini özetle
- `pop`/`drop` gerekiyorsa önce kullanıcıdan onay iste

## Hata durumları

- **`No stash entries found`:** Stash boş; kullanıcıya bildir.
- **`not a git repository`:** Dizin Git reposu değil.
- **`pop` çakışması:** Stash uygulanırken conflict çıkabilir; `git-conflict-finder`
  ile incele.
