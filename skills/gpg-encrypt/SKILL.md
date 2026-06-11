---
name: gpg-encrypt
version: 0.1.0
description: Bir dosyayı GPG ile şifreler (parola tabanlı simetrik veya alıcı anahtarıyla).
icon: "🔒"
example_prompt: "gizli.pdf'i parolayla şifrele"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [gpg]
  internet: false
tags: [security, encrypt, gpg, file]
---

# GPG Encrypt Skill

Bir dosyayı GPG ile şifreler. En basit yol parola tabanlı (simetrik) şifreleme;
alıcının public key'i varsa asimetrik de yapılabilir.

## Çalıştırılacak komut

**Parola ile (simetrik) — `<dosya>.gpg` üretir:**

```
gpg --symmetric --cipher-algo AES256 <dosya>
```

GPG parolayı **etkileşimli olarak** sorar (terminalde gizli giriş). Parolayı
komut satırına yazma — geçmişe/süreç listesine sızar.

**Alıcının public key'i ile (asimetrik):**

```
gpg --encrypt --recipient <alıcı@mail> <dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan `.gpg` dosyasının yolunu belirt
- Simetrik şifrelemede parolayı **güvenli sakla** uyarısı yap — kaybolursa
  dosya geri açılamaz
- Orijinal dosya hâlâ duruyor; istenirse güvenli silme (`rm`) ayrı bir adım

## Hata durumları

- **`gpg: command not found`:** macOS `brew install gnupg`, Linux
  `sudo apt install gnupg`.
- **`No such file`:** Dosya yolunu teyit et.
- **Alıcı anahtarı yok:** Asimetrik şifrelemede önce alıcının public key'i
  `gpg --import` ile eklenmeli.
