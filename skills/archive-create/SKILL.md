---
name: archive-create
version: 0.1.0
description: Belirtilen dosya veya klasörlerden zip ya da tar.gz arşivi oluşturur.
icon: "📦"
example_prompt: "~/Desktop/proje klasörünü zip'le"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [zip, tar]
  internet: false
tags: [archive, zip, tar, file, create]
---

# Archive Create Skill

Bir veya daha fazla dosya/klasörden arşiv oluşturmak için `zip` veya `tar`
kullanılır. Tamamlayıcı skill: `archive-list` (arşiv içeriğini listeleme).

## Çalıştırılacak komut

**zip oluşturmak için:**

```
zip -r <çıktı.zip> <kaynak1> <kaynak2> ...
```

**tar.gz oluşturmak için:**

```
tar -czvf <çıktı.tar.gz> <kaynak1> <kaynak2> ...
```

**tar.bz2 oluşturmak için:**

```
tar -cjvf <çıktı.tar.bz2> <kaynak1> <kaynak2> ...
```

Kullanıcı format belirtmezse **zip** kullan (en yaygın).
Çıktı dosya adı belirtilmemişse kaynak klasör/dosya adından türet
(örn. `proje` → `proje.zip`).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Oluşturulan arşivin **tam yolunu** göster
- Eklenen dosya **sayısını** belirt
- Arşivin **boyutunu** söyle (`ls -lh` ile kontrol edebilirsin)

## Hata durumları

- **`Permission denied`:** Hedef dizine yazma izni yok; farklı bir dizin öner.
- **Kaynak bulunamadı:** Dosya veya klasör mevcut değil; yolu kontrol ettir.
- **`zip`/`tar` bulunamadı:** Çoğu sistemde yerleşik; yoksa kurulması gerekir.
- **Disk dolu:** Yeterli alan olmadığında uyar.
