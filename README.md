Fleet Guardian
Fleet Observability and AIOps Assignment
Overview
Fleet Guardian is a simulated fleet monitoring platform designed to demonstrate observability, monitoring, incident management, and AIOps concepts.
The system consists of three services:
Truck Service
Shipment Service
Driver Service
Features
Truck Service
View all trucks
View truck status
Monitor active trucks
Shipment Service
View shipments
View failed shipments
Simulate shipment delays
Generate HTTP 500 failures
Driver Service
View drivers
Monitor active drivers
Simulate traffic spikes
AIOps Utility
Reads service output
Summarizes incidents
Suggests probable root causes
Chaos Engineering
Implemented scenarios:
Shipment Delay Simulation
HTTP 500 Error Simulation
Driver Traffic Spike Simulation
Incident Investigation
Included:
Symptoms
Impact Analysis
Evidence
Root Cause Analysis
Recommendations
Technologies Used
Python 3.12
Flask
GitHub
Planned:
OpenTelemetry
Docker
Azure
Splunk Observability
Project Structure
Fleet-guardian/
README.md
truck_service.py
shipment_service.py
driver_service.py
log_analyzer.py
incident_report.md
requirements.txt
Future Enhancements
OpenTelemetry Instrumentation
Docker Containerization
Azure Deployment
Splunk Observability Integration
Automated Alerting
Author
Abhimanyu Sharma :::
## Assignment Notes

This project demonstrates a local implementation of Fleet Guardian.

- Fleet Monitoring
- Service Observability
- Chaos Engineering
- Incident Investigation
- AIOps Concepts

The architecture remains cloud-ready and can be integrated with Azure, Docker, OpenTelemetry, and Splunk Observability Cloud.
## OpenTelemetry Instrumentation

All Fleet Services are instrumented using OpenTelemetry Flask Instrumentation.

Implemented:
- Distributed Trace Generation
- Request Monitoring
- Service Visibility

Future Integration:
- OpenTelemetry Collector
- Splunk Observability Cloud Export
## OpenTelemetry Collector

An OpenTelemetry Collector configuration has been included to demonstrate the observability pipeline.

Pipeline:

Services
→ OpenTelemetry Instrumentation
→ OpenTelemetry Collector
→ Splunk Observability Cloud (Future Integration)

Current implementation exports telemetry to local logging for demonstration purposes.
Added dashboard documentation
