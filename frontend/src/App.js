import React, { useState, useEffect } from 'react';
import ChatInterface from './components/ChatInterface';
import './App.css';

function App() {
  const [sessionId, setSessionId] = useState(null);

  useEffect(() => {
    // Generate a session ID on component mount
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
  }, []);

  const handleReset = () => {
    // Generate new session ID to reset the chat
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
  };

  return (
    <div className="App">
      <div className="app-container">
        <header className="app-header">
          <div className="header-content">
            <div className="logo-container">
              <svg className="logo-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 6H17V4C17 2.9 16.1 2 15 2H9C7.9 2 7 2.9 7 4V6H4C2.9 6 2 6.9 2 8V20C2 21.1 2.9 22 4 22H20C21.1 22 22 21.1 22 20V8C22 6.9 21.1 6 20 6ZM9 4H15V6H9V4ZM20 20H4V8H20V20Z" fill="currentColor"/>
                <path d="M12 9C10.34 9 9 10.34 9 12C9 13.66 10.34 15 12 15C13.66 15 15 13.66 15 12C15 10.34 13.66 9 12 9ZM12 13C11.45 13 11 12.55 11 12C11 11.45 11.45 11 12 11C12.55 11 13 11.45 13 12C13 12.55 12.55 13 12 13Z" fill="currentColor"/>
                <path d="M7 18H17V16H7V18Z" fill="currentColor"/>
              </svg>
              <div>
                <h1>Healthcare Bot</h1>
                <p className="subtitle">Medical Diagnosis Expert System</p>
              </div>
            </div>
            <button className="reset-button" onClick={handleReset} title="Start New Consultation">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4C7.58 4 4.01 7.58 4.01 12C4.01 16.42 7.58 20 12 20C15.73 20 18.84 17.45 19.73 14H17.65C16.83 16.33 14.61 18 12 18C8.69 18 6 15.31 6 12C6 8.69 8.69 6 12 6C13.66 6 15.14 6.69 16.22 7.78L13 11H20V4L17.65 6.35Z" fill="currentColor"/>
              </svg>
              New Chat
            </button>
          </div>
        </header>
        
        <main className="app-main">
          {sessionId && <ChatInterface sessionId={sessionId} key={sessionId} />}
        </main>
        
        <footer className="app-footer">
          <p className="disclaimer">
            ⚠️ <strong>Disclaimer:</strong> This is an AI-assisted diagnostic tool for educational purposes only. 
            Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment.
          </p>
        </footer>
      </div>
    </div>
  );
}

export default App;
