
# Hello LLM (JavaScript)

A minimal example showing how to call Groq Chat from Node.js.

Prerequisites:
1. Node.js (v18+ recommended)
2. A valid `GROQ_API_KEY`

Setup:
- macOS terminal (example): `export GROQ_API_KEY=your_api_key_here`
- Or prefix the command when running: `GROQ_API_KEY=your_api_key_here node Hellollm.js`

Run:
- From the project root: `node Hellollm.js`

Or import from another script:
- ```javascript
  const { callGroqChat } = require('./Hellollm');
  callGroqChat();
  ```