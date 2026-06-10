---
name: video-info
version: 0.1.0
description: Bir medya dosyasının süre, çözünürlük, codec, bitrate gibi bilgilerini gösterir.
icon: "📺"
example_prompt: "video.mp4 kaç saniye, çözünürlüğü ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ffprobe]
  internet: false
tags: [media, video, metadata, info, file]
---

# Video Info Skill

Bir video/ses dosyasının teknik bilgilerini (süre, çözünürlük, codec, bitrate,
fps) gösterir. `ffprobe` (ffmpeg paketiyle gelir) kullanılır. Bu skill yalnız
**okur**, dosyayı değiştirmez.

## Çalıştırılacak komut

**İnsan-okunur özet:**

```
ffprobe -hide_banner <dosya>
```

**Yapılandırılmış (JSON) — script için:**

```
ffprobe -v quiet -print_format json -show_format -show_streams <dosya>
```

**Sadece süre (saniye):**

```
ffprobe -v quiet -show_entries format=duration -of csv=p=0 <dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile özetle:
- **Süre** (sa:dk:sn), **çözünürlük** (genişlik×yükseklik), **fps**
- **Video codec** (h264, hevc…) ve **ses codec** (aac, mp3…)
- **Bitrate** ve dosya boyutu
- Ham JSON'u yapıştırma; okunaklı liste yap

## Hata durumları

- **`ffprobe: command not found`:** ffmpeg paketini kur (`brew install ffmpeg` /
  `apt install ffmpeg`); `ffprobe` onunla gelir.
- **`Invalid data found`:** Dosya bozuk veya bir medya dosyası değil.
- **Dosya bulunamadı:** Yolu teyit et.
