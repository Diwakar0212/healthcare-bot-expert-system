# Healthcare Bot - Setup Guide

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm

### Backend Setup (Terminal 1)

```powershell
# Navigate to backend
cd "c:\Users\diwakar\Documents\PBL\5th Sem PBL\HealthCare BOT\backend"

# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
```

Backend runs at: http://localhost:5000

### Frontend Setup (Terminal 2)

```powershell
# Navigate to frontend
cd "c:\Users\diwakar\Documents\PBL\5th Sem PBL\HealthCare BOT\frontend"

# Install dependencies
npm install

# Start React app
npm start
```

Frontend runs at: http://localhost:3000

## Testing the Application

1. Open http://localhost:3000 in your browser
2. Type symptoms like "I have a fever and headache"
3. Review the diagnosis results
4. Click suggestions for quick responses

## Troubleshooting

### Backend Issues

**Port 5000 already in use:**
```powershell
# Windows: Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Module not found:**
```powershell
pip install -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
```powershell
# Set different port
$env:PORT=3001; npm start
```

**Dependencies error:**
```powershell
# Clear cache and reinstall
rm -r node_modules
rm package-lock.json
npm install
```

### CORS Issues

Make sure Flask-CORS is installed:
```powershell
pip install flask-cors
```

## Development Tips

### Hot Reload
- Backend: Use `Flask debug mode` (already enabled in app.py)
- Frontend: React automatically hot reloads on save

### API Testing
Test endpoints with PowerShell:
```powershell
# Health check
Invoke-WebRequest -Uri http://localhost:5000/health -Method GET

# Chat endpoint
$body = @{
    session_id = "test_123"
    message = "I have a fever"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:5000/api/chat -Method POST -Body $body -ContentType "application/json"
```

### Code Structure

**Backend:**
- `app.py` - API routes
- `expert_system.py` - Main logic
- `knowledge_base.py` - Medical data
- `inference_engine.py` - Diagnosis algorithm

**Frontend:**
- `App.js` - Main component
- `ChatInterface.js` - Chat logic
- `Message.js` - Message display

## Next Steps

1. ✅ Backend running on port 5000
2. ✅ Frontend running on port 3000
3. ✅ Test the chat interface
4. ✅ Try different symptom combinations
5. 📝 Customize knowledge base (add more conditions)
6. 🎨 Customize UI styling
7. 🚀 Deploy to production (optional)

## Production Deployment

### Backend (Flask)
- Use Gunicorn or uWSGI
- Set up environment variables
- Use production database (if needed)
- Enable HTTPS

### Frontend (React)
```powershell
npm run build
# Deploy the 'build' folder to hosting service
```

## Support

For issues or questions:
1. Check the README.md
2. Review error messages
3. Verify all dependencies are installed
4. Ensure both servers are running

---

Happy Coding! 🚀
