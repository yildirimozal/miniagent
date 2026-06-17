---
name: git-search
version: 0.1.0
description: Git geçmişinde kod, değişiklik veya commit mesajı arar (bir satır ne zaman geldi/gitti?).
icon: "🕵️"
example_prompt: "bu projede 'API_KEY' ifadesi ne zaman eklendi?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, search, history, pickaxe, vcs]
---

# Git Search Skill

Git geçmişinde detektiflik yapar: bir kod parçasının ne zaman **eklendiğini/
silindiğini**, hangi commit'in dokunduğunu veya bir commit mesajını bulur.
Sadece **okur**, repoyu değiştirmez.

## Çalıştırılacak komut

`<dizin>` belirtilmezse `.` kullan. Kullanıcının niyetine göre seç:

**Bir metin/kod NE ZAMAN eklendi veya silindi (pickaxe — en güçlü):**

```
git -C <dizin> log --oneline -S "<metin>"
```

Bu, o metnin geçiş **sayısını değiştiren** (ekleyen/silen) commit'leri listeler.
Belirli dosyaya daraltmak için sona ` -- <yol>` ekle. Diff'leri de görmek için
`-S "<metin>" -p`.

**Regex ile diff arama (kod deseni değişen commit'ler):**

```
git -C <dizin> log --oneline -G "<regex>"
```

**Commit MESAJLARINDA arama:**

```
git -C <dizin> log --oneline --grep "<kelime>"
```

`--grep` için büyük/küçük duyarsız: `-i` ekle. Birden çok terimi VEYA'lamak için
birden fazla `--grep` + `--all-match` (VE için).

**Belirli bir satırın tüm geçmişi (kim, ne zaman değiştirdi):**

```
git -C <dizin> log -p -L <başlangıç>,<bitiş>:<dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Bulunan commit'leri (hash + tarih + mesaj) sırala; en alakalıyı öne çıkar
- Pickaxe (`-S`) sonucunda en eski commit genelde **eklendiği**, sonrakiler
  taşındığı/silindiği yerlerdir — bunu yorumla
- Çok sonuç varsa `--oneline` özetini ver, detay istenirse `-p` ile diff göster

## Hata durumları

- **Sonuç boş:** O metin hiç commit'lenmemiş olabilir; yazımı kontrol et, `-G`
  (regex) veya `--grep` (mesaj) ile dene.
- **`not a git repository`:** Dizin Git reposu değil.
- **Çok yavaş (büyük repo):** Aramayı bir yola (` -- <yol>`) veya tarih aralığına
  (`--since`/`--until`) daralt.
- **Özel karakterli metin:** Deseni tek tırnak içinde ver; regex değil düz arama
  için `-S` (pickaxe) kullan, `-G` regex'tir.
