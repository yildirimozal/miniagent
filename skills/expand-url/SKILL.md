---
name: expand-url
version: 0.1.0
description: Kısaltılmış bir URL'i (bit.ly, t.co vb.) tıklamadan gerçek hedefine çözer.
icon: "🔗"
example_prompt: "şu link nereye gidiyor: https://bit.ly/xxxx"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [curl]
  internet: true
tags: [network, url, redirect, security]
---

# Expand URL Skill

Kısaltılmış veya yönlendiren bir URL'in **gerçek hedefini**, sayfayı açmadan
ve içeriği indirmeden gösterir — şüpheli linkleri tıklamadan önce nereye
gittiğini görmek için.

> ℹ️ Bu komut kısaltma servisine **bir HEAD isteği** atar (servis bunu
> loglayabilir), ama hedef sayfayı **indirmez/çalıştırmaz**. Yine de tamamen
> bilinmeyen/şüpheli linklerde dikkatli ol.

## Çalıştırılacak komut

**Son hedef URL'i göster (tüm yönlendirmeleri izleyerek):**

```
curl -sIL -o /dev/null -w '%{url_effective}\n' <url>
```

- `-s` sessiz, `-I` sadece header (HEAD), `-L` yönlendirmeleri izle,
  `-o /dev/null` gövdeyi atar, `-w '%{url_effective}'` son URL'i yazar.

**Tüm yönlendirme zincirini göster (her durağı görmek için):**

```
curl -sIL <url> | grep -i '^location:'
```

**Güvenli zaman aşımı ekle (takılmasın):**

```
curl -sIL --max-time 10 -o /dev/null -w '%{url_effective}\n' <url>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Son hedef URL'i** net göster; kısa linkten farklı bir domain'e gidiyorsa belirt
- Zincirde birden çok yönlendirme varsa duraklarını sırala
- Hedef domain tanıdık/güvenilir mi diye kullanıcının değerlendirmesini öner

## Hata durumları

- **`could not resolve host`:** Link veya domain geçersiz.
- **Aynı URL döndü:** Link zaten kısaltılmamış (yönlendirme yok).
- **Zaman aşımı:** Sunucu yanıt vermiyor; `--max-time` ile sınırlı kalır.
- **`curl: command not found`:** Hemen her sistemde vardır; yoksa kurulması gerek.
