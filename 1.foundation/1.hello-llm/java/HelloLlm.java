public class HelloLlm {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("GROQ_API_KEY");

        if (apiKey == null || apiKey.isEmpty()) {
            throw new IllegalArgumentException("GROQ_API_KEY environment variable is not set.");
        }

        String url = "https://api.groq.com/openai/v1/chat/completions";

        String requestBody = """
        {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                { "role": "user", "content": "Hello LLM!" }
            ]
        }
        """;

        java.net.http.HttpClient client = java.net.http.HttpClient.newHttpClient();
        java.net.http.HttpRequest request = java.net.http.HttpRequest.newBuilder()
                .uri(java.net.URI.create(url))
                .header("Authorization", "Bearer " + apiKey)
                .header("Content-Type", "application/json")
                .POST(java.net.http.HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        java.net.http.HttpResponse<String> response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
        System.out.println("Response: " + response.body());
    }
}
