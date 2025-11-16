import React from 'react';
import './Message.css';

function Message({ message }) {
  const isBot = message.role === 'bot';
  const isUser = message.role === 'user';

  const formatContent = (content) => {
    // Convert markdown-style bold text
    content = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert line breaks to <br>
    content = content.replace(/\n/g, '<br>');
    
    return content;
  };

  const renderDiagnosis = () => {
    if (!message.diagnosis || message.diagnosis.length === 0) {
      return null;
    }

    return (
      <div className="diagnosis-container">
        <h4 className="diagnosis-title">📋 Diagnostic Results</h4>
        {message.diagnosis.map((diag, index) => (
          <div key={index} className="diagnosis-card">
            <div className="diagnosis-header">
              <span className="diagnosis-rank">#{index + 1}</span>
              <h5 className="diagnosis-condition">{diag.condition}</h5>
              <span className="diagnosis-confidence">
                {diag.confidence.toFixed(1)}%
              </span>
            </div>
            <div className="diagnosis-body">
              <div className="diagnosis-section">
                <strong>Matched Symptoms:</strong>
                <div className="symptoms-list">
                  {diag.matched_symptoms.map((symptom, idx) => (
                    <span key={idx} className="symptom-tag matched">
                      ✓ {symptom}
                    </span>
                  ))}
                </div>
              </div>
              {diag.description && (
                <div className="diagnosis-section">
                  <strong>Description:</strong>
                  <p>{diag.description}</p>
                </div>
              )}
              {diag.recommendations && (
                <div className="diagnosis-section">
                  <strong>Recommendations:</strong>
                  <p>{diag.recommendations}</p>
                </div>
              )}
            </div>
            <div className="confidence-bar">
              <div 
                className="confidence-fill" 
                style={{ width: `${diag.confidence}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className={`message ${isBot ? 'bot-message' : 'user-message'}`}>
      {isBot && (
        <div className="message-avatar bot-avatar">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 6H17V4C17 2.9 16.1 2 15 2H9C7.9 2 7 2.9 7 4V6H4C2.9 6 2 6.9 2 8V20C2 21.1 2.9 22 4 22H20C21.1 22 22 21.1 22 20V8C22 6.9 21.1 6 20 6ZM9 4H15V6H9V4ZM20 20H4V8H20V20Z" fill="currentColor"/>
            <path d="M12 9C10.34 9 9 10.34 9 12C9 13.66 10.34 15 12 15C13.66 15 15 13.66 15 12C15 10.34 13.66 9 12 9ZM12 13C11.45 13 11 12.55 11 12C11 11.45 11.45 11 12 11C12.55 11 13 11.45 13 12C13 12.55 12.55 13 12 13Z" fill="currentColor"/>
          </svg>
        </div>
      )}
      <div className="message-content">
        <div 
          className="message-text"
          dangerouslySetInnerHTML={{ __html: formatContent(message.content) }}
        />
        {renderDiagnosis()}
        <span className="message-time">
          {new Date(message.timestamp).toLocaleTimeString([], { 
            hour: '2-digit', 
            minute: '2-digit' 
          })}
        </span>
      </div>
      {isUser && (
        <div className="message-avatar user-avatar">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z" fill="currentColor"/>
          </svg>
        </div>
      )}
    </div>
  );
}

export default Message;
