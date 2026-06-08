---
name: rsa-keypair-gen
version: 0.1.0
description: Test amaçlı hızlıca RSA Public ve Private anahtar çifti oluşturur.
icon: "🗝️"
example_prompt: "Bana bir RSA anahtar çifti oluştur."
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
tags: [security, rsa, keys, crypto]
---

# RSA Keypair Generator Skill

Genellikle JWT imzalama/doğrulama işlemleri (RS256) veya şifreleme testleri için hızlıca 2048 bitlik bir RSA Private/Public Key (PEM formatında) çifti üretir.

## Yöntem

Aşağıdaki openssl komutlarını kullanarak geçici dosyalar üzerinden veya doğrudan stdout üzerinden anahtarları üretebilirsin. `bash` tool'unu kullanarak şu komutu çalıştır:

```bash
# Private key üret ve göster, ardından bundan Public key türet ve göster
PRIVATE_KEY=$(openssl genrsa 2048 2>/dev/null)
echo "=== PRIVATE KEY ==="
echo "$PRIVATE_KEY"
echo "=== PUBLIC KEY ==="
echo "$PRIVATE_KEY" | openssl rsa -pubout 2>/dev/null
```

## Sonuç işleme

Oluşturulan Private Key ve Public Key bloklarını (`-----BEGIN PRIVATE KEY-----` ile başlayan kısımları) iki ayrı Markdown kod bloğu halinde kullanıcıya sun.
Bu anahtarların sadece test ve geliştirme amaçlı olduğunu, canlı (production) ortamda bu şekilde rastgele oluşturulan ve bir chat ortamından geçen anahtarların güvenli olmayacağını mutlaka hatırlat.
