---
name: git-branch
version: 0.1.0
description: Bir Git reposundaki branch'leri listeler ve aktif branch bilgisini gösterir.
icon: "🌿"
example_prompt: "Bu repodaki branch'ler neler?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, branch, dev, info]
---

# Git Branch Skill

Bir Git reposundaki yerel ve uzak branch'leri listelemek için `git branch`
kullanılır. Tamamlayıcı skill'ler: `git-log` (commit geçmişi),
`git-status` (çalışma ağacı durumu), `git-diff` (değişiklikler).

## Çalıştırılacak komut

**Yerel branch'ler:**

```
git -C <dizin> branch -v
```

**Tüm branch'ler (uzak dahil):**

```
git -C <dizin> branch -av
```

`<dizin>` yerine kullanıcının belirttiği dizini koy. Belirtilmezse `.` kullan.

Kullanıcı sadece uzak branch'leri istiyorsa:

```
git -C <dizin> branch -rv
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- **Aktif branch'i** (`*` ile işaretli) vurgula
- Her branch'in son commit hash'i ve mesajını göster
- Yerel ve uzak branch'leri ayrı grupla (eğer `-av` kullanıldıysa)
- Toplam branch sayısını belirt

## Hata durumları

- **Git reposu değil:** "fatal: not a git repository" hatası gelirse dizinin
  bir Git deposu olmadığını söyle.
- **`git` bulunamadı:** Git CLI'nin kurulu olmadığını bildir.
- **Tek branch:** Sadece `main`/`master` varsa bunu belirt.
