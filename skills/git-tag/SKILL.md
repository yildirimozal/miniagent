---
name: git-tag
version: 0.1.0
description: Git tag'lerini listeler veya yeni bir tag (sürüm etiketi) oluşturur.
icon: "🏷️"
example_prompt: "bu repodaki tag'leri göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, tag, release, vcs]
---

# Git Tag Skill

Git tag'lerini (genelde sürüm işaretleri, örn. `v1.0`) listeler veya yeni tag
oluşturur.

## Çalıştırılacak komut

**Tüm tag'leri listele:**

```
git -C <dizin> tag --sort=-v:refname
```

`--sort=-v:refname` sürümleri büyükten küçüğe sıralar. Desen için:
`git -C <dizin> tag -l "v1.*"`.

**Bir tag'in işaret ettiği commit'i gör:**

```
git -C <dizin> show <tag> --stat
```

**Yeni annotated tag oluştur (önerilen — yazar+tarih+mesaj tutar):**

```
git -C <dizin> tag -a <tag_adı> -m "<mesaj>"
```

> Tag oluşturmak repoyu değiştirir; uzak depoya gitmesi için ayrıca
> `git push origin <tag_adı>` gerekir (bunu kullanıcı onayıyla yap).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Tag listesini düzenli göster; en güncel sürümü öne çıkar
- Yeni tag oluşturulduysa adını ve işaret ettiği commit'i belirt
- Push gerekiyorsa hatırlat (tag'ler otomatik push edilmez)

## Hata durumları

- **`not a git repository`:** Dizin Git reposu değil.
- **`tag already exists`:** Aynı adlı tag var; farklı ad seç veya `-f` (dikkatle).
- **Tag yok (boş çıktı):** Repoda hiç tag tanımlanmamış.
