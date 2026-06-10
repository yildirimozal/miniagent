---
name: video-compress
version: 0.1.0
description: Bir videonun dosya boyutunu H.264/CRF ile yeniden kodlayarak küçültür.
icon: "📉"
example_prompt: "büyük-video.mov dosyasını sıkıştır"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ffmpeg]
  internet: false
tags: [media, video, compress, optimize, file]
---

# Video Compress Skill

Bir videoyu H.264 codec ve CRF (Constant Rate Factor) ile yeniden kodlayarak
dosya boyutunu küçültür. `ffmpeg` kullanılır.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
ffmpeg -i <video> -vcodec libx264 -crf 28 -preset medium <çıktı.mp4>
```

- `-crf 28` — kalite/boyut dengesi. **Düşük = daha kaliteli + büyük dosya**
  (18 görsel olarak kayıpsıza yakın, 23 varsayılan, 28 belirgin küçülme).
- `-preset` — `ultrafast`…`veryslow`; yavaş preset = daha iyi sıkıştırma.

Sesi de küçültmek için: `-acodec aac -b:a 128k` ekle.

Boyut karşılaştırması için: `ls -lh <video> <çıktı.mp4>`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Eski/yeni dosya boyutunu ve küçülme yüzdesini belirt (`ls -lh`)
- Kalite/boyut için `-crf` değerini ayarlamayı öner

## Hata durumları

- **`ffmpeg: command not found`:** `brew install ffmpeg` / `apt install ffmpeg`.
- **Çıktı girdiden büyük:** Kaynak zaten sıkıştırılmış olabilir; `-crf` artır.
- **Çok yavaş:** `-preset faster`/`ultrafast` kullan (daha az sıkıştırma).
- **Girdi okunamadı:** Video yolu/formatı hatalı.
