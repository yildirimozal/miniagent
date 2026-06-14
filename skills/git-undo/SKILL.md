---
name: git-undo
version: 0.1.0
description: Yaygın Git hatalarını güvenle geri alma rehberi (commit, add, push sonrası).
icon: "↩️"
example_prompt: "son commit'i geri al ama değişikliklerim kalsın"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, undo, reset, recovery, vcs]
---

# Git Undo Skill

"Yanlış commit attım / yanlış dosya ekledim / geri almam lazım" durumlarının
doğru komutunu seçer. Kullanıcının **ne geri almak istediğine** göre uygun
komutu uygula. Yıkıcı (geri alınamaz) işlemleri **önce göster, onay al**.

## Çalıştırılacak komut

Önce duruma bak: `git -C <dizin> status` ve `git -C <dizin> log --oneline -5`.
Sonra kullanıcının niyetine göre seç:

**Son commit'i geri al, değişiklikler KALSIN (en sık, güvenli):**

```
git -C <dizin> reset --soft HEAD~1
```

Commit çözülür, dosyalar staged kalır. Mixed istersen (`--soft` yerine
varsayılan): `git -C <dizin> reset HEAD~1` — değişiklikler korunur ama unstage olur.

**Bir dosyayı `git add`'den çıkar (unstage), içeriğe dokunma:**

```
git -C <dizin> restore --staged <dosya>
```

**ZATEN PUSH EDİLMİŞ commit'i geri al (güvenli — geçmişi bozmaz):**

```
git -C <dizin> revert <commit_hash>
```

`revert` yeni bir "geri alma commit'i" oluşturur; paylaşılan branch'lerde doğru yoldur.

**Kaybolan commit'i kurtar (çok ileri gittiysen):**

```
git -C <dizin> reflog
```

Listeden doğru hash'i bul, sonra (onayla): `git -C <dizin> reset --hard <hash>`.

> ⚠️ **YIKICI — yalnız açık onayla:**
> - `git reset --hard HEAD~1` → son commit'i **ve** kaydedilmemiş değişiklikleri **siler**.
> - `git restore <dosya>` / `git checkout -- <dosya>` → dosyadaki değişiklikleri **geri alınamaz şekilde siler**.
>
> Bunları çalıştırmadan önce ne kaybolacağını (`git status`, `git diff`) göster, kullanıcıdan **net onay** al.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Hangi işlemin yapıldığını ve **şu anki durumu** (`git status`) özetle
- Değişikliklerin korunup korunmadığını açıkça söyle
- Push edilmiş commit için **her zaman `revert`** öner (reset değil)

## Hata durumları

- **`unknown revision HEAD~1`:** Repo'da geri alınacak yeterli commit yok (ilk commit).
- **`not a git repository`:** Dizin Git reposu değil.
- **`--hard` ile veri kaybı:** Geri alınamaz; reflog ile kurtarma denenebilir
  (`git reflog` → `git reset --hard <hash>`), ama kaydedilmemiş değişiklikler dönmez.
- **Merge/rebase ortasında:** Önce `git status` ile durumu netleştir; `git merge --abort`
  / `git rebase --abort` ayrı bir geri alma yoludur.
