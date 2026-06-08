---
name: sql-format
version: 0.1.0
description: Tek satırlık veya karmaşık SQL sorgularını okunabilir, girintili bir yapıya çevirir.
icon: "🗄️"
example_prompt: "Şu SQL'i formatla: SELECT id, name FROM users WHERE age > 18 ORDER BY name"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, sql_format]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [python3]
  internet: false
tags: [developer, sql, database, formatter]
---

# SQL Format Skill

Kullanıcının verdiği sıkışık, düzensiz veya tek satırlık SQL komutunu göze hoş gelen ve daha okunabilir bir formata getirir.

## Yöntem

Tam teşekküllü bir SQL parser gerekmeden, temel SQL anahtar kelimelerini ayırıp yeni satıra geçerek basit ama etkili bir formatlama yapabiliriz. Bunu Python ile yapabilirsiniz:

```bash
python3 -c '
import sys, re
sql = sys.argv[1].replace("\n", " ")
keywords = ["SELECT", "FROM", "WHERE", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "GROUP BY", "ORDER BY", "HAVING", "LIMIT", "UPDATE", "SET", "INSERT INTO", "VALUES", "DELETE FROM"]
for kw in keywords:
    sql = re.sub(r"\b(?i)" + kw + r"\b", "\n" + kw.upper(), sql)
print(sql.strip())
' "SQL_SORGUSU_BURAYA"
```

Eğer sistemde `sqlparse` kütüphanesi (python modülü) kuruluysa doğrudan onu kullanmak çok daha iyi sonuç verir, ancak kurulu değilse yukarıdaki Regex tabanlı yaklaşımı yedek olarak kullanabilirsiniz.

## Sonuç işleme

Dönen formatlı SQL sorgusunu Markdown formatında `sql` kod bloğu içinde kullanıcıya sun. Sonucu sunarken kısa ve net ol.
