---
name: api-health-check
version: 0.1.0
description: Bir API veya web adresine istek atıp HTTP durumunu ve gecikmesini ölçer.
icon: "🩺"
example_prompt: "API ayakta mı kontrol et: https://api.github.com"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [curl]
  internet: true
tags: [api, network, health, http]
---

# API Health Check Skill

Belirtilen bir URL'ye (genelde bir REST API veya web sayfası) istek atarak API'nin ayakta olup olmadığını (Status Code) ve ne kadar sürede yanıt verdiğini ölçer.

## Yöntem

`bash` tool'u ile `curl` komutunu kullanarak sadece metadata'yı alacak şekilde (gövdeyi gizleyerek) şu komutu çalıştır:

```bash
curl -s -o /dev/null -w "HTTP_CODE: %{http_code}\nTIME_TOTAL: %{time_total}s\nTIME_NAMELOOKUP: %{time_namelookup}s\nCONTENT_TYPE: %{content_type}\n" "https://HEDEF_URL"
```

Eğer API'den dönen gövdenin de (örneğin hata mesajı) ufak bir önizlemesini görmek isterseniz, `-o /dev/null` kısmını çıkarıp hem body'i hem status kodu okuyacak bir bash komutu yazabilirsiniz.

## Sonuç işleme

Elde edilen HTTP Status Code'un ne anlama geldiğini (ör: 200 OK, 404 Not Found, 500 Server Error) kısaca açıkla.
Toplam yanıt süresini (TIME_TOTAL) ve hedef url'yi formatlı, okunabilir bir tablo veya maddeler halinde kullanıcıya sun.
