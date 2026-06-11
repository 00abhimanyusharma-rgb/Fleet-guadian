# Azure Deployment Plan

## Target Architecture

Truck Service
Shipment Service
Driver Service

↓

Docker Containers

↓

Azure Container Apps

↓

OpenTelemetry Instrumentation

↓

OpenTelemetry Collector

↓

Splunk Observability Cloud

## Azure Services

### Azure Container Apps

Used to host:

- Truck Service
- Shipment Service
- Driver Service

### Azure Monitor

Used for:

- Application Monitoring
- Metrics Collection
- Health Monitoring

### Azure Log Analytics

Used for:

- Centralized Logging
- Incident Investigation

### Azure Application Insights

Used for:

- Distributed Tracing
- Request Monitoring
- Performance Analysis

## Deployment Steps

1. Build Docker Images
2. Push Images to Azure Container Registry
3. Deploy to Azure Container Apps
4. Configure OpenTelemetry
5. Connect to Splunk Observability Cloud
6. Create Dashboards and Alerts

## Scaling Strategy

- Auto Scaling Enabled
- CPU Based Scaling
- Request Based Scaling

## Security

- Managed Identity
- HTTPS Only
- Role Based Access Control

## Future Enhancement

Production deployment can be completed once Azure resources and credentials are available.
