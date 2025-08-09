# Microbes Interactive Art/Game

An AI-driven, narrative-rich interactive installation exploring **basal human desires** through the lens of exaggerated microbial personalities.  
Designed for the _"The Body"_ festival theme, the experience invites players/participants to engage with a living, reactive ecosystem of crocheted animatronic microbes — each representing a core need taken to the extreme.

---

## Concept Overview

The installation consists of five main **microbe characters**, each embodying a specific exaggerated human drive:

1. **Community** — _Psychic fungal hive-mind_

   - Represents: belonging, social connection, collective consciousness.
   - Personality: empathetic, all-knowing, a little clingy.
   - Interaction themes: group coordination, social energy sensing.

2. **Hunger** — _Gluttonous gas-producing bacteria_

   - Represents: overconsumption, insatiable appetite, chaotic cravings.
   - Personality: playful yet reckless, always searching for snacks.
   - Interaction themes: feeding mechanics, smell/gas effects.

3. **Reproduction** — _Horny exponential growth bacteria_

   - Represents: lust, thrill of exchange, compulsive multiplication.
   - Personality: dopamine-chasing, high-energy, flirtatious.
   - Interaction themes: proximity triggers, "gene exchange" mini-events.

4. **Relationships** — _Co-dependent tapeworm_

   - Represents: attachment, neediness, mutual reliance.
   - Personality: clingy, slightly manipulative, thrives when “latched on.”
   - Interaction themes: one-to-one bonding, attachment-based progression.

5. **Mastery** — _Control-obsessed virus_
   - Represents: domination, structure, hierarchy.
   - Personality: strategic, authoritarian, power-hungry.
   - Interaction themes: issuing commands, taking over other microbes.

---

## Artistic Goals

- **Theme**: exaggerated human needs as microbial archetypes.
- **Setting**: immersive “inside the body” space — crocheted organic textures, lighting effects, soundscape.
- **Narrative Question**: _Can the microbiota find a way to live in harmony, or will one dominate?_
- **Player Agency**: influence the balance of power between microbes through interactions.
- **Outcome Variability**: harmony, domination, or chaos depending on collective interactions.

---

## Interaction Design

- **Physical Animatronics**
  - Crocheted microbial bodies conceal mechanical/robotic movement systems.
  - Potential actuation: servo-based puppet motion, small robot arm cores, vibration motors.
- **Sensing & Tracking**
  - Camera + vision models for **real-time user detection & recognition**.
  - Face detection/tagging with vector embeddings for repeat visitor identification.
  - Microphone for live audio cues / voice interactions.
- **AI Behavior**

  - Each microbe runs as an **AI agent** with unique personality prompt & memory.
  - Agents react to:
    - Proximity & movement
    - Voice & facial recognition
    - Cross-agent interactions
  - Potential architecture: local LLM core + vision/audio inference + real-time event loop.

- **Game-Like Layer**
  - Multiple agents influencing shared “body state” variables.
  - Users’ actions shift inter-microbe balance.
  - End-state narrative (harmony vs. domination) emerges over session.

---

## Technical Goals & Architecture

### Core Components

- **Agent Engine**

  - Runs 5 independent AI agents with personality prompts.
  - Maintains short-term context + long-term memory.
  - Cross-communication between agents to simulate microbial politics.

- **Sensing**

  - **Vision**: object/person detection, tracking, expression/body language inference.
  - **Audio**: real-time voice activity detection (VAD) + transcription (e.g., ElevenLabs Scribe).
  - **ID Memory**: persistent tags for recognized faces to carry interaction history.

- **Control**

  - Animatronic control via microcontrollers or small SBCs (ESP32, Raspberry Pi).
  - Event-based actuation tied to AI agent emotional state.

- **Networking**
  - Possible central orchestrator service connecting sensors, AI, and animatronic controllers.

### Possible Stack

- **Hardware**:
  - Crocheted shells around 3D-printed or modular animatronic rigs.
  - USB cameras for vision input.
  - Servo/stepper motors controlled via Arduino/ESP32 or Pi HAT.
- **Software**:
  - Python orchestrator for event routing.
  - Unity/Unreal optional for projection-mapped overlays or hybrid digital display.
  - Coordinated LED lighting in the room (using chroma.tech canopy)
- **AI Models**:
  - Vision: DeepFace (face recognition) and player identity tracking. VLM running locally (or in a private cloud container), likely Gemma or Qwen running with vLLM.
  - Audio: VAD + ElevenLabs Scribe or Whisper for STT.
  - LLM: Most likely chatgpt providing conversational responses in character. Vision analysis and game state is fed into the LLM as context.

---

## Current State

- **Narrative & Characters**: Core microbe archetypes finalized.
- **Art Direction**: Crocheted bodies planned; aesthetic is warm, organic, tactile.
- **Interaction Goals**: Player agency through physical proximity, voice, and recognition.
- **Technical Research**:
  - Investigating DeepFace for multi-person detection & recognition.
  - Considering real-time LLM loop with vision/audio context injection.
  - Exploring animatronic actuation options (servo rigs, robot arms, vibration).

---

## Roadmap

### Short-Term

1. **Repo Bootstrapping** — create codebase structure for agents, sensors, controllers.
2. **Agent Personality Prompts** — draft prompt templates for all five microbes.
3. **Basic Sensing Pipeline** — implement camera input + person detection + face embeddings.
4. **Animatronic Test Rig** — build minimal prototype crochet puppet with servo motion.

### Mid-Term

5. **Multi-Agent Coordination** — inter-agent message passing & influence system.
6. **Narrative State Tracking** — persistent variables for harmony vs. domination.
7. **User Memory System** — store history per visitor to affect microbe behavior.

### Long-Term

8. **Full Installation Integration** — link all microbes, orchestrator, and physical environment.
9. **Festival Deployment** — optimize for reliability and minimal supervision.

---

## License

TBD — choose based on project goals (art installation, open-source, etc.)
