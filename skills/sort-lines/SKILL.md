---
name: sort-lines
version: 0.1.0
description: Bir dosyanın satırlarını sıralar (alfabetik, sayısal, ters, benzersiz).
icon: "🔢"
example_prompt: "liste.txt'i alfabetik sırala"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sort]
  internet: false
tags: [text, sort, file]
---

# Sort Lines Skill

Bir dosyanın satırlarını sıralar. `sort` kullanılır; çıktı varsayılan olarak
ekrana gelir (dosya değişmez).

## Çalıştırılacak komut

**Alfabetik:**

```
sort <dosya>
```

Sık kullanılan bayraklar:
- `-n` — sayısal sıralama (1, 2, 10 doğru sırada)
- `-r` — ters sıralama
- `-u` — sıralarken tekrarları at (benzersiz)
- `-f` — büyük/küçük harf duyarsız

**Sonucu yeni dosyaya kaydetmek için:**

```
sort <dosya> -o <çıktı>
```

(`-o` ile aynı dosyaya yazmak güvenlidir; `> aynı_dosya` İÇERİĞİ SİLER.)

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Sıralı satırları göster (uzunsa ilk birkaçını + toplam satır sayısı)
- Hangi sıralama tipinin uygulandığını belirt

## Hata durumları

- **Dosya bulunamadı:** Yolu teyit et.
- **Beklenmedik sıra (sayılar):** Sayısal alanlar için `-n` ekle.
- **`> dosya` ile boş dosya:** Aynı dosyaya yönlendirme içeriği siler; `-o` kullan.
