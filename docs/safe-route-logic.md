# Safer Route Generation Logic

1. User requests navigation
2. Azure Maps provides multiple routes
3. Routes are split into segments
4. Safety Prediction API evaluates each segment
5. Route risk is calculated as:

Route Risk = Σ (segment_risk × segment_length)

6. Route with lowest risk is selected
7. Safest route is displayed to user
