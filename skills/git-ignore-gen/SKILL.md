---
name: git-ignore-gen
version: 0.1.0
description: Belirtilen teknolojiler için hazır .gitignore şablonu oluşturur.
icon: "🙈"
example_prompt: "Node, Python ve macOS için bir gitignore oluştur"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, git_ignore]
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
tags: [git, developer, ignore, setup]
---

# Git Ignore Generator Skill

Kullanıcının projede kullandığı teknolojilere (dil, framework, işletim sistemi) uygun, standart bir `.gitignore` dosyası oluşturmak için `gitignore.io` API'sini kullanır.

## Yöntem

Kullanıcının isteklerini virgülle ayrılmış küçük harfli bir listeye çevir (örneğin: `node,python,macos`).
Sonra `bash` tool'u ile şu API'ye istek at:

```bash
curl -sL "https://www.toptal.com/developers/gitignore/api/TEKNOLOJI_LISTESI"
```
Örnek komut:
`curl -sL "https://www.toptal.com/developers/gitignore/api/node,python,macos"`

## Sonuç işleme

Dönen `.gitignore` içeriğini kullanıcıya Markdown kod bloğu içinde sun. İstenirse bu içeriği doğrudan projenin `.gitignore` dosyasına yazabileceğini (veya yazmanı isteyip istemediğini) sor.
Eğer API geçersiz bir teknoloji adı tespit ederse dönen hata mesajını (veya boş sonucu) yorumlayarak kullanıcıdan doğru teknoloji adlarını iste.
