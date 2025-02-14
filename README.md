# Friday - AI Voice Assistant

## Overview
Friday is an AI-powered voice assistant that can process commands, open websites, fetch the latest news, and respond to user queries using OpenAI's GPT-3.5. It utilizes speech recognition and text-to-speech capabilities to interact with users.

## Features
- **Voice Activation**: Listens for the wake word "Friday" to activate.
- **Website Access**: Opens Google, YouTube, LinkedIn, and Facebook via voice commands.
- **YouTube Search**: Searches and plays videos based on user input.
- **News Updates**: Fetches the latest news headlines using the News API.
- **AI Responses**: Uses OpenAI's GPT-3.5 to generate responses for user queries.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7+
- Required Python libraries: `speech_recognition`, `webbrowser`, `pyttsx3`, `urllib`, `json`, `requests`, `openai`, `dotenv`

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/friday-voice-assistant.git
   cd friday-voice-assistant
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your API keys:
   ```env
   OPENAI_KEY=your_openai_api_key
   NEWS_KEY=your_news_api_key
   ```

4. Run the program:
   ```sh
   python friday.py
   ```

## Usage
1. Start the assistant by running the script.
2. Say **"Friday"** to activate.
3. Speak commands like:
   - "Open Google"
   - "Play Despacito on YouTube"
   - "Get me the latest news"
   - "What is the capital of France?"
4. The assistant will process the command and respond accordingly.

## Dependencies
The project requires the following libraries:
```sh
pip install speechrecognition pyttsx3 requests openai python-dotenv
```

## Troubleshooting
- Ensure your microphone is working properly.
- If API calls fail, verify your API keys in the `.env` file.
- If the assistant doesn’t recognize your voice, try speaking clearly and avoid background noise.

## Contributing
Feel free to submit pull requests and improve the project. Suggestions and feature requests are welcome.

## License
This project is licensed under the MIT License. See `LICENSE` for details.



