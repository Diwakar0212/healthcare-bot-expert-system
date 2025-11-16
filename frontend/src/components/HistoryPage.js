import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';
import './HistoryPage.css';

function HistoryPage({ onBack }) {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedEntry, setSelectedEntry] = useState(null);
  const { user } = useAuth();

  useEffect(() => {
    fetchHistory();
  }, [user]);

  const fetchHistory = async () => {
    if (!user) return;
    
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:5000/api/history/${user.username}`);
      if (response.data.success) {
        setHistory(response.data.history.reverse()); // Most recent first
      }
    } catch (error) {
      console.error('Error fetching history:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleClearHistory = async () => {
    if (!window.confirm('Are you sure you want to clear all your medical history? This action cannot be undone.')) {
      return;
    }

    try {
      const response = await axios.delete(`http://localhost:5000/api/history/${user.username}`);
      if (response.data.success) {
        setHistory([]);
        setSelectedEntry(null);
      }
    } catch (error) {
      console.error('Error clearing history:', error);
      alert('Failed to clear history. Please try again.');
    }
  };

  const formatDate = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getTopCondition = (diagnoses) => {
    if (!diagnoses || diagnoses.length === 0) return 'No diagnosis';
    return diagnoses[0].condition;
  };

  return (
    <div className="history-page">
      <div className="history-header">
        <button className="back-button" onClick={onBack}>
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 11H7.83L13.42 5.41L12 4L4 12L12 20L13.41 18.59L7.83 13H20V11Z" fill="currentColor"/>
          </svg>
          Back to Chat
        </button>
        <h2>Medical History</h2>
        {history.length > 0 && (
          <button className="clear-button" onClick={handleClearHistory}>
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 19C6 20.1 6.9 21 8 21H16C17.1 21 18 20.1 18 19V7H6V19ZM19 4H15.5L14.5 3H9.5L8.5 4H5V6H19V4Z" fill="currentColor"/>
            </svg>
            Clear History
          </button>
        )}
      </div>

      <div className="history-content">
        {loading ? (
          <div className="loading-container">
            <div className="loading-spinner-large"></div>
            <p>Loading your medical history...</p>
          </div>
        ) : history.length === 0 ? (
          <div className="empty-state">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19 3H14.82C14.4 1.84 13.3 1 12 1C10.7 1 9.6 1.84 9.18 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM12 3C12.55 3 13 3.45 13 4C13 4.55 12.55 5 12 5C11.45 5 11 4.55 11 4C11 3.45 11.45 3 12 3ZM19 19H5V5H7V7H17V5H19V19Z" fill="currentColor"/>
            </svg>
            <h3>No Medical History</h3>
            <p>Your consultation history will appear here once you start using the diagnostic chatbot.</p>
            <button className="start-chat-button" onClick={onBack}>
              Start Consultation
            </button>
          </div>
        ) : (
          <div className="history-grid">
            <div className="history-list">
              <div className="history-stats">
                <div className="stat-card">
                  <div className="stat-number">{history.length}</div>
                  <div className="stat-label">Total Consultations</div>
                </div>
                <div className="stat-card">
                  <div className="stat-number">
                    {new Set(history.flatMap(h => h.symptoms)).size}
                  </div>
                  <div className="stat-label">Unique Symptoms</div>
                </div>
              </div>

              {history.map((entry, index) => (
                <div 
                  key={index} 
                  className={`history-card ${selectedEntry === index ? 'selected' : ''}`}
                  onClick={() => setSelectedEntry(index)}
                >
                  <div className="history-card-header">
                    <h3>{getTopCondition(entry.diagnoses)}</h3>
                    <span className="history-date">{formatDate(entry.timestamp)}</span>
                  </div>
                  <div className="history-card-symptoms">
                    <strong>Symptoms:</strong>
                    <div className="symptom-tags">
                      {entry.symptoms.slice(0, 3).map((symptom, idx) => (
                        <span key={idx} className="symptom-tag">{symptom}</span>
                      ))}
                      {entry.symptoms.length > 3 && (
                        <span className="symptom-tag more">+{entry.symptoms.length - 3} more</span>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {selectedEntry !== null && (
              <div className="history-details">
                <h3>Consultation Details</h3>
                <div className="detail-section">
                  <h4>📅 Date & Time</h4>
                  <p>{formatDate(history[selectedEntry].timestamp)}</p>
                </div>

                <div className="detail-section">
                  <h4>🩺 Symptoms Reported</h4>
                  <div className="symptom-list">
                    {history[selectedEntry].symptoms.map((symptom, idx) => (
                      <div key={idx} className="symptom-item">
                        <span className="bullet">•</span>
                        <span>{symptom}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="detail-section">
                  <h4>🔍 Diagnosis Results</h4>
                  {history[selectedEntry].diagnoses.map((diagnosis, idx) => (
                    <div key={idx} className="diagnosis-detail-card">
                      <div className="diagnosis-detail-header">
                        <span className="rank">#{idx + 1}</span>
                        <h5>{diagnosis.condition}</h5>
                        <span className="confidence-badge">
                          {diagnosis.confidence.toFixed(1)}%
                        </span>
                      </div>
                      <div className="diagnosis-detail-body">
                        <p><strong>Description:</strong> {diagnosis.description}</p>
                        <p><strong>Recommendations:</strong> {diagnosis.recommendations}</p>
                      </div>
                      <div className="confidence-bar">
                        <div 
                          className="confidence-fill" 
                          style={{ width: `${diagnosis.confidence}%` }}
                        ></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default HistoryPage;
