# Predictive Safety Alert Flow

1. Mobile app sends user location
2. Backend calls Safety Prediction API
3. API returns safety_score
4. If safety_score < 40:
   - Trigger Azure Function
   - Send warning to user
   - Suggest safer route
5. If risk persists:
   - Escalate alert
   - Keep SOS ready
