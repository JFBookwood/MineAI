"""
🎮 ENHANCED MINECRAFT AI v12.0
- Beantwortet ALLE Fragen (nicht nur Minecraft)
- Deutsch + Englisch Support
- Minecraft-fokussiert aber flexibel
- Für ActivePieces Integration optimiert
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random
import datetime

app = FastAPI(
    title="Enhanced Minecraft AI v12.0",
    description="Minecraft-fokussierte KI die ALLE Fragen beantwortet",
    version="12.0"
)

# CORS für alle Origins erlauben
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

def get_enhanced_answer(question):
    """
    Enhanced Minecraft AI - beantwortet ALLE Fragen
    Bleibt Minecraft-fokussiert aber ist flexibel
    """
    
    question_lower = question.lower().strip()
    
    # Leere Frage abfangen
    if not question_lower:
        return get_general_minecraft_help()
    
    # SPEZIFISCHE MINECRAFT FRAGEN (wie vorher)
    minecraft_answer = get_specific_minecraft_answer(question_lower)
    if minecraft_answer:
        return minecraft_answer
    
    # ALLGEMEINE FRAGEN MIT MINECRAFT-BEZUG
    return get_general_answer_with_minecraft_context(question, question_lower)

def get_specific_minecraft_answer(question_lower):
    """Spezifische Minecraft-Antworten (bestehende Logik)"""
    
    # Nether-Portal
    if ('nether' in question_lower and 'portal' in question_lower) or 'netherportal' in question_lower:
        return """**🔥 Nether-Portal bauen:**

**📋 Materialien:**
• **10 Obsidian-Blöcke** (für 4x5 Rahmen)
• **1 Feuerzeug** (zum Aktivieren)

**⛏️ Obsidian beschaffen:**
• Wasser auf Lava-Quelle → wird zu Obsidian
• Mit **Diamant-Spitzhacke** abbauen (15 Sek.)
• Andere Werkzeuge zerstören ohne Drop!

**🏗️ Aufbau:**
1. **Basis:** 4 Obsidian horizontal
2. **Seiten:** Je 3 Obsidian vertikal
3. **Dach:** 4 Obsidian horizontal
4. **Aktivieren:** Feuerzeug in Rahmen

**💡 Tipp:** Erst in Overworld bauen - sicherer!

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # Diamant-Werkzeuge
    elif 'diamant' in question_lower and ('spitzhacke' in question_lower or 'pickaxe' in question_lower):
        return """**💎 Diamant-Spitzhacke craften:**

**📋 Materialien:**
• **3x Diamanten** (Diamonds)
• **2x Stöcke** (Sticks)

**🏗️ Crafting-Rezept:**
```
[D] [D] [D]
[ ] [S] [ ]
[ ] [S] [ ]
```
D = Diamant, S = Stock

**⚡ Eigenschaften:**
• **Haltbarkeit:** 1.561 Verwendungen
• **Geschwindigkeit:** Sehr schnell
• **Kann abbauen:** Alle Blöcke (außer Bedrock)
• **Verzauberbar:** Ja (Effizienz, Glück, etc.)

**💡 Profi-Tipps:**
• Mit **Haltbarkeit III** verzaubern → 6.244 Verwendungen
• **Effizienz V** → Noch schneller abbauen
• **Glück III** → Mehr Drops (z.B. mehr Diamanten)

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # Redstone Grundlagen
    elif 'redstone' in question_lower:
        return """**⚡ Redstone Grundlagen:**

**🔧 Basis-Komponenten:**
• **Redstone-Staub** → Leitet Signal weiter (15 Blöcke)
• **Redstone-Fackel** → Dauerhaftes Signal
• **Hebel/Knopf** → Signal ein/ausschalten
• **Druckplatte** → Aktiviert durch Gewicht

**🎛️ Logik-Gatter:**
• **NOT-Gatter** → Redstone-Fackel (invertiert Signal)
• **AND-Gatter** → Beide Eingänge müssen aktiv sein
• **OR-Gatter** → Ein Eingang reicht

**🏗️ Praktische Anwendungen:**
• **Automatische Türen** → Druckplatte + Kolben
• **Fallen** → Tripwire + Dispenser
• **Farmen** → Timer + Kolben/Wasser
• **Beleuchtung** → Tageslicht-Sensor + Lampen

**💡 Anfänger-Projekt:**
Automatische Tür mit Druckplatte!

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # Weitere spezifische Antworten...
    elif 'enderdrache' in question_lower or 'ender dragon' in question_lower:
        return """**🐉 Enderdrache besiegen:**

**🎯 Vorbereitung:**
• **Diamant/Netherite-Ausrüstung** (vollständig)
• **Bogen + 64+ Pfeile** (oder Armbrust)
• **Essen** (Goldene Äpfel, Steaks)
• **Tränke** (Heilung, Stärke, Langsamkeit)
• **Blöcke** zum Bauen (64+ Kopfsteinpflaster)

**🏗️ End-Portal finden:**
• **Enderaugen** werfen → Folge der Richtung
• **Festung** finden → End-Portal aktivieren
• **12 Enderaugen** in Portal-Rahmen setzen

**⚔️ Kampf-Strategie:**
1. **End-Kristalle** zerstören (auf Obsidian-Türmen)
2. **Drache angreifen** wenn er landet
3. **Schutz suchen** bei Atem-Attacke
4. **Geduldig bleiben** - dauert 5-10 Minuten

**🏆 Belohnung:**
• **Drachenei** (Trophäe)
• **Viel XP** (12.000 Punkte)
• **End-Gateway** → Äußere End-Inseln

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    return None  # Keine spezifische Antwort gefunden

def get_general_answer_with_minecraft_context(original_question, question_lower):
    """Beantwortet allgemeine Fragen mit Minecraft-Kontext"""
    
    # GRÜSSE UND HÖFLICHKEIT
    if any(greeting in question_lower for greeting in ['hallo', 'hi', 'hey', 'guten tag', 'hello', 'good morning']):
        return f"""**🎮 Hallo! Willkommen bei CirbyMC's Enhanced AI!**

Du hast gefragt: "{original_question}"

**🌟 Ich bin deine Minecraft-KI und helfe dir bei:**
• **Crafting-Rezepten** → "Wie crafte ich X?"
• **Überlebens-Tipps** → "Wie überlebe ich die erste Nacht?"
• **Redstone-Mechaniken** → "Wie funktioniert Redstone?"
• **Boss-Kämpfe** → "Wie besiege ich den Enderdrachen?"
• **Bau-Projekte** → "Wie baue ich eine Burg?"
• **Farmen** → "Wie baue ich eine automatische Farm?"

**💡 Aber auch allgemeine Fragen beantworte ich gerne!**

**🎯 Beispiel-Fragen:**
• "Wie crafte ich eine Diamant-Spitzhacke?"
• "Was ist das beste Essen in Minecraft?"
• "Wie finde ich Diamanten?"
• "Erkläre mir Redstone"

**🚀 Frag mich einfach alles - ich bin hier um zu helfen!**

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # MATHEMATIK MIT MINECRAFT-BEZUG
    elif any(math_word in question_lower for math_word in ['rechnen', 'mathematik', 'plus', 'minus', 'mal', 'geteilt', 'calculate', 'math']):
        return f"""**🧮 Mathematik-Hilfe mit Minecraft-Bezug:**

Du fragst: "{original_question}"

**🎮 Minecraft-Mathe-Beispiele:**
• **Crafting-Mengen:** 1 Diamant-Spitzhacke = 3 Diamanten + 2 Stöcke
• **Bau-Berechnungen:** Haus 10x10 = 100 Blöcke für Boden
• **Farm-Effizienz:** 1 Weizen-Farm 9x9 = 81 Ackerboden
• **Redstone-Timing:** 1 Redstone-Tick = 0,1 Sekunden

**💡 Konkrete Mathe-Frage?**
Stelle sie mir und ich erkläre sie mit Minecraft-Beispielen!

**🔢 Beispiele:**
• "Wie viele Blöcke brauche ich für ein 20x20 Haus?"
• "Wie lange dauert es 64 Eisenerz zu schmelzen?"
• "Wie viel XP gibt der Enderdrache?"

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # WISSENSCHAFT MIT MINECRAFT-BEZUG
    elif any(science_word in question_lower for science_word in ['physik', 'chemie', 'biologie', 'wissenschaft', 'physics', 'chemistry', 'biology', 'science']):
        return f"""**🔬 Wissenschaft trifft Minecraft:**

Du fragst: "{original_question}"

**🎮 Minecraft-Wissenschaft:**
• **Physik:** Schwerkraft (Sand/Kies fallen), Wasser-Mechanik, Redstone-Elektrizität
• **Chemie:** Brauen (Tränke mischen), Schmelzen (Erze → Barren)
• **Biologie:** Mob-Verhalten, Pflanzen-Wachstum, Tierzucht

**⚗️ Praktische Beispiele:**
• **Tränke brauen** = Chemie-Labor
• **Redstone-Schaltungen** = Elektronik
• **Mob-Farmen** = Verhaltensbiologie
• **Automatische Farmen** = Landwirtschaft

**💡 Spezifische Wissenschafts-Frage?**
Ich erkläre sie gerne mit Minecraft-Beispielen!

**🧪 Beispiele:**
• "Wie funktioniert Redstone physikalisch?"
• "Welche Tränke-Kombinationen gibt es?"
• "Wie züchte ich Tiere effizient?"

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # PROGRAMMIERUNG MIT MINECRAFT-BEZUG
    elif any(prog_word in question_lower for prog_word in ['programmieren', 'code', 'programming', 'python', 'javascript', 'html']):
        return f"""**💻 Programmierung trifft Minecraft:**

Du fragst: "{original_question}"

**🎮 Minecraft & Programmierung:**
• **Command Blocks** = Minecraft-Programmierung
• **Redstone** = Logische Schaltungen (wie Code)
• **Mods erstellen** = Java/Python Programmierung
• **Server-Plugins** = Bukkit/Spigot Development

**⚡ Redstone = Programmier-Logik:**
• **IF-THEN** → Redstone-Komparator
• **Loops** → Clock-Schaltungen
• **Variables** → Redstone-Signalstärke
• **Functions** → Redstone-Module

**💡 Programmier-Projekt Ideen:**
• **Minecraft-Bot** (Python)
• **Server-Plugin** (Java)
• **Redstone-Computer** (In-Game)
• **Mod Development** (Forge/Fabric)

**🚀 Konkrete Programmier-Frage?**
Ich helfe gerne mit Minecraft-Beispielen!

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

    # ALLGEMEINE FRAGEN
    else:
        return f"""**🤔 Interessante Frage!**

Du fragst: "{original_question}"

**🎮 Als Minecraft-KI denke ich dabei an:**

{get_minecraft_connection_for_general_question(question_lower)}

**💡 Aber lass mich auch allgemein antworten:**
{get_general_response(original_question, question_lower)}

**🎯 Für spezifische Minecraft-Hilfe frag gerne:**
• "Wie crafte ich...?"
• "Wie funktioniert...?"
• "Wie besiege ich...?"
• "Wie baue ich...?"

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

def get_minecraft_connection_for_general_question(question_lower):
    """Findet Minecraft-Verbindungen zu allgemeinen Fragen"""
    
    if any(word in question_lower for word in ['wetter', 'weather', 'regen', 'rain']):
        return "**🌧️ Minecraft hat auch Wetter!** Regen füllt Kessel, Blitze können Creeper zu Charged Creepern machen!"
    
    elif any(word in question_lower for word in ['zeit', 'time', 'uhr', 'clock']):
        return "**🕐 Minecraft-Zeit:** 1 Minecraft-Tag = 20 Minuten real! Du kannst Uhren craften um die Zeit zu sehen."
    
    elif any(word in question_lower for word in ['essen', 'food', 'hunger', 'kochen']):
        return "**🍖 Minecraft-Essen:** Von rohem Fleisch bis zu Goldenen Äpfeln - Essen ist überlebenswichtig!"
    
    elif any(word in question_lower for word in ['musik', 'music', 'sound']):
        return "**🎵 Minecraft-Musik:** Noteblöcke, Jukeboxes und die entspannende Hintergrundmusik von C418!"
    
    elif any(word in question_lower for word in ['farben', 'colors', 'bunt']):
        return "**🌈 Minecraft-Farben:** 16 verschiedene Wolle-Farben, bunte Betten, Glas und Keramik!"
    
    elif any(word in question_lower for word in ['tiere', 'animals', 'pets']):
        return "**🐕 Minecraft-Tiere:** Hunde, Katzen, Pferde, Papageien - alle zähmbar und als Begleiter!"
    
    else:
        return "**🎮 In Minecraft gibt es bestimmt auch etwas Ähnliches!** Die Welt ist riesig und voller Überraschungen."

def get_general_response(original_question, question_lower):
    """Allgemeine Antworten auf nicht-Minecraft Fragen"""
    
    responses = [
        f"Das ist eine spannende Frage! Auch wenn ich hauptsächlich Minecraft-Experte bin, denke ich: {original_question} ist ein interessantes Thema das viele Aspekte hat.",
        
        f"Gute Frage! '{original_question}' ist definitiv ein Thema über das man viel diskutieren könnte. In Minecraft würde ich das anders angehen, aber allgemein gesehen gibt es viele Perspektiven dazu.",
        
        f"Interessant dass du nach '{original_question}' fragst! Das zeigt dass du neugierig bist - genau wie ein guter Minecraft-Spieler der die Welt erkundet.",
        
        f"'{original_question}' - das ist eine Frage die zeigt dass du über den Tellerrand hinausdenkst! Auch in Minecraft ist Kreativität und Neugier der Schlüssel zum Erfolg."
    ]
    
    return random.choice(responses)

def get_general_minecraft_help():
    """Standard Minecraft-Hilfe für leere Fragen"""
    return """**🎮 Minecraft Allgemein-Guide:**

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

🎮 CirbyMC's Enhanced AI v12.0! ⛏️"""

# API ENDPOINTS
@app.get("/")
async def root():
    return {
        "message": "🎮 Enhanced Minecraft AI v12.0 - Beantwortet ALLE Fragen!",
        "version": "12.0",
        "features": [
            "Spezifische Minecraft-Antworten",
            "Allgemeine Fragen mit Minecraft-Kontext", 
            "Deutsch + Englisch Support",
            "Erweiterte Flexibilität"
        ],
        "endpoints": {
            "/query/simple": "POST - Stelle eine Frage",
            "/health": "GET - Server Status",
            "/examples": "GET - Beispiel-Fragen"
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "Enhanced Minecraft AI v12.0",
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/query/simple")
async def query_simple(query: Query):
    try:
        # Leere Fragen mit Standard-Antwort behandeln
        if not query.question or not query.question.strip():
            answer = get_general_minecraft_help()
        else:
            answer = get_enhanced_answer(query.question)
        
        return {
            "answer": answer,
            "timestamp": datetime.datetime.now().isoformat(),
            "version": "CirbyMC Enhanced AI v12.0"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler bei der Antwort-Generierung: {str(e)}")

@app.get("/examples")
async def examples():
    return {
        "minecraft_specific": [
            "Wie crafte ich eine Diamant-Spitzhacke?",
            "Wie baue ich ein Nether-Portal?",
            "Wie besiege ich den Enderdrachen?",
            "Wie funktioniert Redstone?"
        ],
        "general_with_minecraft": [
            "Hallo, wie geht's?",
            "Was ist 2+2?",
            "Erkläre mir Physik",
            "Wie programmiert man?",
            "Was ist das Wetter heute?"
        ],
        "multilingual": [
            "How do I craft a diamond pickaxe?",
            "Hello, how are you?",
            "What is the weather like?",
            "Explain programming to me"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)