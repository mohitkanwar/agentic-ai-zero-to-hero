# Running the Java Code

## Steps

1. **Define the API key**  
   Set your API key as an environment variable or in the code as required.

2. **Compile the code**  
   Use the following command in your terminal inside the folder where the class is present.:
   ```sh
   javac HelloLlm.java
   ```

3. **Run the code**  
   Execute the compiled program:
   ```sh
   java HelloLlm
   ```

To run the class from the command line and provide the environment variable, use:

```sh
GROQ_API_KEY=your_api_key_here java HelloLlm
```

Replace `your_api_key_here` with your actual API key and `path/to/classes` with the directory or jar containing the compiled class.