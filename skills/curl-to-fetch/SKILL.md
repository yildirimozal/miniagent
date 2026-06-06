---
name: curl-to-fetch
version: 0.1.0
description: cURL komutunu JavaScript fetch() metoduna çevirir.
icon: "🌐"
example_prompt: "Şu cURL'i fetch yap: curl -X POST https://api.com -d '{\"x\": 1}'"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, curl_to_fetch]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  internet: false
tags: [curl, fetch, javascript, developer]
---

# cURL to Fetch Skill

Ağ sekmesinden veya dökümantasyonlardan kopyalanan `curl` komutlarını, doğrudan Frontend projelerinde kullanılabilecek JavaScript `fetch()` kod bloğuna çevirir.

## Yöntem

Harici bir komut çalıştırmaya gerek kalmadan, Agent'ın kendi doğal dil işleme (NLP) yeteneğini kullanarak bu komutu ayrıştır. Kullanıcının sağladığı cURL metnini incele:
- URL'yi tespit et.
- HTTP metodunu (`-X POST`, `-X GET` vb.) tespit et.
- Gövdeyi (`--data`, `-d` vb.) tespit et.
- Header'ları (`-H "Authorization: Bearer..."`) tespit et.

Sonra tüm bu bilgileri standart bir JavaScript `fetch(url, options)` formatında yaz.

## Sonuç işleme

Dönüştürülmüş JavaScript/TypeScript kodunu Markdown `javascript` kod bloğu içinde kullanıcıya sun. Header'lar ve body kısmı varsa bunların uygun formatta (örneğin JSON.stringify kullanarak) eklendiğinden emin ol.
Mümkünse kod bloğunun sonuna örnek bir `.then(res => res.json())` veya `await` kullanımı ekleyerek kullanımı daha da kolaylaştır.
