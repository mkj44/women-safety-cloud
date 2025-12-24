# System Architecture – Women Safety Platform

Mobile App (Flutter / React Native)
        |
        | HTTPS + JWT
        v
Azure API Management
        |
        v
Backend API (Azure App Service)
        |
        |-------------------------------|
        |                               |
        v                               v
Safety Prediction API          Azure Functions
(Azure App Service)            (Alerts & SOS)
        |                               |
        v                               v
Azure Machine Learning          Azure Event Grid
        |                               |
        v                               v
Risk Scores                    Notification Hubs
                                        |
                                        v
                           Emergency Contacts / User

Azure Maps → Safer Routes  
Cosmos DB → Incidents & Logs  
Key Vault → Secrets
