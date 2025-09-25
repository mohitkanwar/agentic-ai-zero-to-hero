// Hellollm.js

/**
 * Calls the Groq LLM API and logs the response.
 * Requires GROQ_API_KEY to be set in your environment variables.
 */
async function callGroqChat() {
  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    console.error("Error: GROQ_API_KEY environment variable not set.");
    return;
  }

  try {
  const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: "llama-3.3-70b-versatile",
      messages: [
        { role: "user", content: "Hello LLM!" }
      ]
    })
  });

    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }

  const data = await response.json();
  console.log("Groq says:", data.choices[0].message.content);
  } catch (error) {
    console.error("Failed to call Groq API:", error.message);
  }
}

module.exports = { callGroqChat };

callGroqChat()