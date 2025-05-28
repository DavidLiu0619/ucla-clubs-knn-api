#!/bin/bash

curl http://localhost:5001/

curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"query": "health", "top": 4}' \
     http://localhost:5001/predict_clubs


curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"query": "health", "top": 4}' \
     https://ucla-clubs-knn-980752141572.us-central1.run.app/predict_clubs




