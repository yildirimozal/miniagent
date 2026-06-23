---
name: port-check
version: 0.1.0
description: Bir host'ta belirli bir TCP portunun açık (erişilebilir) olup olmadığını kontrol eder.
icon: "🔌"
example_prompt: "example.com 443 portu açık mı?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [nc]
  internet: true
tags: [network, port, tcp, connectivity, debug]
---

# Port Check Skill

Bir host'ta bir TCP portunun **açık ve erişilebilir** olup olmadığını test eder
— "servise bağlanamıyorum" durumlarının ilk teşhisi. `nc` (netcat) kullanılır.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
nc -zv -w 3 <host> <port>
```

- `-z` — sadece tara (veri gönderme)
- `-v` — sonucu yaz (succeeded / refused)
- `-w 3` — 3 saniye zaman aşımı (takılmasın)

**Birden fazla port veya aralık:**

```
nc -zv -w 3 <host> 80 443
nc -zv -w 3 <host> 8000-8010
```

**`nc` yoksa — bash `/dev/tcp` ile alternatif:**

```
timeout 3 bash -c "</dev/tcp/<host>/<port>" 2>/dev/null && echo "açık" || echo "kapalı/erişilemez"
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- **`succeeded`/açık** → port açık, servis bağlantı kabul ediyor
- **`Connection refused`** → host ayakta ama o portta dinleyen servis yok
- **timeout (yanıt yok)** → host erişilemez ya da güvenlik duvarı paketi düşürüyor
  (refused'tan farkı: refused aktif ret, timeout sessizlik)
- Hangi host:port'un test edildiğini belirt

## Hata durumları

- **`could not resolve host`:** DNS çözülemedi; host adını kontrol et (`dns-lookup`
  ile bakılabilir).
- **`nc: command not found`:** macOS'ta genelde vardır; Linux'ta
  `sudo apt install netcat-openbsd`, ya da yukarıdaki `/dev/tcp` alternatifi.
- **Her port timeout:** Güvenlik duvarı veya yanlış host olabilir; `ping` ile
  host'un ayakta olduğunu doğrula.
- **UDP gerekiyor:** Bu skill TCP içindir; UDP için `nc -zuv` ayrı bir durumdur
  (UDP'de "açık" tespiti güvenilmezdir).
