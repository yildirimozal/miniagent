---
name: git-sync
version: 0.1.0
description: Mevcut branch'i uzak depodan güvenle günceller (fetch + fast-forward, merge karmaşası yok).
icon: "🔄"
example_prompt: "bu branch'i uzaktan güncelle"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: true
tags: [git, sync, fetch, pull, vcs]
---

# Git Sync Skill

Mevcut branch'i uzak depodaki haliyle güvenle eşitler: önce `fetch`, sonra
**yalnız fast-forward** ile günceller. Diverge (ayrışma) varsa istemeden merge
yapmaz — durur, kararı sana bırakır.

## Çalıştırılacak komut

**1. Uzak referansları güncelle (+ silinmiş branch'leri temizle):**

```
git -C <dizin> fetch --prune origin
```

**2. Mevcut branch'i fast-forward ile güncelle:**

```
git -C <dizin> pull --ff-only
```

`--ff-only`: yalnız ileri-sarma yapar; yerel commit'lerin uzaktan ayrışmışsa
**hata verir** (veri/merge sürprizi olmaz). `<dizin>` belirtilmezse `.` kullan.

**Güncelleme öncesi/sonrası ne değişti görmek için:**

```
git -C <dizin> log --oneline HEAD..@{u}
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Kaç commit ileri sarıldığını / "zaten güncel" olduğunu söyle
- `Already up to date` → değişiklik yok
- Fast-forward yapıldı → kaç yeni commit geldiğini özetle

## Hata durumları

- **`Not possible to fast-forward` / diverged:** Yerel ve uzak ayrışmış; istemeden
  birleştirme yapma. Kullanıcıya seçenek sun: `git rebase` (lineer) veya normal
  `git merge` (ikisi de onayla). `git-undo` ile geri alınabileceğini hatırlat.
- **`no tracking information`:** Branch bir upstream'e bağlı değil;
  `git push -u origin <branch>` veya `git branch --set-upstream-to=origin/<branch>`.
- **`could not resolve host` / ağ:** İnternet veya remote erişimi yok.
- **`not a git repository`:** Dizin Git reposu değil.
