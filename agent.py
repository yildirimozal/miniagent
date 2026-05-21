"""
Mini Agent — Ollama + Qwen 2.5 7B
Local'de calisan bir AI agent. Ekstra paket gerekmez.

Calistir:  python3 agent.py
Cik:       q (veya Ctrl+C)
"""
import json
import os
import urllib.request

OLLAMA_URL = "http://localhost:11500/api/chat"
MODEL = "qwen2.5:7b"
IDENTITY_FILE = os.path.expanduser("~/Desktop/miniagent/identity.json")

# =========================================================
# 1) TOOLS — Agent'in "elleri". Normal Python fonksiyonlari.
# =========================================================
def list_files(directory: str) -> str:
    try:
        items = os.listdir(os.path.expanduser(directory))
        return "\n".join(items) if items else "(bos klasor)"
    except Exception as e:
        return f"Hata: {e}"


def read_file(path: str) -> str:
    try:
        with open(os.path.expanduser(path), "r", encoding="utf-8") as f:
            return f.read()[:2000]
    except Exception as e:
        return f"Hata: {e}"


def calculator(expression: str) -> str:
    if not all(c in "0123456789+-*/(). " for c in expression):
        return "Hata: yalniz sayi ve + - * / ( ) karakterleri."
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Hata: {e}"


def set_identity(name: str, description: str = "") -> str:
    """Agent'in kimligini (isim ve aciklama) dosyaya kaydet."""
    try:
        data = {"name": name, "description": description}
        with open(IDENTITY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return f"Kimlik kaydedildi: {name}"
    except Exception as e:
        return f"Hata: {e}"


def get_identity() -> str:
    """Kayitli kimligi oku."""
    try:
        if not os.path.exists(IDENTITY_FILE):
            return "Henuz bir kimlik kaydedilmemis."
        with open(IDENTITY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        name = data.get("name", "bilinmiyor")
        desc = data.get("description", "")
        if desc:
            return f"Ismim: {name}. Aciklama: {desc}"
        return f"Ismim: {name}"
    except Exception as e:
        return f"Hata: {e}"

TOOLS_MAP = {
    "list_files": list_files,
    "read_file": read_file,
    "calculator": calculator,
    "set_identity": set_identity,
    "get_identity": get_identity,
}

# Model'e tool'lari tanitan sema (OpenAI/Ollama function-calling formati)
TOOLS_SCHEMA = [
    {"type": "function", "function": {
        "name": "list_files",
        "description": "Bir klasordeki dosya ve alt klasorleri listeler.",
        "parameters": {"type": "object", "required": ["directory"],
            "properties": {"directory": {"type": "string", "description": "Klasor yolu, orn: '~/Desktop'"}}}}},
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Bir dosyanin icerigini okur (ilk 2000 karakter).",
        "parameters": {"type": "object", "required": ["path"],
            "properties": {"path": {"type": "string", "description": "Dosya yolu"}}}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Matematik ifadesini hesaplar.",
        "parameters": {"type": "object", "required": ["expression"],
            "properties": {"expression": {"type": "string", "description": "Orn: '2+2*3'"}}}}},
     {"type": "function", "function": {
        "name": "calculator",
        "description": "Matematik ifadesini hesaplar.",
        "parameters": {"type": "object", "required": ["expression"],
            "properties": {"expression": {"type": "string", "description": "Orn: '2+2*3'"}}}}},
    {"type": "function", "function": {
        "name": "set_identity",
        "description": "Agent'in kendi kimligini (isim ve aciklama) kalici olarak kaydeder. Kullanici 'ismin X olsun', 'sana Y diyecegim', 'adini Z koyalim' gibi seyler dediginde bu tool'u kullan. Sadece isim verilen durumlarda description'i bos birak.",
        "parameters": {"type": "object", "required": ["name"],
            "properties": {
                "name": {"type": "string", "description": "Agent'a verilecek isim, orn: 'Sekhmet'"},
                "description": {"type": "string", "description": "Opsiyonel kisa aciklama, orn: 'Misir mitolojisinde aslan basli tanrica'"}
            }}}},
    {"type": "function", "function": {
        "name": "get_identity",
        "description": "Agent'in kayitli kimligini (ismini ve aciklamasini) okur. Kullanici 'sen kimsin', 'ismin ne', 'adin neydi' gibi seyler sordugunda bu tool'u kullan.",
        "parameters": {"type": "object", "required": [], "properties": {}}}},
]       



# =========================================================
# 2) Ollama'ya istek gonder
# =========================================================
def chat(messages):
    payload = json.dumps({"model": MODEL, "messages": messages,
                          "tools": TOOLS_SCHEMA, "stream": False}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["message"]


# =========================================================
# 3) AGENT LOOP — Sihir burada
#    kullanici sorusu -> LLM dusunur -> tool cagirir
#    -> sonuc LLM'e gider -> LLM tekrar dusunur -> ... -> cevap
# =========================================================
def run_agent(user_input: str, max_iter: int = 6):
    messages = [
        {"role": "system", "content": "Sen yardimci bir Turkce asistansin. Sadece Turkce konus, asla baska dile gecme. Normal sohbet et, dogal davran. Kullanici sana 'sen kimsin', 'ismin ne' gibi seyler sordugunda get_identity ile ismini kontrol et. Kullanici sana yeni bir isim verirse (ornegin 'ismin X olsun') set_identity ile kaydet. Diger durumlarda bu tool'lari cagirma, dogrudan cevap ver. Diger tool'lari da gerektiginde kullan."},
        {"role": "user", "content": user_input},
    ]
    for _ in range(max_iter):
        msg = chat(messages)
        messages.append(msg)

        tool_calls = msg.get("tool_calls") or []
        if not tool_calls:
            print(f"\nAgent: {msg.get('content', '').strip()}\n")
            return

        for call in tool_calls:
            name = call["function"]["name"]
            args = call["function"]["arguments"]
            print(f"  [tool] {name}({args})")
            result = TOOLS_MAP[name](**args)
            preview = result[:150].replace("\n", " ")
            print(f"  [out ] {preview}{'...' if len(result) > 150 else ''}")
            messages.append({"role": "tool", "content": str(result)})

    print("\n(Max iteration asildi.)\n")


# =========================================================
# 4) Sohbet dongusu
# =========================================================
if __name__ == "__main__":
    print(f"Mini Agent ({MODEL}) — cikmak icin 'q'\n")
    while True:
        try:
            q = input("Sen: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("q", "quit", "exit"):
            break
        if q:
            run_agent(q)
