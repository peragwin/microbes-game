using UnityEngine;
using System.Collections.Generic;

public class Microbe : MonoBehaviour
{
    [Header("Microbe Stats")]
    public string microbeName;
    public int microbeId;

    [Tooltip("Represents the microbe's influence on the overall gut harmony.")]
    public float influence;

    [Tooltip("A list of traits that define the microbe's current behavior.")]
    public List<string> behavioralTraits = new List<string>();

    // Example of a unique stat for a specific microbe
    public float specialStat;

    void Start()
    {
        // Initialization logic for the microbe can go here.
        Debug.Log($"Microbe '{microbeName}' with ID {microbeId} has been initialized.");
    }

    void Update()
    {
        // Per-frame logic for the microbe can go here.
        // For example, its behavior could change based on its traits.
    }

    public void UpdateBehavior(string newBehavior)
    {
        if (!behavioralTraits.Contains(newBehavior))
        {
            behavioralTraits.Add(newBehavior);
            Debug.Log($"Microbe '{microbeName}' adopted a new behavior: {newBehavior}");
        }
    }
}
