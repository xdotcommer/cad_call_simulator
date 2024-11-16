# CAD Call Simulator

A Python application that simulates real-time police incident reporting by reading historical police incident data and sending it to a web service.

## Overview

This simulator reads police incident data from a CSV file and replays it by sending individual incidents to a web service. It includes health checks and proper error handling to ensure reliable data transmission.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/xdotcommer/cad_call_simulator.git
cd cad_call_simulator
```

2. Create and activate a virtual environment (recommended):
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The simulator is configured to connect to a web service at:
- Base URL: `http://127.0.0.1:9292`
- Health Check Endpoint: `/health`
- Incident Submission Endpoint: `/call_details`

## Data Format

The simulator expects a CSV file with the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| incident_number | Unique identifier | 22BU000002 |
| call_type | Type of police call | Welfare Check |
| call_type_group | Category of call | Public Service |
| call_time | Timestamp | 2021-12-31T20:08:55-05:00 |
| Street | Location | Main St |
| call_origin | Source of call | 911, Phone |
| mental_health | Mental health flag | 0/1 |
| drug_related | Drug relation flag | 0/1 |
| dv_related | Domestic violence flag | 0/1 |
| alcohol_related | Alcohol relation flag | 0/1 |
| Area | Area code | E |
| AreaName | Area name | SouthEnd |
| Latitude | Latitude coordinate | 44.4754105 |
| Longitude | Longitude coordinate | -73.1971131 |
| Hour | Time of day | 1 am |
| DayOfWeek | Day of week | Saturday |
| WARD | Ward number | 8 |
| DISTRICT | District name | East |
| priority | Priority level | Priority 2 |
| Month | Month name | January |
| year | Year | 2022 |

## Usage

1. Place your incident data CSV file in the project directory
2. Run the simulator:
```bash
python simulator.py
```

The simulator will:
- Perform a health check on the web service
- Read incidents from the CSV file
- Send each incident to the web service with a 4-second delay
- Display progress in the console

## Features

- Health check monitoring
- JSON payload formatting
- Error handling for failed requests
- Rate limiting (4-second delay between incidents)
- Progress monitoring through console output

## Sample Output

```
Health Check Succeeded.
New Call:
  Incident #: 22BU000002
  Call Type: Welfare Check
  Call Time: 2021-12-31T20:08:55-05:00
```

## Error Handling

The simulator handles:
- Failed health checks
- Network connectivity issues
- Invalid response data
- Server errors

## Development

Want to contribute? Here's how to set up the project for development:

```bash
# Clone the repository
git clone https://github.com/xdotcommer/cad_call_simulator.git
cd cad_call_simulator

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the simulator
python simulator.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Related Services

- [CAD Call Simulator](https://github.com/xdotcommer/cad-call-simulator) - A Python tool for simulating incident data
- [Call Service](https://github.com/xdotcommer/call_service) - Main call processing service
- [APCO Service](https://github.com/xdotcommer/apco_incident_types_service) - APCO code lookup service
- [Call Logger](https://github.com/xdotcommer/call_logger) - Persistent storage service for emergency call data

This microservices ecosystem provides a complete solution for:
- Simulating emergency calls (CAD Call Simulator)
- Processing and routing calls (Call Service)
- Standardizing call types (APCO Service)
- Storing call history (Call Logger)
