---
name: ping
version: 0.1.0
description: Bir host'a ping atarak erişilebilirliğini ve gecikme süresini (latency) ölçer.
icon: "📶"
example_prompt: "google.com'a ping at"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ping]
  internet: true
tags: [ping, network, latency, connectivity]
---

# Ping Skill

Bir host'un erişilebilirliğini ve ağ gecikmesini (latency) ölçmek için `ping`
kullanılır. Tamamlayıcı skill'ler: `dns-lookup` (DNS sorgusu),
`http-headers` (HTTP yanıt başlıkları), `network-interfaces` (yerel ağ).

## Çalıştırılacak komut

**Varsayılan (4 paket):**

```
ping -c 4 <host>
```

`<host>` yerine kullanıcının belirttiği domain veya IP adresini koy.

Kullanıcı farklı sayıda paket istiyorsa `-c` değerini değiştir.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Gönderilen ve alınan paket sayısını göster
- **Paket kaybı** yüzdesini belirt
- Ortalama, minimum ve maksimum **gecikme süresini** (ms) vurgula
- Genel olarak bağlantının iyi/kötü olduğunu yorumla

## Hata durumları

- **`100% packet loss`:** Host erişilemiyor; ağ bağlantısını veya host adresini
  kontrol etmesini öner.
- **`unknown host`:** Domain çözümlenemedi; yazımı kontrol ettir veya
  `dns-lookup` skill'ini öner.
- **`ping` bulunamadı:** Hemen her sistemde yerleşik; yoksa kurulması gerekir.
- **Timeout:** Firewall engelliyor olabilir; ICMP trafiğinin açık olması gerek.
