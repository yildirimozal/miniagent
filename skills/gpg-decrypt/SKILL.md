---
name: gpg-decrypt
version: 0.1.0
description: GPG ile şifrelenmiş bir dosyayı (.gpg/.asc) çözer.
icon: "🔓"
example_prompt: "gizli.pdf.gpg'i çöz"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [gpg]
  internet: false
tags: [security, decrypt, gpg, file]
---

# GPG Decrypt Skill

GPG ile şifrelenmiş bir dosyayı (`.gpg` veya ASCII-armored `.asc`) çözer. GPG,
simetrik parolayı veya gizli anahtar parolanı etkileşimli sorar.

## Çalıştırılacak komut

**Belirli bir dosyaya çöz:**

```
gpg --output <çıktı> --decrypt <dosya.gpg>
```

**Otomatik (çıktı adı genelde `.gpg` uzantısı atılarak):**

```
gpg --decrypt-files <dosya.gpg>
```

GPG parolayı **etkileşimli** sorar; parolayı komut satırına yazma.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Çözülen dosyanın yolunu belirt
- `gpg: Good signature` / imza bilgisi geldiyse aktarabilirsin (asimetrik durumda)

## Hata durumları

- **`gpg: command not found`:** `brew install gnupg` / `apt install gnupg`.
- **`decryption failed: Bad session key`:** Yanlış parola veya uygun gizli
  anahtar yok.
- **`no secret key`:** Asimetrik şifreliyse karşılık gelen private key bu
  makinede yok.
- **Dosya bulunamadı:** Yolu teyit et.
