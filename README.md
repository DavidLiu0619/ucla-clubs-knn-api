# UCLA Clubs KNN API
**Author**: Hengyuan (David) Liu

This project implements a K-Nearest Neighbors (KNN) based recommendation system through a Flask API to find similar UCLA student organizations based on their descriptions. The model uses natural language processing to vectorize club descriptions and finds the most similar clubs based on cosine similarity.

The project is fully containerized using Docker and deployed to **Google Cloud Run**. Anyone should be able to clone this repo, follow the setup steps, and reproduce the deployment.

---

## Repository Structure

| File | Description |
|------|-------------|
| `ucla_orgs_cleaned_unique.csv` | Dataset containing UCLA club information |
| `prediction.py` | Python script containing the KNN prediction function |
| `model/vectorizer.joblib` | Saved text vectorizer model |
| `Dockerfile` | Instructions to build the Docker image |
| `docker-compose.yml` | Used to launch the app locally via Docker |
| `requirements.txt` | List of Python dependencies |
| `curl_test.sh` | Test command lines |

---

## API Features

The API accepts the following parameters:

- `query` (required) – Text description to find similar clubs
- `neighbors` (optional, default=5) – Number of neighbors to consider
- `top` (optional, default=neighbors) – Number of results to return

The response includes:
- `name` – Club name
- `category` – Club category
- `detail_url` – URL to club details
- `similarity` – Cosine similarity score

---

## Local Testing with Docker

### 1. Clone this repository:
```bash
git clone https://github.com/DavidLiu0619/ucla-clubs-knn-api.git
cd ucla_clubs_knn_api
```

### 2. Build and run the app locally:
```bash
docker compose up -d
```

### 3. Test the API:
Verify the server is running:
```bash
curl http://localhost:5001/
```

Test a prediction:
```bash
curl -H "Content-Type: application/json" -X POST -d '{"query":"machine learning artificial intelligence", "top":4}' "http://localhost:5001/predict_clubs"
```

Expect output:
```bash
{
  "predict clubs": [
    {
      "category": "medical and technology",
      "detail_url": "https://community.ucla.edu/studentorg/6456",
      "name": "CAIR Collective",
      "similarity": 0.8159411098154683
    },
    {
      "category": "engineering and technology",
      "detail_url": "https://community.ucla.edu/studentorg/6081",
      "name": "Bruin Machine Learning & Analytics",
      "similarity": 0.3025182975325662
    },
    {
      "category": "medical and technology",
      "detail_url": "https://community.ucla.edu/studentorg/5059",
      "name": "AI and Eye",
      "similarity": 0.22405186589537673
    },
    {
      "category": "engineering and technology",
      "detail_url": "https://community.ucla.edu/studentorg/3892",
      "name": "DataRes at UCLA",
      "similarity": 0.1894215109713645
    }
  ]
}

```


### 4. Stop the container:
```bash
docker compose down -v
```

---

## After deployment on Google Cloud Run, Test the deployed API:
```bash
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"query": "machine learning artificial intelligence", "top": 4}' \
     https://ucla-clubs-knn-980752141572.us-central1.run.app/predict_clubs
```

Expect output:
```bash
{
  "predict clubs": [
    {
      "category": "medical and technology",
      "detail_url": "https://community.ucla.edu/studentorg/6456",
      "name": "CAIR Collective",
      "similarity": 0.8159411098154683
    },
    {
      "category": "engineering and technology",
      "detail_url": "https://community.ucla.edu/studentorg/6081",
      "name": "Bruin Machine Learning & Analytics",
      "similarity": 0.3025182975325662
    },
    {
      "category": "medical and technology",
      "detail_url": "https://community.ucla.edu/studentorg/5059",
      "name": "AI and Eye",
      "similarity": 0.22405186589537673
    },
    {
      "category": "engineering and technology",
      "detail_url": "https://community.ucla.edu/studentorg/3892",
      "name": "DataRes at UCLA",
      "similarity": 0.1894215109713645
    }
  ]
}

```

---

## Error Handling

The API includes proper error handling for:
- Empty queries
- Invalid number of neighbors
- Invalid input types
- Missing required parameters

---

## Contributing

Feel free to open issues or submit pull requests for any improvements.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
