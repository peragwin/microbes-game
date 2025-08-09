using UnityEngine;
using System.Collections.Generic;
// using System.Net.Http; // Uncomment for HttpClient
// using System.Text; // Uncomment for JSON serialization
// using M2Mqtt; // Example MQTT client library, will depend on the asset used in Unity

public class GameController : MonoBehaviour
{
    public static GameController Instance { get; private set; }

    [Header("Game State")]
    [Range(-100, 100)]
    [Tooltip("Overall state of the gut biome. -100 is dysbiosis, 100 is harmony.")]
    public float harmonyLevel;

    public List<Microbe> microbes = new List<Microbe>();

    // private static readonly HttpClient client = new HttpClient(); // For making API calls

    // private MqttClient mqttClient; // For MQTT communication

    void Awake()
    {
        // Singleton pattern to ensure only one GameController exists
        if (Instance != null && Instance != this)
        {
            Destroy(this.gameObject);
        }
        else
        {
            Instance = this;
        }
    }

    void Start()
    {
        Debug.Log("Game Controller started. Current harmony level: " + harmonyLevel);
        // ConnectToMqttBroker();
    }

    // --- Placeholder methods for server communication ---

    public void RequestChatResponse(string userMessage)
    {
        // TODO: Implement API call to the chat_server
        // 1. Construct JSON payload with the message and current game state.
        //    string gameStateJson = JsonUtility.ToJson(this);
        //    string payload = $"{{\"message\": \"{userMessage}\", \"state\": {gameStateJson}}}";
        // 2. Send POST request to "http://localhost:8001/chat" (or your chat server's address).
        //    var content = new StringContent(payload, Encoding.UTF8, "application/json");
        //    var response = await client.PostAsync("http://localhost:8001/chat", content);
        // 3. Deserialize the response, which may contain an action to execute.
        //    string responseJson = await response.Content.ReadAsStringAsync();
        //    // Parse responseJson and call ExecuteGameAction()
        Debug.Log("Placeholder: Requesting chat response for: " + userMessage);
    }

    public void RequestVllmAnalysis()
    {
        // TODO: Implement API call to the vllm_server
        // 1. Capture a screenshot or relevant visual data.
        // 2. Send POST request to "http://localhost:8000/analyze".
        // 3. Receive and process the analysis.
        Debug.Log("Placeholder: Requesting VLLM analysis.");
    }

    public void ExecuteGameAction(string action, Dictionary<string, object> parameters)
    {
        // TODO: Implement logic to execute actions returned by the chat server.
        // Example:
        // if (action == "INCREASE_HARMONY") {
        //     harmonyLevel += (float)parameters["amount"];
        // }
        Debug.Log($"Placeholder: Executing action '{action}' with parameters.");
    }


    // --- Placeholder methods for MQTT communication ---

    private void ConnectToMqttBroker()
    {
        // TODO: Implement MQTT connection logic.
        // The specifics will depend on the Unity MQTT asset you choose.
        // string brokerAddress = "localhost";
        // mqttClient = new MqttClient(brokerAddress);
        // mqttClient.Connect("UnityClient");
        Debug.Log("Placeholder: Connecting to MQTT broker.");
    }

    public void SendMqttCommand(int microbeId, string command)
    {
        // TODO: Implement MQTT publish logic.
        // The topic could be something like $"microbes/{microbeId}/command"
        // string topic = $"microbes/{microbeId}/command";
        // mqttClient.Publish(topic, Encoding.UTF8.GetBytes(command));
        Debug.Log($"Placeholder: Sending MQTT command '{command}' to microbe {microbeId}.");
    }
}
