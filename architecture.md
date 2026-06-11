# Fleet Guardian Architecture

## Overview

Fleet Guardian is a fleet observability and monitoring solution designed to track trucks, shipments, and drivers.

## Architecture Flow

Truck Service
      |
Shipment Service
      |
Driver Service
      |
Observability Layer
      |
Dashboard
      |
AIOps Log Analyzer

## Components

### Truck Service
Provides truck status and fleet information.

### Shipment Service
Provides shipment tracking and failure simulation.

### Driver Service
Provides driver information and traffic spike simulation.

### Observability Layer
Captures logs, metrics, and service activity.

### Dashboard
Displays operational metrics and service information.

### AIOps Log Analyzer
Analyzes logs and suggests probable root causes.

## Future Integrations

- OpenTelemetry
- OpenTelemetry Collector
- Azure
- Splunk Observability Cloud
- Automated Alerting
- Truck Service
      |
Shipment Service
      |
Driver Service
      |
OpenTelemetry Instrumentation
      |
OpenTelemetry Collector
      |
Splunk Observability Cloud
      |
AIOps Utility
