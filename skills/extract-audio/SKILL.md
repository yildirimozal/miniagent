---
name: extract-audio
version: 0.1.0
description: Bir videodan ses parçasını çıkarıp ses dosyası (mp3/m4a/wav) olarak kaydeder.
icon: "🎵"
example_prompt: "ders.mp4'ten sesi mp3 olarak çıkar"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ffmpeg]
  internet: false
tags: [media, video, audio, extract, file]
---

# Extract Audio Skill

Bir videodan ses kanalını ayıklayıp ayrı bir ses dosyasına kaydeder. `ffmpeg`
kullanılır.

## Çalıştırılacak komut

**MP3 olarak (yeniden kodlar):**

```
ffmpeg -i <video> -vn -q:a 0 -map a <çıktı.mp3>
```

- `-vn` — video kanalını at
- `-q:a 0` — en yüksek MP3 kalitesi

**Sesi olduğu gibi, yeniden kodlamadan çıkar (en hızlı, kalite kaybı yok):**

```
ffmpeg -i <video> -vn -acodec copy <çıktı.m4a>
```

> `copy` kullanırken çıktı uzantısı kaynak ses codec'iyle uyumlu olmalı
> (genelde `.m4a` / `.aac`).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Oluşan ses dosyasının yolunu, formatını ve süresini belirt
- `copy` mi yoksa yeniden-kodlama mı yapıldığını söyle

## Hata durumları

- **`ffmpeg: command not found`:** `brew install ffmpeg` / `apt install ffmpeg`.
- **`copy` ile hata:** Çıktı uzantısı kaynak codec'le uymuyor; MP3'e yeniden
  kodlamayı (`-q:a 0`) dene.
- **Videoda ses yok:** Kaynak sessizdir; kullanıcıya bildir.
- **Girdi okunamadı:** Video yolu/formatı hatalı.
