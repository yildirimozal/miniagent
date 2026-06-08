---
name: json-to-ts
version: 0.1.0
description: Verilen bir JSON objesinden TypeScript Interface (arayüz) oluşturur.
icon: "📘"
example_prompt: "Şu JSON'dan TS interface yap: {\"id\": 1, \"name\": \"Ali\"}"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
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
tags: [json, typescript, interface, developer]
---

# JSON to TypeScript Interface Skill

Frontend ve Backend geliştiricilerin en sık ihtiyaç duyduğu şeylerden biri API'den dönen JSON verisine uygun TypeScript arayüzleri yazmaktır. Kullanıcının verdiği JSON'ı analiz edip basit düzeyde TS interface'ine çevirir.

## Yöntem

Tam kapsamlı, kompleks bir AST oluşturmak yerine Python üzerinden basit tip analizi ile bir script çalıştırabiliriz. Ancak en güvenlisi Agent'ın kendi yeteneğini kullanarak JSON anahtarlarını ve tiplerini (string, number, boolean, any[] vb.) analiz etmesidir. 
`bash` kullanmak istenirse basit bir python betiği ile:

```bash
python3 -c '
import sys, json

def get_type(val):
    if isinstance(val, bool): return "boolean"
    if isinstance(val, (int, float)): return "number"
    if isinstance(val, str): return "string"
    if isinstance(val, list):
        if len(val) > 0: return get_type(val[0]) + "[]"
        return "any[]"
    if isinstance(val, dict): return "Record<string, any>"
    return "any"

try:
    data = json.loads(sys.stdin.read())
    print("export interface RootObject {")
    for k, v in data.items():
        print(f"  {k}: {get_type(v)};")
    print("}")
except Exception as e:
    print(f"HATA: Geçersiz JSON. {e}")
' << 'EOF'
JSON_ICERIGI
EOF
```

## Sonuç işleme

Elde edilen TypeScript kodunu Markdown `typescript` bloğu içinde göster. Bu kodun temel bir başlangıç noktası olduğunu ve karmaşık iç içe objeler (nested objects) için geliştiricinin elle müdahale etmesi gerekebileceğini not düş.
