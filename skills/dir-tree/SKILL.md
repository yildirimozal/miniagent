---
name: dir-tree
version: 0.1.0
description: Bir dizinin ağaç görünümünü (alt klasörler ve dosyalar) çıkarır.
icon: "🌲"
example_prompt: "~/Projeler klasörünün ağaç yapısını göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [find]
  internet: false
tags: [file, directory, tree, list]
---

# Dir Tree Skill

Bir dizinin iç içe yapısını (alt klasörler + dosyalar) ağaç biçiminde gösterir.
`tree` kuruluysa onu, değilse `find` ile bir alternatifi kullanır.

## Çalıştırılacak komut

**`tree` varsa (en okunaklı) — derinliği sınırla:**

```
tree -L <derinlik> <dizin>
```

`-L 2` ilk iki seviyeyi gösterir. Faydalı bayraklar: `-d` (sadece klasörler),
`-a` (gizli dosyalar dahil), `--gitignore` (gitignore'a uyanları atla).

**`tree` yoksa — `find` tabanlı sade ağaç:**

```
find <dizin> -maxdepth <derinlik> -print | sed -e 's;[^/]*/;|  ;g;s;|  \([^|]\);+-- \1;'
```

**Sadece klasör yapısı (find ile):**

```
find <dizin> -maxdepth <derinlik> -type d
```

> Büyük ağaçlarda çıktıyı sınırlamak için `<derinlik>` küçük tut (örn. 2-3)
> ve gerekirse `| head -50` ekle. `node_modules`/`.git` gibi klasörleri
> dışlamak için `tree -I 'node_modules|.git'` ya da
> `find ... -not -path '*/node_modules/*'`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Ağaç yapısını olduğu gibi göster (kod bloğunda)
- Çok büyükse önce klasör sayısı/derinlik özeti ver, sonra detay sun
- Hangi derinlikle sınırlandığını belirt

## Hata durumları

- **`tree: command not found`:** `find` alternatifini kullan; ya da kurmak için
  macOS `brew install tree`, Linux `sudo apt install tree`.
- **`Permission denied`:** Bazı alt dizinler okunamayabilir; `find ... 2>/dev/null`
  ile sustur.
- **Çıktı çok büyük:** `<derinlik>`'i düşür veya `| head` ile sınırla.
- **Dizin bulunamadı:** Yolu teyit et.
