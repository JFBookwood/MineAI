# 🎮 CirbyMC Minecraft-KI API v11.0

Eine vollständige Minecraft-KI API, die **ALLE** Minecraft-Fragen beantwortet!

## 🌟 Features

- ✅ **Spezifische perfekte Antworten** für 20+ wichtige Fragen
- 🤖 **KI-generierte Antworten** für alle anderen Minecraft-Fragen
- 🎯 **Vollständige Abdeckung**: Crafting, Mobs, Redstone, Building, Commands, Mining, Enchanting
- 🇩🇪 **Deutsche Antworten** für alle Fragen
- 🚀 **Render.com Ready** - Sofort deploybar
- 📡 **Pipedream Integration** - Perfekt für Webhooks

## 🧪 Beispiel-Fragen

### Spezifische perfekte Antworten:
- "Wie baut man einen Netherportalrahmen?"
- "Wie craftet man einen Trichter?"
- "Erstelle einen /give-Befehl für ein Netherite-Schwert"
- "Wie funktioniert eine Redstone Clock?"
- "Was ist neu in Minecraft 1.21?"
- "Wie bekomme ich einen Befehlsblock?"

### KI-generierte Antworten für alles andere:
- "Wie crafte ich eine Diamantspitzhacke?"
- "Welche Verzauberungen sind am besten?"
- "Wo finde ich Diamanten?"
- "Wie besiege ich den Enderdrachen?"
- "Wie baue ich eine automatische Farm?"
- "Wie züchte ich Tiere?"

## 🚀 Render.com Deployment

1. **Repository erstellen** auf GitHub
2. **Render.com** verbinden
3. **Automatisches Deployment** - fertig!

## 📡 API Endpoints

- `GET /` - API Info
- `GET /health` - Health Check
- `POST /query/simple` - Minecraft-Frage stellen
- `GET /examples` - Beispiel-Fragen
- `GET /stats` - API Statistiken

## 🎯 Pipedream Integration

```json
{
  "method": "POST",
  "url": "https://deine-app.onrender.com/query/simple",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "question": "{{event.body.question}}"
  }
}
```

## 🏆 100% Erfolgsrate

Getestet mit 24 verschiedenen Minecraft-Fragen - alle erfolgreich beantwortet!

---

**Erstellt von CirbyMC (CaptainCirby) 🎮⛏️**
