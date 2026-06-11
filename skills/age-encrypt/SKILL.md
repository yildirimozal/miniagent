---
name: age-encrypt
version: 0.1.0
description: Bir dosyayı age ile şifreler/çözer (modern, basit dosya şifreleme).
icon: "🛡️"
example_prompt: "notlar.txt'i age ile parolayla şifrele"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [age]
  internet: false
tags: [security, encrypt, age, file]
---

# Age Encrypt Skill

Bir dosyayı `age` ile şifreler veya çözer. `age` modern, sade bir dosya
şifreleme aracıdır (GPG'ye hafif alternatif).

## Çalıştırılacak komut

**Parola ile şifrele:**

```
age --passphrase --output <çıktı.age> <dosya>
```

`age` parolayı **etkileşimli** sorar; komut satırına yazma.

**Çöz:**

```
age --decrypt --output <çıktı> <dosya.age>
```

**Alıcı public key'i ile (asimetrik):**

```
age --recipient <age1...> --output <çıktı.age> <dosya>
```

Anahtar çifti üretmek için: `age-keygen -o key.txt`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan `.age` (veya çözülmüş) dosyanın yolunu belirt
- Parola tabanlıysa parolayı güvenli sakla uyarısı yap

## Hata durumları

- **`age: command not found`:** macOS `brew install age`, Linux
  `sudo apt install age` (veya GitHub release).
- **`incorrect passphrase`:** Yanlış parola.
- **Alıcı/anahtar hatası:** Asimetrik kullanımda doğru recipient/identity
  dosyası gerekli.
- **Dosya bulunamadı:** Yolu teyit et.
