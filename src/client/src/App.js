// src/App.js
import React, {useState} from 'react';
import './App.css';
import SpeechRecognition from './components/SpeechRecognition';

function App() {
  const [messages, setMessages] = useState([]);
  const [recognizedText, setRecognizedText] = useState('');

  const handleTextRecognized = (text) => {
    setMessages([...messages, {type: 'user', text}]);
    setRecognizedText(text);
  };

  const handleNlpResponse = (response) => {
    setMessages([...messages, {type: 'bot', text: response}]);
  };

  return (
    <div className="App">
      <div className="chat-window">
        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.type}`}>
              <div className="message-content">{message.text}</div>
            </div>
          ))}
        </div>
        <SpeechRecognition
          onTextRecognized={handleTextRecognized}
          onNlpResponse={handleNlpResponse}
        />
      </div>
    </div>
  );
}

export default App;
