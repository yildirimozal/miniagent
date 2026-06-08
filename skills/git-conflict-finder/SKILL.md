---
name: git-conflict-finder
version: 0.1.0
description: Projedeki çözülmemiş Git conflict (çakışma) noktalarını bulur.
icon: "⚔️"
example_prompt: "Projede çözülmemiş git conflict var mı?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [git, grep]
  internet: false
tags: [git, developer, conflict, merge]
---

# Git Conflict Finder Skill

Git merge veya rebase sonrası projede unutulmuş veya çözülmeyi bekleyen `<<<<<<< HEAD` gibi conflict marker'larını arar.

## Yöntem

Önce Git'in kendi diff aracını kullanarak unmerged (çakışan) dosyaları bul:
```bash
git diff --name-only --diff-filter=U
```

Eğer Git merge state'inde değilse ancak kod içinde unutulmuş marker'lar olabileceğinden şüpheleniliyorsa, doğrudan grep ile arama yap:
```bash
grep -rnw . -e '<<<<<<< ' -e '=======' -e '>>>>>>> ' --exclude-dir=.git
```

## Sonuç işleme

Çakışma tespit edilen dosyaların bir listesini yap. Mümkünse hangi dosyanın hangi satırlarında çakışma olduğunu belirt.
Eğer hiçbir çakışma yoksa, "Projenizde çözülmemiş bir Git çakışması (conflict) bulunmuyor." şeklinde güven verici bir mesaj ver.
