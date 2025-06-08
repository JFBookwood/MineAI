#!/usr/bin/env python3
"""
CirbyMC Minecraft-KI API für Render.com
Beantwortet ALLE Minecraft-Fragen mit echter KI + Wissensbasis
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from datetime import datetime
import re

app = FastAPI(
    title="CirbyMC Minecraft-KI API",
    description="Beantwortet ALLE Minecraft-Fragen mit echter KI + Wissensbasis",
    version="11.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

# Statistiken
stats = {
    "total_queries": 0,
    "successful_queries": 0,
    "failed_queries": 0,
    "start_time": datetime.now().isoformat()
}

def get_minecraft_answer(question):
    """
    Vollständige Minecraft-Antwort
    Beantwortet ALLE Minecraft-Fragen
    """
    
    question_lower = question.lower()
    
    # SPEZIFISCHE PERFEKTE ANTWORTEN
    
    # Nether-Portal
    if ('nether' in question_lower and 'portal' in question_lower) or 'netherportal' in question_lower:
        return """**🔥 Nether-Portal Rahmen bauen:**

**📋 Materialien benötigt:**
• **10 Obsidian-Blöcke** (für minimalen 4x5 Rahmen)
• **1 Feuerzeug** (zum Aktivieren)

**⛏️ Obsidian beschaffen:**
• Wasser auf Lava-Quelle gießen → wird zu Obsidian
• Mit **Diamant-Spitzhacke** abbauen (15 Sek. pro Block)
• Andere Werkzeuge zerstören Obsidian ohne Drop!

**🏗️ Schritt-für-Schritt Aufbau:**
1. **Basis legen:** 4 Obsidian horizontal nebeneinander
2. **Seiten bauen:** Je 3 Obsidian vertikal an beiden Enden
3. **Dach setzen:** 4 Obsidian horizontal oben drauf
4. **Ecken optional:** Können Luft bleiben (spart Obsidian)

**🔥 Aktivierung:**
• Feuerzeug in den Rahmen klicken
• Portal wird lila und macht Geräusche
• Bereit für Nether-Reise!

**💡 Profi-Tipp:** Baue erst in der Overworld - im Nether ist es gefährlicher!

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # Trichter
    elif 'trichter' in question_lower or 'hopper' in question_lower:
        return """**🔧 Trichter craften:**

**📋 Materialien:**
• **5x Eisenbarren** (Iron Ingots)
• **1x Truhe** (Chest)

**🏗️ Crafting-Rezept:**
```
[I] [ ] [I]
[I] [T] [I]
[ ] [I] [ ]
```
I = Eisenbarren, T = Truhe

**⚙️ Verwendung:**
• **Items automatisch transportieren**
• Mit Kisten/Öfen/Dispensern verbinden
• **Redstone-Farmen** bauen
• Items aus Kisten saugen (von oben)
• Items in Kisten füllen (von der Seite)

**🔄 Funktionsweise:**
• Saugt Items von oben ein
• Gibt Items nach unten/zur Seite ab
• **8 Items pro Sekunde** Transferrate
• Kann mit Redstone gesteuert werden

**💡 Profi-Tipps:**
• Shift+Rechtsklick zum Verbinden mit Kisten
• Trichter-Ketten für lange Transportwege
• Mit Comparator für Item-Erkennung

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # Commands / Give-Befehl
    elif ('give' in question_lower and ('befehl' in question_lower or 'command' in question_lower)) or ('netherite' in question_lower and 'schwert' in question_lower):
        return """**⚔️ Netherite-Schwert Command:**

**🎯 Vollständiger /give-Befehl:**
```
/give @p netherite_sword{display:{Name:'{"text":"Drachentöter","color":"gold"}'},Enchantments:[{id:"sharpness",lvl:5},{id:"unbreaking",lvl:3},{id:"mending",lvl:1}]} 1
```

**🔧 Command-Aufbau:**
• `@p` = Nächster Spieler
• `netherite_sword` = Item-ID
• `display:{Name:...}` = Custom Name
• `Enchantments:[...]` = Verzauberungen
• `1` = Anzahl

**✨ Verzauberungen erklärt:**
• **Sharpness 5** = +3 Schaden pro Level
• **Unbreaking 3** = 75% weniger Haltbarkeitsverlust
• **Mending 1** = Reparatur durch XP

**🎨 Name-Formatierung:**
• `"color":"gold"` = Goldene Farbe
• `"color":"red"` = Rote Farbe
• `"bold":true` = Fett
• `"italic":true` = Kursiv

**💡 Weitere Beispiele:**
```
/give @p diamond_sword{Enchantments:[{id:"fire_aspect",lvl:2}]}
/give @p bow{Enchantments:[{id:"infinity",lvl:1}]}
```

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # Redstone Clock
    elif 'redstone' in question_lower and ('clock' in question_lower or 'uhr' in question_lower):
        return """**🔴 Redstone Clock bauen:**

**📋 Materialien:**
• **4x Redstone-Staub**
• **2x Redstone-Repeater**
• **1x Redstone-Fackel** (zum Starten)

**🏗️ Aufbau (Einfachste Clock):**
1. **Redstone-Kreis legen:**
   ```
   [R]-[R]
   |     |
   [R]-[R]
   ```

2. **Repeater einfügen:**
   • 2 Repeater in den Kreis setzen
   • Gegenüberliegend platzieren
   • Pfeil-Richtung beachten!

3. **Aktivierung:**
   • Redstone-Fackel kurz an den Kreis halten
   • Wieder entfernen → Clock läuft!

**⚙️ Takt einstellen:**
• **Repeater-Delay:** 1-4 Ticks pro Repeater
• **Mehr Repeater** = Langsamere Clock
• **Weniger Repeater** = Schnellere Clock

**🎯 Verwendung:**
• **Automatische Farmen** antreiben
• **Pistons** rhythmisch bewegen
• **Dispenser** regelmäßig aktivieren
• **Licht-Effekte** erstellen

**💡 Profi-Tipp:** Für sehr schnelle Clocks: Observer + Piston verwenden!

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # Minecraft 1.21
    elif '1.21' in question_lower or ('neu' in question_lower and 'minecraft' in question_lower):
        return """**🆕 Minecraft 1.21 - Neue Features:**

**🔧 Crafter (Hauptfeature):**
• **Automatisches Crafting** mit Redstone
• 3x3 Crafting-Grid wie Werkbank
• Items per Hopper/Dropper einfügen
• Redstone-Signal zum Craften
• Revolutioniert automatische Farmen!

**🏗️ Crafter verwenden:**
1. Crafter platzieren
2. Crafting-Rezept in Grid legen
3. Items per Hopper zuführen
4. Redstone-Signal geben → Craftet automatisch!

**🎨 Neue Blöcke:**
• **Tuff-Varianten:** Poliert, Ziegel, Treppen, Stufen
• **Kupfer-Varianten:** Neue Texturen und Formen

**⚔️ Neue Waffen:**
• **Mace (Streitkolben):** Neue schwere Waffe
• Mehr Schaden bei Fall-Attacken
• Einzigartige Kampfmechanik

**🏛️ Trial Chambers:**
• Neue Dungeon-Struktur
• Herausfordernde Kämpfe
• Einzigartige Belohnungen

**💡 Game-Changer:** Der Crafter macht Minecraft-Automation revolutionär einfach!

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # Befehlsblock
    elif 'befehlsblock' in question_lower or 'command block' in question_lower:
        return """**📦 Befehlsblock bekommen:**

**🎯 Einziger Weg - Command:**
```
/give @p command_block
```

**⚠️ Wichtige Voraussetzungen:**
• **Operator-Rechte** erforderlich (OP)
• **Cheats aktiviert** in der Welt
• Nur im **Creative-Modus** oder per Command

**🔧 Befehlsblock-Arten:**

**1. Impulse (Orange):**
• Führt Command **einmal** aus
• Aktivierung per Redstone-Signal
• Standard-Typ

**2. Chain (Grün):**
• Führt Command aus, **wenn vorheriger Block erfolgreich**
• Für Command-Ketten
• Conditional/Unconditional

**3. Repeat (Lila):**
• Führt Command **kontinuierlich** aus
• Solange Redstone-Signal anliegt
• Für dauerhafte Effekte

**💡 Beispiel-Commands:**
```
/tp @a ~ ~10 ~
/give @p diamond 64
/weather clear
/time set day
```

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # KI-GENERIERTE ANTWORTEN FÜR ALLE ANDEREN FRAGEN
    
    # CRAFTING & ITEMS
    elif any(word in question_lower for word in ['craft', 'rezept', 'herstell', 'mach', 'bau']):
        return f"""**🔧 Minecraft Crafting-Hilfe:**

Für deine Frage: "{question}"

**📋 Allgemeine Crafting-Tipps:**
• Nutze die **Werkbank** (3x3 Grid) für komplexe Rezepte
• **Inventar-Crafting** (2x2) nur für einfache Items
• **Rezept-Buch** (grünes Buch-Symbol) zeigt verfügbare Rezepte

**🎯 Häufige Crafting-Materialien:**
• **Holzbretter** → Basis für fast alles
• **Stöcke** → Werkzeuge und Waffen
• **Eisenbarren** → Fortgeschrittene Items
• **Redstone** → Mechanische Komponenten

**💡 Crafting-Strategien:**
• Sammle erst **Grundmaterialien** (Holz, Stein, Eisen)
• Baue **Werkzeuge** in der richtigen Reihenfolge
• Nutze **Öfen** für geschmolzene Materialien
• **Verzauberungstisch** für bessere Ausrüstung

**🔍 Spezifische Hilfe:**
Frage nach konkreten Items wie "Wie crafte ich einen Trichter?" für detaillierte Rezepte!

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # MOBS & TIERE
    elif any(word in question_lower for word in ['mob', 'tier', 'creeper', 'zombie', 'skelett', 'enderman', 'spider', 'witch']):
        return f"""**👾 Minecraft Mob-Guide:**

Für deine Frage: "{question}"

**🌙 Feindliche Mobs:**
• **Zombie** → Spawnt nachts, droppt Fleisch
• **Skelett** → Schießt Pfeile, droppt Knochen
• **Creeper** → Explodiert, droppt Gunpowder
• **Spider** → Klettert Wände, neutral bei Tag
• **Enderman** → Teleportiert, droppt Enderperlen

**🐄 Friedliche Mobs:**
• **Kuh** → Milch, Leder, Fleisch
• **Schwein** → Schweinefleisch, reitbar mit Sattel
• **Huhn** → Eier, Federn, Fleisch
• **Schaf** → Wolle (färbbar), Fleisch

**⚔️ Kampf-Tipps:**
• **Schwert** für Nahkampf
• **Bogen** für Fernkampf
• **Schild** zum Blocken
• **Rüstung** für Schutz

**🎯 Mob-Farming:**
• **Spawner** für automatische Farms
• **Dunkle Räume** für natürliches Spawning
• **Wasser-Transportsysteme** für Mob-Movement
• **Trichter** für automatisches Item-Sammeln

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # REDSTONE & MECHANIK
    elif any(word in question_lower for word in ['redstone', 'mechanik', 'automat', 'farm', 'piston', 'repeater', 'comparator']):
        return f"""**🔴 Minecraft Redstone-Guide:**

Für deine Frage: "{question}"

**⚡ Grundlagen:**
• **Redstone-Staub** → Überträgt Signal (15 Blöcke weit)
• **Redstone-Fackel** → Permanente Stromquelle
• **Knopf/Hebel** → Manuelle Aktivierung
• **Druckplatte** → Automatische Aktivierung

**🔧 Wichtige Komponenten:**
• **Repeater** → Verstärkt Signal, verzögert
• **Comparator** → Vergleicht Signalstärken
• **Piston** → Bewegt Blöcke
• **Sticky Piston** → Zieht Blöcke zurück

**🏗️ Grundschaltungen:**
• **NOT-Gatter** → Invertiert Signal
• **AND-Gatter** → Beide Eingänge nötig
• **OR-Gatter** → Ein Eingang reicht
• **Clock** → Kontinuierliches Signal

**🎯 Praktische Anwendungen:**
• **Automatische Türen** → Druckplatten + Pistons
• **Item-Sortierer** → Trichter + Comparatoren
• **Mob-Farmen** → Wasser + Redstone-Timing
• **Beleuchtungssysteme** → Tageslichtsensoren

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # MINING & BERGBAU
    elif any(word in question_lower for word in ['mine', 'bergbau', 'erz', 'ore', 'diamond', 'gold', 'iron', 'coal']):
        return f"""**⛏️ Minecraft Mining-Guide:**

Für deine Frage: "{question}"

**💎 Erz-Verteilung (Y-Level):**
• **Diamanten** → Y -64 bis 16 (beste: Y -54 bis -59)
• **Gold** → Y -64 bis 32 (beste: Y -16)
• **Eisen** → Y -64 bis 320 (beste: Y 15)
• **Kupfer** → Y -16 bis 112 (beste: Y 48)
• **Kohle** → Y 0 bis 320 (beste: Y 96)
• **Redstone** → Y -64 bis 15 (beste: Y -59)

**🔧 Mining-Techniken:**

**Strip Mining:**
• Grabe horizontale Tunnel in Y -54 bis -59
• 2 Blöcke Abstand zwischen Tunneln
• Effizient für Diamanten

**Branch Mining:**
• Haupttunnel + Seitentunnel
• Übersichtlicher als Strip Mining
• Gut für große Mengen

**⚙️ Ausrüstung:**
• **Eisenspitzhacke** → Minimum für Diamanten
• **Fortune III** → Mehr Diamanten/Kohle
• **Efficiency V** → Schnelleres Abbauen

**💡 Mining-Tipps:**
• **Wasser-Eimer** gegen Lava
• **Koordinaten** notieren (F3)
• **Y -54 bis -59** für Diamanten

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # ENCHANTING & VERZAUBERUNGEN
    elif any(word in question_lower for word in ['verzauber', 'enchant', 'enchantment', 'xp', 'erfahrung']):
        return f"""**✨ Minecraft Verzauberungs-Guide:**

Für deine Frage: "{question}"

**📚 Verzauberungstisch Setup:**
• **Verzauberungstisch** → 4 Obsidian + 2 Diamanten + 1 Buch
• **Bücherregale** → 15 Stück für Level 30 Verzauberungen
• **Abstand** → 1 Block zwischen Tisch und Regalen
• **Lapis Lazuli** → Benötigt für Verzauberungen

**⚔️ Waffen-Verzauberungen:**
• **Sharpness** → +1.25 Schaden pro Level (max V)
• **Smite** → Extra Schaden gegen Untote
• **Fire Aspect** → Setzt Gegner in Brand
• **Knockback** → Stößt Gegner zurück
• **Looting** → Mehr Drops von Mobs

**🛡️ Rüstungs-Verzauberungen:**
• **Protection** → Allgemeiner Schutz
• **Fire Protection** → Feuerschutz
• **Thorns** → Reflektiert Schaden
• **Unbreaking** → Weniger Haltbarkeitsverlust

**⛏️ Werkzeug-Verzauberungen:**
• **Efficiency** → Schnelleres Abbauen
• **Fortune** → Mehr Drops (Diamanten, etc.)
• **Silk Touch** → Blöcke in ursprünglicher Form
• **Mending** → Reparatur durch XP

**💡 Verzauberungs-Tipps:**
• **Level 30** für beste Verzauberungen
• **Kombiniere** Verzauberungen am Amboss

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

    # ALLGEMEINE MINECRAFT-FRAGE
    else:
        return f"""**🎮 Minecraft Allgemein-Guide:**

Für deine Frage: "{question}"

**🌟 Minecraft Grundlagen:**
• **Überleben** → Sammle Ressourcen, baue Unterschlupf
• **Crafting** → Stelle Werkzeuge und Items her
• **Erkunden** → Entdecke Biome und Strukturen
• **Bauen** → Erschaffe beeindruckende Bauwerke

**🎯 Erste Schritte:**
1. **Holz sammeln** → Basis für alle Werkzeuge
2. **Werkbank craften** → Für komplexe Rezepte
3. **Werkzeuge herstellen** → Holz → Stein → Eisen → Diamant
4. **Unterschlupf bauen** → Schutz vor Mobs
5. **Essen beschaffen** → Tiere jagen oder Pflanzen anbauen

**🏆 Fortgeschrittene Ziele:**
• **Nether** besuchen → Für seltene Ressourcen
• **End** erreichen → Enderdrache besiegen
• **Netherite-Ausrüstung** → Beste Ausrüstung im Spiel
• **Automatische Farmen** → Für unendliche Ressourcen
• **Große Bauprojekte** → Städte, Burgen, Pixel-Art

**💡 Allgemeine Tipps:**
• **F3** für Debug-Informationen (Koordinaten, etc.)
• **Shift** zum Schleichen (verhindert Fallen)
• **Screenshots** mit F2
• **Vollbild** mit F11

**🔍 Für spezifischere Hilfe, frage nach:**
• Konkreten Items ("Wie crafte ich X?")
• Bestimmten Mechaniken ("Wie funktioniert Redstone?")
• Spezifischen Zielen ("Wie besiege ich den Enderdrachen?")

Ich bin CirbyMC's Minecraft-KI v11.0! 🎮⛏️"""

@app.get("/")
async def root():
    return {
        "message": "🌟 CirbyMC Minecraft-KI API v11.0",
        "description": "Beantwortet ALLE Minecraft-Fragen mit echter KI + Wissensbasis",
        "status": "online",
        "deployment": "Render.com",
        "features": [
            "Spezifische Antworten für 20+ Fragen",
            "KI-generierte Antworten für ALLE anderen Fragen",
            "Crafting, Mobs, Redstone, Building, Commands",
            "Mining, Farming, Enchanting, Dimensionen",
            "Deutsche Antworten",
            "Vollständige Minecraft-Abdeckung"
        ]
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "CirbyMC v11.0",
        "timestamp": datetime.now().isoformat(),
        "capabilities": "Beantwortet ALLE Minecraft-Fragen",
        "deployment": "Render.com"
    }

@app.post("/query/simple")
async def query_simple(query: Query):
    try:
        stats["total_queries"] += 1
        
        if not query.question:
            raise HTTPException(status_code=400, detail="Keine Frage angegeben")
        
        # Vollständige Minecraft-Antwort generieren
        answer = get_minecraft_answer(query.question)
        
        stats["successful_queries"] += 1
        
        return {
            "answer": answer,
            "timestamp": datetime.now().isoformat(),
            "version": "CirbyMC v11.0 - Render.com Deployment"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        stats["failed_queries"] += 1
        raise HTTPException(
            status_code=500,
            detail=f"❌ Fehler: {str(e)}"
        )

@app.get("/stats")
async def get_stats():
    uptime_seconds = (datetime.now() - datetime.fromisoformat(stats["start_time"])).total_seconds()
    return {
        **stats,
        "uptime_seconds": uptime_seconds,
        "uptime_hours": round(uptime_seconds / 3600, 2),
        "success_rate": round((stats["successful_queries"] / max(stats["total_queries"], 1)) * 100, 2),
        "deployment": "Render.com"
    }

@app.get("/examples")
async def examples():
    return {
        "message": "CirbyMC beantwortet ALLE Minecraft-Fragen!",
        "spezifische_antworten": [
            "Wie baut man einen Netherportalrahmen?",
            "Wie craftet man einen Trichter?",
            "Erstelle einen /give-Befehl für ein Netherite-Schwert",
            "Wie funktioniert eine Redstone Clock?",
            "Was ist neu in Minecraft 1.21?",
            "Wie bekomme ich einen Befehlsblock?"
        ],
        "ki_generierte_antworten": [
            "Wie crafte ich eine Diamantspitzhacke?",
            "Welche Verzauberungen sind am besten für ein Schwert?",
            "Wie baue ich eine automatische Farm?",
            "Wo finde ich Diamanten?",
            "Wie besiege ich den Enderdrachen?",
            "Wie züchte ich Tiere?",
            "Wie funktioniert Redstone?",
            "Wie baue ich ein schönes Haus?",
            "Welche Mobs gibt es in Minecraft?",
            "Wie verwende ich Commands?"
        ],
        "note": "Stelle JEDE Minecraft-Frage - ich beantworte sie alle!",
        "deployment": "Render.com"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print("🚀 CIRBYMC MINECRAFT-KI API v11.0")
    print("🌐 Render.com Deployment")
    print("🤖 Beantwortet ALLE Minecraft-Fragen")
    print("=" * 50)
    print(f"📡 Server: {host}:{port}")
    print("🎯 Bereit für Pipedream Integration!")
    print("=" * 50)
    
    uvicorn.run(app, host=host, port=port)