---
name: flush-dns
version: 0.1.0
description: İşletim sistemi/çözücüyü tespit edip DNS önbelleğini temizleyecek doğru komutu verir.
icon: "🌊"
example_prompt: "DNS önbelleğini temizle, site eski IP'ye gidiyor"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [uname]
  internet: false
tags: [network, dns, cache, troubleshooting]
---

# Flush DNS Skill

Bir alan adı taşındı ama makinen hâlâ eski IP'ye gidiyorsa DNS önbelleği
bayattır. Bu skill **platformu ve çözücüyü tespit eder** ve önbelleği
temizleyecek **doğru komutu verir**.

> ⚠️ DNS temizleme komutları `sudo` (root) gerektirir. Ajanox `sudo`'yu otomatik
> ÇALIŞTIRMAZ — agent yalnız tespiti yapar, doğru `sudo ...` komutunu **gösterir**;
> kullanıcı kendi parolasıyla çalıştırır. İşin zor kısmı (hangi komut?) zaten tespit.

## Çalıştırılacak komut

**1. Platformu tespit et (sudo'suz, salt-okunur):**

```
uname -s
```

`Darwin` → macOS. `Linux` → Linux; çözücüyü de belirle:

```
systemctl is-active systemd-resolved 2>/dev/null; command -v nscd; command -v dnsmasq
```

**2. Tespite göre kullanıcıya şu komutu GÖSTER (agent çalıştırmaz, kullanıcı çalıştırır):**

macOS:

```
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

Linux — `systemd-resolved` aktifse:

```
sudo resolvectl flush-caches
```

Linux — `nscd` varsa: `sudo systemctl restart nscd`
Linux — `dnsmasq` varsa: `sudo systemctl restart dnsmasq`

## Sonuç işleme

Kullanıcıya:
- Tespit edilen platform/çözücüyü söyle ve **çalıştırması gereken tek komutu** net ver
- Komutun `sudo` parolası isteyeceğini hatırlat
- Sonrası: `dig <alanadı>` veya `nslookup <alanadı>` ile yeni IP'nin geldiğini
  doğrulayabileceğini söyle
- Tarayıcı hâlâ eskiyi gösteriyorsa tarayıcının kendi DNS önbelleğini de
  temizlemek gerekebilir

## Hata durumları

- **Çözücü belirsiz (Linux):** `systemd-resolved` aktif değilse ve nscd/dnsmasq
  yoksa, sistem büyük olasılıkla DNS önbelleği tutmuyordur; temizlenecek bir şey yok.
- **`sudo` parolası:** Komut root ister; agent çalıştıramaz, kullanıcı çalıştırmalı.
- **Temizledim ama hâlâ eski IP:** Router/upstream DNS önbelleği veya kayıt TTL'i
  sebep olabilir; TTL süresi dolana kadar beklemek gerekebilir.
