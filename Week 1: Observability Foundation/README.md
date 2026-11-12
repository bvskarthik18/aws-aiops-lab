# Week 01 - Observability Foundation

## Goal

Learn what Observability data an AIOps system needs before AI can investigate cloud incidents.

## Status

🚧 In Progress

## Lab Workload

For the first lab, I will use a simple two-service application:

User → Orders API → Inventory API

The application is intentionally small. Its purpose is to generate
metrics, logs, and distributed traces that can later be used for
manual and AI-assisted incident investigation.

## AWS Runtime

The first version of the workload will use:

User → Amazon API Gateway → Orders Lambda → Inventory Lambda

I am using a small serverless architecture so I can concentrate on observability and AIOps rather than Infrastructure management.

## First API

The first API will be:

GET /orders/123

The orders service will call the Inventory service to check whether the product is available.

Expected response:

{
    "order_id": "123",
    "product": "laptop",
    "quantity": 1,
    "inventory_status": "available"
}