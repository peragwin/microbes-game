# vLLM Vision Host Server

This directory contains the code for the vLLM (Vision Large Language Model) Host Server.

## Purpose

This server provides a simple API endpoint for the main Unity application to query for visual analysis of the game world. It's designed to be a stateless microservice that receives data, processes it, and returns a structured analysis.

## API

-   **Endpoint:** `/analyze`
-   **Method:** `POST`
-   **Description:** Receives visual data (e.g., a screenshot or scene description) and returns a mock JSON object describing the state of the game world and the microbes within it.

## Running the Server

1.  Navigate to this directory (`vllm_server`).
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server using Uvicorn:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

The server will be available at `http://localhost:8000`.
