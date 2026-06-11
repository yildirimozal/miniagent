---
name: verify-checksum
version: 0.1.0
description: Bir dosyayı beklenen bir sha256/md5 checksum ile karşılaştırıp bütünlüğünü doğrular.
icon: "✅"
example_prompt: "installer.dmg'in sha256'sı şu mu: abc123..."
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [shasum]
  internet: false
tags: [security, checksum, hash, verify, file]
---

# Verify Checksum Skill

Bir dosyanın checksum'unu hesaplayıp **beklenen** değerle karşılaştırır —
indirilen dosyanın bozulmadığını/değiştirilmediğini doğrulamak için.
`hash-file` ile tamamlayıcıdır (o hesaplar, bu doğrular).

## Çalıştırılacak komut

**Otomatik doğrulama (sha256) — `OK` veya `FAILED` der:**

```
echo "<beklenen_hash>  <dosya>" | shasum -a 256 -c
```

Beklenen hash ile dosya adı arasında **iki boşluk** olmalı (format katı).

**Veya hesaplayıp gözle karşılaştır:**

```
shasum -a 256 <dosya>
```

**md5 için:** `-a 256` yerine `md5` (macOS) / `md5sum` (Linux) kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- `<dosya>: OK` → **eşleşiyor**, dosya bütün. Açıkça "doğrulandı ✅" de.
- `<dosya>: FAILED` → **eşleşmiyor**. Dosya bozuk veya değiştirilmiş olabilir;
  kullanıcıyı uyar, yeniden indirmesini öner.
- Manuel modda hesaplananı beklenenle yan yana göster.

## Hata durumları

- **`shasum: command not found` (Linux):** `sha256sum` kullan
  (`echo "<hash>  <dosya>" | sha256sum -c`).
- **`no properly formatted ... lines found`:** Hash ile dosya adı arasında iki
  boşluk yok ya da satır formatı bozuk.
- **Dosya bulunamadı:** Yolu teyit et.
