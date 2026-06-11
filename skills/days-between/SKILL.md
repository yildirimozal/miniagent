---
name: days-between
version: 0.1.0
description: İki tarih arasındaki gün sayısını hesaplar.
icon: "📆"
example_prompt: "2026-01-01 ile bugün arasında kaç gün var?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [time, date, calculation]
---

# Days Between Skill

İki tarih arasındaki gün farkını hesaplar. Python ile cross-platform çalışır
(macOS/Linux `date` farklarından etkilenmez).

## Çalıştırılacak komut

```
python3 -c '
import sys
from datetime import date
a = date.fromisoformat(sys.argv[1])
b = date.fromisoformat(sys.argv[2])
print(abs((b - a).days), "gün")
' <tarih1> <tarih2>
```

Tarihler **ISO formatında** (`YYYY-MM-DD`) verilmeli. Örn:
`... 2026-01-01 2026-06-09`.

**Bugüne göre** hesaplamak için ikinci tarihi bugünden al:

```
python3 -c '
import sys
from datetime import date
a = date.fromisoformat(sys.argv[1])
print(abs((date.today() - a).days), "gün")
' <tarih>
```

> Bu komut bugünün tarihini sistemden alır (`date.today()`), elle yazmaya gerek yok.

## Sonuç işleme

`bash` tool'undan gelen sonucu kullanıcıya **doğal Türkçe** ile aktar:
- Gün sayısını belirt; geçmiş mi gelecek mi olduğunu ekleyebilirsin
- İstenirse hafta/ay olarak da çevir (gün ÷ 7, ÷ 30 yaklaşık)

## Hata durumları

- **`Invalid isoformat string`:** Tarih `YYYY-MM-DD` değil; formatı düzelt.
- **`python3` yok:** Python 3 kur.
- **Geçersiz tarih (örn. 2026-13-40):** Ay/gün aralığını kontrol et.
