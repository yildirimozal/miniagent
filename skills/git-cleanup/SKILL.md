---
name: git-cleanup
version: 0.1.0
description: Ana branch'e merge edilmiş yerel branch'leri bulup onaylı şekilde toplu siler.
icon: "🧹"
example_prompt: "merge olmuş eski branch'leri temizle"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, cleanup, branch, vcs]
---

# Git Cleanup Skill

İşi biten, merge edilmiş yerel branch'leri toplu temizler — repo'da birikmiş
ölü branch yığınını dağıtır. **Önce silinecekleri göster, onay al, sonra sil.**

## Çalıştırılacak komut

`git branch --merged` **bulunduğun branch'e** göre çalışır. O yüzden önce ana
branch'e geç (genelde `main`):

```
git -C <dizin> checkout main && git -C <dizin> pull --ff-only
```

**1. Silinecekleri ÖNCE göster (silme):**

```
git -C <dizin> branch --merged | grep -vE '^[*+]|^\s*(main|master|develop)$'
```

Bu; aktif branch'i ve `main`/`master`/`develop`'ı hariç tutar. Listeyi
kullanıcıya göster ve **onay iste**.

**2. Onaydan sonra — sil (`-d` güvenli: merge OLMAYANI silmez):**

```
git -C <dizin> branch --merged | grep -vE '^[*+]|^\s*(main|master|develop)$' | xargs -r git -C <dizin> branch -d
```

**Bonus — uzaktaki silinmiş branch'lerin yerel referanslarını temizle:**

```
git -C <dizin> fetch --prune
```

> ⚠️ `-d` yerine `-D` **merge edilmemiş** branch'leri de siler (iş kaybı).
> `-D`'yi yalnız kullanıcı bilerek isterse ve açık onayla kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Kaç branch'in silindiğini ve adlarını söyle
- Hangi ana branch'e göre "merged" sayıldığını belirt (önemli: HEAD'e göre)
- `-d`'nin merge edilmemiş branch'leri koruduğunu (silmediğini) hatırlat

## Hata durumları

- **Hiç branch silinmedi:** Temizlenecek merged branch yok ya da yanlış ana
  branch'tesin; doğru branch'e (`main`) geçip tekrar dene.
- **`branch -d` reddetti (`not fully merged`):** O branch HEAD'e merge edilmemiş;
  gerçekten silinecekse kullanıcı onayıyla `-D` kullan.
- **`not a git repository`:** Dizin Git reposu değil.
- **Aktif branch'i silemezsin:** Üstünde durduğun branch silinemez; önce başka
  branch'e geç.
