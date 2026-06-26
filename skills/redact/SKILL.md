---
name: redact
version: 0.1.0
description: Bir dosyadaki e-posta, IP ve uzun token/secret'leri maskeleyerek paylaşılabilir kopya üretir.
icon: "🖊️"
example_prompt: "log.txt'i paylaşmadan önce mail ve IP'leri gizle"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sed]
  internet: false
tags: [security, privacy, redact, mask]
---

# Redact Skill

Bir log/metin dosyasını paylaşmadan önce içindeki **hassas bilgileri** (e-posta,
IP adresi, uzun API key/token) maskeler. Çıktı ekrana gelir; orijinal dosya
değişmez.

> ⚠️ Bu **kalıbı** maskeler — her secret'ı garanti yakalamaz. Paylaşmadan önce
> çıktıyı gözle de kontrol et (kişi adları, özel yollar, vb. kalmış olabilir).

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır (e-posta, IP ve 24+ karakterli token'ları maskeler):

```
sed -E \
  -e 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/[EMAIL]/g' \
  -e 's/([0-9]{1,3}\.){3}[0-9]{1,3}/[IP]/g' \
  -e 's/[A-Za-z0-9_-]{24,}/[TOKEN]/g' \
  <dosya>
```

Maskelenmiş kopyayı kaydetmek için sona ` > <dosya>.redacted` ekle.

**Sadece belirli bir şeyi** maskelemek istenirse ilgili `-e` satırını kullan
(örn. yalnız e-posta). Kullanıcının istediği özel bir desen varsa ona göre
ek `-e 's/.../[GIZLI]/g'` ekle.

## Sonuç işleme

`bash` tool'undan gelen maskelenmiş çıktıyı kullanıcıya aktar:
- Hangi tür bilgilerin (e-posta/IP/token) maskelendiğini söyle
- **Uyar:** kalıp tabanlı; gözle son kontrolü öner
- İsterse `> dosya.redacted` ile kaydetmeyi hatırlat

## Hata durumları

- **Çok fazla şey maskelendi:** `[TOKEN]` deseni (24+ karakter) bazı normal uzun
  kelimeleri de yakalayabilir; gerekirse o `-e` satırını çıkar veya uzunluğu artır.
- **Bir secret kaçtı:** Kalıba uymayan formatlar (kısa key, özel format) için
  kullanıcıya özel `-e` deseni ekle.
- **Dosya bulunamadı:** Yolu teyit et.
