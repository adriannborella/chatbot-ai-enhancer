// src/components/SpeechRecognition.js
import React, {useState, useRef, useEffect} from 'react';
import axios from 'axios';

const SpeechRecognition = ({onTextRecognized, onNlpResponse}) => {
  const [recording, setRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [randomText, setRandomText] = useState('');
  const [error, setError] = useState('');
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  useEffect(() => {
    getRandomText();
  }, []);

  const handleRecordingStart = async () => {
    setRecording(true);
    setError('');

    const stream = await navigator.mediaDevices.getUserMedia({audio: true});
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder;
    audioChunksRef.current = [];

    mediaRecorder.ondataavailable = (event) => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunksRef.current, {type: 'audio/wav'});
      setAudioBlob(audioBlob);
    };

    mediaRecorder.start();
  };

  const getRandomText = async () => {
    try {
      const response = await fetch('http://localhost:8000/core/random-text/');
      const data = await response.json();
      setRandomText(data.random_text);
    } catch (error) {
      console.error('Error fetching random text:', error);
    }
  };

  const handleRecordingStop = () => {
    setRecording(false);
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
    }
  };

  const handleUploadAudio = async () => {
    if (!audioBlob) return;
    const formData = new FormData();
    formData.append('audio', audioBlob, 'recording.wav');
    formData.append('random_text', randomText);

    try {
      const response = await axios.post(
        'http://localhost:8000/core/recognize_speech/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
      );
      if (response.data.error) {
        setError(response.data.error);
      } else {
        onTextRecognized(response.data.text);
        const nlpResponse = await axios.get(
          'http://localhost:8000/core/analyze_text/',
          {
            params: {text: response.data.text},
          },
        );
        if (nlpResponse.data.error) {
          setError(nlpResponse.data.error);
        } else {
          onNlpResponse(nlpResponse.data.choices[0].text);
        }
      }
    } catch (err) {
      setError('An error occurred while recognizing speech');
    }
  };

  return (
    <div className="speech-recognition">
      <button onClick={getRandomText}>Get Random Text</button>
      <div>
        <p>{randomText}</p>
      </div>
      <div className="controls">
        <button
          onClick={recording ? handleRecordingStop : handleRecordingStart}
        >
          {recording ? 'Stop Recording' : 'Start Recording'}
        </button>
        {audioBlob && (
          <div className="audio-controls">
            <audio src={URL.createObjectURL(audioBlob)} controls />
            <button onClick={handleUploadAudio}>Upload Audio</button>
          </div>
        )}
      </div>
      {error && <p style={{color: 'red'}}>{error}</p>}
    </div>
  );
};

export default SpeechRecognition;
