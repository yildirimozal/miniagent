---
name: jwt-decode
version: 0.1.0
description: JWT (JSON Web Token) içeriğini çözümler ve gösterir.
icon: "🎫"
example_prompt: "Şu JWT token'ını decode et: eyJhbG..."
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
tags: [jwt, decode, security, web]
---

# JWT Decode Skill

Kullanıcının verdiği JWT (JSON Web Token) string'ini parçalarına ayırıp içeriğini (header ve payload) JSON formatında çözümler.

## Yöntem

JWT üç parçadan oluşur: `header.payload.signature`. Base64Url formatındadır.
`python3` yardımıyla token içeriği decode edilebilir:

```python
import sys
import base64
import json

token = sys.argv[1]
parts = token.split('.')
if len(parts) != 3:
    print("HATA: Geçersiz JWT formatı")
    sys.exit(1)

def decode_part(part):
    padded = part + '=' * (4 - len(part) % 4)
    return json.loads(base64.urlsafe_b64decode(padded))

print("=== HEADER ===")
print(json.dumps(decode_part(parts[0]), indent=2))
print("=== PAYLOAD ===")
print(json.dumps(decode_part(parts[1]), indent=2))
```

Bu Python kodunu `bash` tool'u ile çalıştırabilirsiniz.

## Sonuç işleme

Header ve Payload kısımlarını okunabilir, formatlanmış JSON blokları halinde kullanıcıya göster. 
Hassas veriler (varsa) konusunda dikkatli olmasını tavsiye et.
Signature kısmı doğrulanmadığı için bunun sadece "decode" işlemi olduğunu, bir "verify" işlemi olmadığını belirt.
