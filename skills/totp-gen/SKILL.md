---
name: totp-gen
version: 0.1.0
description: Bir TOTP gizli anahtarından anlık 2FA (iki adımlı doğrulama) kodu üretir.
icon: "🔢"
example_prompt: "şu TOTP secret için 2FA kodu üret"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [oathtool]
  internet: false
tags: [security, totp, 2fa, otp]
---

# TOTP Gen Skill

Bir TOTP (zaman tabanlı tek-kullanımlık parola) gizli anahtarından, o anki 6
haneli 2FA kodunu üretir. `oathtool` kullanılır.

> 🔐 **Güvenlik:** TOTP secret, hesabının 2FA'sının anahtarıdır. Komut satırına
> doğrudan yazmak onu **shell geçmişine ve süreç listesine** sızdırır. Secret'ı
> bir dosyada tut ve oradan oku.

## Çalıştırılacak komut

**Secret'ı bir dosyadan okuyarak (önerilen):**

```
oathtool --totp -b "$(cat <secret_dosyası>)"
```

`-b` secret'ın **base32** formatında olduğunu belirtir (çoğu servis böyle verir).

**Doğrudan (yalnız tek seferlik/test, sızıntı riskiyle):**

```
oathtool --totp -b <SECRET>
```

## Sonuç işleme

`bash` tool'undan gelen 6 haneli kodu kullanıcıya aktar:
- Kodun **~30 saniye** geçerli olduğunu, süresi dolarsa tekrar üretmek
  gerektiğini hatırlat
- Secret'ı ekrana/loga yazma

## Hata durumları

- **`oathtool: command not found`:** macOS `brew install oath-toolkit`, Linux
  `sudo apt install oathtool`.
- **`base32 decoding failed`:** Secret base32 değil; `-b` olmadan dene veya
  secret formatını kontrol et.
- **Kod kabul edilmiyor:** Cihaz saati kaymış olabilir (TOTP saat hassas);
  sistem saatini senkronla.
