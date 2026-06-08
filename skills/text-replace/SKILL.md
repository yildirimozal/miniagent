---
name: text-replace
version: 0.1.0
description: Bir dosyadaki belirli bir metni bulup başka bir metinle değiştirir (find & replace).
icon: "🔤"
example_prompt: "config.txt'teki 'localhost' ifadelerini '192.168.1.1' ile değiştir"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sed]
  internet: false
tags: [text, replace, find, file, edit]
---

# Text Replace Skill

Bir dosyadaki belirli bir metni bulup başka bir metinle değiştirmek için `sed`
kullanılır. Tamamlayıcı skill'ler: `wc-stats` (satır/kelime sayısı),
`slugify` (slug dönüşümü), `file-find` (dosya arama).

## Çalıştırılacak komut

**Dosyada değiştirme (yerinde):**

macOS:
```
sed -i '' 's/<eski>/<yeni>/g' <dosya>
```

Linux:
```
sed -i 's/<eski>/<yeni>/g' <dosya>
```

**Önce önizleme (dosyayı değiştirmeden):**

```
sed 's/<eski>/<yeni>/g' <dosya>
```

**Büyük/küçük harf duyarsız:**

```
sed 's/<eski>/<yeni>/gI' <dosya>
```

ÖNEMLİ: Kullanıcıya değişiklik yapmadan önce **önizleme göster**. Onay aldıktan
sonra yerinde değiştirme yap. `<eski>` ve `<yeni>` içinde `/` karakteri varsa
ayraç olarak `|` kullan: `sed 's|<eski>|<yeni>|g'`.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Kaç satırda değişiklik yapıldığını belirt (`grep -c` ile sayılabilir)
- Değişiklik yapılan satırları göster (az sayıda ise)
- Dosyanın yedeklenmesini öner (büyük değişikliklerde)

## Hata durumları

- **Dosya bulunamadı:** Yolu kontrol ettir.
- **Eşleşme yok:** Aranan metin dosyada yok; yazımı kontrol ettir.
- **`Permission denied`:** Dosyaya yazma izni yok.
- **Regex özel karakterler:** `<eski>` içinde `.`, `*`, `[` gibi regex
  karakterleri varsa `\` ile escape edilmeli; kullanıcıyı uyar.
- **`sed` bulunamadı:** Hemen her sistemde yerleşik.
