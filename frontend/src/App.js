import React, { useState, useEffect } from 'react';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import ChatInterface from './components/ChatInterface';
import LoginPage from './components/LoginPage';
import HistoryPage from './components/HistoryPage';
import './App.css';

function AppContent() {
  const [sessionId, setSessionId] = useState(null);
  const [showHistory, setShowHistory] = useState(false);
  const { user, logout, isAuthenticated } = useAuth();

  useEffect(() => {
    // Generate a session ID on component mount
    if (isAuthenticated) {
      setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
    }
  }, [isAuthenticated]);

  const handleReset = () => {
    // Generate new session ID to reset the chat
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
    setShowHistory(false);
  };

  const handleLogout = () => {
    logout();
    setSessionId(null);
    setShowHistory(false);
  };

  if (!isAuthenticated) {
    return <LoginPage />;
  }

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
                <p className="subtitle">Welcome, {user.username}!</p>
              </div>
            </div>
            <div className="header-actions">
              {!showHistory && (
                <button className="history-button" onClick={() => setShowHistory(true)} title="View Medical History">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13 3C8.03 3 4 7.03 4 12H1L4.89 15.89L4.96 16.03L9 12H6C6 8.13 9.13 5 13 5C16.87 5 20 8.13 20 12C20 15.87 16.87 19 13 19C11.07 19 9.32 18.21 8.06 16.94L6.64 18.36C8.27 19.99 10.51 21 13 21C17.97 21 22 16.97 22 12C22 7.03 17.97 3 13 3ZM12 8V13L16.28 15.54L17 14.33L13.5 12.25V8H12Z" fill="currentColor"/>
                  </svg>
                  History
                </button>
              )}
              {!showHistory && (
                <button className="reset-button" onClick={handleReset} title="Start New Consultation">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4C7.58 4 4.01 7.58 4.01 12C4.01 16.42 7.58 20 12 20C15.73 20 18.84 17.45 19.73 14H17.65C16.83 16.33 14.61 18 12 18C8.69 18 6 15.31 6 12C6 8.69 8.69 6 12 6C13.66 6 15.14 6.69 16.22 7.78L13 11H20V4L17.65 6.35Z" fill="currentColor"/>
                  </svg>
                  New Chat
                </button>
              )}
              <button className="logout-button" onClick={handleLogout} title="Logout">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M17 7L15.59 8.41L18.17 11H8V13H18.17L15.59 15.59L17 17L22 12L17 7ZM4 5H12V3H4C2.9 3 2 3.9 2 5V19C2 20.1 2.9 21 4 21H12V19H4V5Z" fill="currentColor"/>
                </svg>
                Logout
              </button>
            </div>
          </div>
        </header>
        
        <main className="app-main">
          {showHistory ? (
            <HistoryPage onBack={() => setShowHistory(false)} />
          ) : (
            sessionId && <ChatInterface sessionId={sessionId} username={user.username} key={sessionId} />
          )}
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

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;
