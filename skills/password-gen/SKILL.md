---
name: password-gen
version: 0.1.0
description: Rastgele güçlü şifre oluşturur.
icon: "🔑"
example_prompt: "Bana 16 karakterli güvenli bir şifre oluştur."
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [openssl]
  internet: false
tags: [security, password, generator]
---

# Password Generator Skill

Kullanıcının belirttiği uzunlukta (varsayılan 16 karakter) güçlü ve rastgele bir şifre oluşturmak için `openssl rand` veya türevi komutları kullan.

## Çalıştırılacak komut

`bash` tool'u ile şu komutu çalıştır (örneğin 16 karakter için):

```bash
openssl rand -base64 16 | cut -c1-16
```

## Sonuç işleme

Elde edilen şifreyi kullanıcıya doğrudan, Markdown formatında kod bloğu içinde ver. Güvenli bir şifre olduğunu belirt.
