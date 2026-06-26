---
name: git-whoami
version: 0.1.0
description: Bu repoda commit'lerin hangi isim ve e-posta ile atılacağını gösterir.
icon: "🪪"
example_prompt: "bu repoda hangi mail ile commit atıyorum?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, identity, config, vcs]
---

# Git Whoami Skill

Bu repoda atacağın commit'lerin hangi **isim** ve **e-posta** ile etiketleneceğini
gösterir — yanlış (örn. kişisel/iş) kimlikle ya da istemediğin bir mail ile commit
atmadan önce kontrol etmek için.

## Çalıştırılacak komut

**Etkin isim ve e-posta (yerel ayar globali ezer):**

```
git -C <dizin> config user.name && git -C <dizin> config user.email
```

`<dizin>` belirtilmezse `.`.

**Ayar nereden geliyor (yerel mi global mi):**

```
git -C <dizin> config --show-origin user.email
```

Çıktıdaki yol `.git/config` ise repoya özel; `~/.gitconfig` ise global.

**Değiştirmek gerekirse (yalnız bu repo için):**

```
git -C <dizin> config user.email "<yeni@mail>"
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Etkin isim + e-posta'yı net göster
- Ayarın **yerel mi global mi** olduğunu belirt (global ise tüm repoları etkiler)
- Mail yanlış/istenmeyense (örn. kişisel mail) bu repo için nasıl değiştirileceğini söyle

## Hata durumları

- **Boş çıktı:** `user.name`/`user.email` hiç ayarlı değil; commit atılamaz.
  `git config user.email "..."` ile ayarla.
- **`not a git repository`:** Dizin Git reposu değil.
- **Beklenmedik mail:** Global ayar devrede olabilir; repoya özel `git config`
  (global `--global` olmadan) ile bu repo için ayrı kimlik tanımla.
