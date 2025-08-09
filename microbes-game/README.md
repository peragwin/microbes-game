# Microbes Game

This repository contains the scaffold for the "Microbes Game", a project that combines a Unity game with several external services to create an interactive experience.

## Project Structure

The project is organized as a monorepo with the following components:

-   **/unity_scripts**: Contains the C# scripts for the Unity game client. Unity is the central component, responsible for managing the game state.
-   **/vllm_server**: A Python server responsible for providing visual analysis of the game world.
-   **/chat_server**: A Python server that handles the conversational AI, using OpenAI's API to generate responses and trigger in-game actions.
-   **/physical_controllers**: Contains MicroPython code for ESP32 microcontrollers that control the physical animatronics of the microbes.

## Architecture Overview

1.  **Unity (State Manager)**: The Unity application is the source of truth for all game state. It passes state information to the other services and receives data to update the game world.
2.  **Stateless Services**: The `vllm_server` and `chat_server` are stateless Python APIs. They receive context from Unity, perform their specific tasks (vision analysis, chat), and return the results.
3.  **Physical World Connection**: Unity communicates with the physical microbe animatronics by sending commands to the `physical_controllers` via an MQTT message broker.

This structure keeps the game logic centralized in Unity while delegating specialized tasks to external microservices.
