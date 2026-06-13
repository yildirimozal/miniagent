---
name: repo-safety-check
version: 0.1.0
description: Commit veya PR öncesi Git reposunda secret sızıntısı, conflict marker, büyük dosya ve diff hijyeni kontrolü yapar.
icon: "🛡️"
example_prompt: "Bu repoyu commit atmadan önce güvenlik açısından kontrol et"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [git, grep, find]
  internet: false
tags: [git, security, safety, preflight, developer]
---

# Repo Safety Check Skill

Bir Git reposunda commit veya PR öncesi hızlı güvenlik ve hijyen kontrolü yap.
Amaç, yanlışlıkla gönderilecek secret, çözülmemiş conflict marker'ı, büyük
dosya veya bozuk diff gibi riskleri kullanıcıya erken göstermektir.

## Çalıştırılacak komut

`<dizin>` yerine kullanıcının belirttiği Git repo dizinini koy. Kullanıcı dizin
belirtmezse `.` (mevcut dizin) kullan.

**1. Repo ve çalışma ağacı durumunu kontrol et:**

```bash
git -C <dizin> status -sb
```

**2. Diff hijyeni ve whitespace hatalarını kontrol et:**

```bash
git -C <dizin> diff --check
git -C <dizin> diff --cached --check
```

**3. Çözülmemiş Git conflict dosyalarını bul:**

```bash
git -C <dizin> diff --name-only --diff-filter=U
```

**4. Dosyalarda unutulmuş conflict marker ara:**

```bash
grep -RIn --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=.venv --exclude-dir=venv -e '<<<<<<< ' -e '=======' -e '>>>>>>> ' <dizin>
```

**5. Staged dosyalarda riskli dosya adlarını kontrol et:**

```bash
git -C <dizin> diff --cached --name-only --diff-filter=ACMR | grep -Ei '(^|/)(\.env|\.env\..*|id_rsa|id_dsa|id_ecdsa|id_ed25519|.*\.(pem|key|p12|pfx|sqlite|db))$'
```

**6. Staged diff içinde muhtemel secret kalıpları ara:**

```bash
git -C <dizin> diff --cached --unified=0 | grep -Ein '^\+.*(api[_-]?key|secret|token|password|passwd|private[_-]?key|access[_-]?key|client[_-]?secret|bearer |BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY)'
```

**7. Staged büyük dosyaları listele:**

```bash
git -C <dizin> diff --cached --name-only --diff-filter=ACMR | while IFS= read -r f; do [ -f "<dizin>/$f" ] && find "<dizin>/$f" -prune -size +5M -print; done
```

## Sonuç işleme

Sonucu kullanıcıya doğal Türkçe ile, kısa bir kontrol raporu olarak aktar:

- **Durum:** Temiz / dikkat gerekli / kritik risk var.
- **Git durumu:** Branch ve staged/unstaged/untracked dosya özetini söyle.
- **Diff hijyeni:** `diff --check` hatalarını dosya ve satırla belirt.
- **Conflict:** Git unmerged dosyaları veya marker bulunan dosyaları listele.
- **Riskli dosyalar:** `.env`, private key, sertifika, veritabanı gibi staged
  dosyaları açıkça belirt.
- **Secret şüpheleri:** Eşleşen satırları aynen yazma. Değerleri maskele;
  sadece dosya/satır ve kalıp türünü söyle. Örnek: `config.py:12 api_key benzeri değer`.
- **Büyük dosyalar:** 5 MB üstü staged dosyaları listele; gerekirse Git LFS veya
  `.gitignore` öner.

Eğer hiçbir risk bulunmazsa: "Commit/PR öncesi temel güvenlik ve hijyen
kontrollerinde belirgin risk bulunmadı." şeklinde net bir sonuç ver.

## Güvenlik kuralları

- Secret veya token değerlerini tam olarak yazma; maskelenmiş bile olsa gereksiz
  tekrar etme.
- Bu skill yalnızca kontrol yapar; dosya silme, düzenleme, commit atma veya
  `git add` çalıştırma.
- `git diff` çıktısı çok uzunsa önce özet ver; kullanıcı isterse ilgili dosya
  için ayrıntı göster.
- Sadece staged diff secret taraması commit öncesi en önemli sinyaldir; kullanıcı
  isterse unstaged diff için de aynı kontrolü yapabileceğini söyle.

## Hata durumları

- **`not a git repository`:** Verilen dizin bir Git reposu değil.
- **`git` bulunamadı:** Git kurulu değil.
- **`grep` veya `find` bulunamadı:** Sistem araçları eksik; Linux/macOS/WSL
  ortamında çalıştırılması gerektiğini söyle.
- **Çıktı boş:** Bu her zaman hata değildir; ilgili kontrol risk bulmamış olabilir.
