---
name: file-type
version: 0.1.0
description: Bir dosyanın gerçek türünü uzantıdan bağımsız olarak içeriğinden tespit eder.
icon: "🔬"
example_prompt: "bu uzantısız dosya aslında ne: ~/Downloads/data"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [file]
  internet: false
tags: [file, type, detect, magic]
---

# File Type Skill

Bir dosyanın **gerçek türünü** uzantısına değil, içeriğine (magic bytes) bakarak
söyler. Uzantısı yanlış/eksik ya da gizemli dosyalar için. `file` komutu kullanılır.

## Çalıştırılacak komut

**Açıklayıcı tür:**

```
file <dosya>
```

**Sadece tür (dosya adı olmadan):**

```
file -b <dosya>
```

**MIME tipi (script/otomasyon için):**

```
file --mime-type <dosya>
```

**Birden fazla dosya:** `file <dosya1> <dosya2>` ya da `file <klasör>/*`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Tespit edilen türü açıkla (örn. "uzantısı yok ama aslında bir PNG görseli")
- Uzantı ile gerçek tür **uyuşmuyorsa** bunu özellikle belirt (güvenlik/sürpriz)
- MIME tipi istenmişse onu ver

## Hata durumları

- **`cannot open` / dosya bulunamadı:** Yolu teyit et.
- **`data` veya `empty`:** İçerik tanınamadı (bilinmeyen ikili format) ya da dosya
  boş.
- **`file: command not found`:** Çok nadirdir; Linux'ta `file` paketi kurulmalı.
