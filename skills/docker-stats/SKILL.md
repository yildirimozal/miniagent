---
name: docker-stats
version: 0.1.0
description: Çalışan Docker konteynerlerinin kaynak kullanımını gösterir.
icon: "🐳"
example_prompt: "Hangi docker konteynerleri ne kadar RAM yiyor?"
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
  binaries: [docker]
  internet: false
tags: [docker, devops, containers, stats]
---

# Docker Stats Skill

Çalışan Docker konteynerlerinin CPU, bellek (RAM) ve Ağ (Network I/O) kullanımlarını hızlıca listelemek için kullanılır.

## Yöntem

Terminalde `bash` tool'u aracılığıyla şu komutu çalıştır:

```bash
docker stats --no-stream --format "table {{.Name}}\t{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
```

## Sonuç işleme

Eğer `docker` kurulu değilse veya Docker arka plan hizmeti (daemon) çalışmıyorsa oluşan hatayı kullanıcıya nazikçe bildir ("Docker şu anda çalışmıyor gibi görünüyor").
Komut başarılı olursa, dönen tabloyu Markdown formatında bir tabloya dönüştürerek kullanıcıya sun. En çok kaynak tüketen konteynerleri vurgulayabilirsin.
