# CAD Call Simulator

A Python application that simulates real-time police incident reporting by reading historical police incident data and sending it to a web service.

## Overview

This simulator reads police incident data from a CSV file and replays it by sending individual incidents to a web service. It includes health checks and proper error handling to ensure reliable data transmission.

## Data Format

The simulator uses historical police incident data with the following fields:

- `incident_number`: Unique identifier for each incident
- `call_type`: Type of police call (e.g., "Welfare Check", "DUI")
- `call_type_group`: Broad category of the call
- `call_time`: Timestamp of the incident
- `Street`: Location of the incident
- `call_origin`: Source of the call (e.g., "911", "Phone")
- Various flags for incident characteristics:
  - `mental_health`
  - `drug_related`
  - `dv_related`
  - `alcohol_related`
- Location information:
  - `Area`: Area code
  - `AreaName`: Name of the area
  - `Latitude`
  - `Longitude`
- Time-based information:
  - `Hour`
  - `DayOfWeek`
  - `Month`
  - `year`
- Additional details:
  - `WARD`
  - `DISTRICT`
  - `priority`

## Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests
```

## Configuration

The simulator is configured to connect to a web service at:
- Base URL: `http://127.0.0.1:9292`
- Health Check Endpoint: `/health`
- Incident Submission Endpoint: `/call_details`

## Usage

1. Place your incident data CSV file in the project directory
2. Run the simulator:
```bash
python simulator.py
```

The simulator will:
1. Perform a health check on the web service
2. Read incidents from the CSV file
3. Send each incident to the web service with a 4-second delay
4. Display progress in the console

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

The simulator handles several types of errors:
- Failed health checks
- Network connectivity issues
- Invalid response data
- Server errors

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Your chosen license]
