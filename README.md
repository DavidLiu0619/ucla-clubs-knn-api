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
git clone https://github.com/[your-username]/ucla_clubs_knn_api.git
cd ucla_clubs_knn_api
```

### 2. Build and run the app locally:
```bash
docker compose up -d
```

### 3. Test the API:
Verify the server is running:
```bash
curl http://localhost:5050/
```

Test a prediction:
```bash
curl -H "Content-Type: application/json" -X POST -d '{"query":"machine learning artificial intelligence", "neighbors":5}' "http://localhost:5050/predict"
```

### 4. Stop the container:
```bash
docker compose down -v
```

---

## Deployment on Google Cloud Run

### Prerequisites:
1. Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
2. Initialize and authenticate:
```bash
gcloud init
gcloud auth configure-docker
```

### Deployment Steps:

1. Build the Docker image:
```bash
docker build -t gcr.io/[PROJECT-ID]/ucla-clubs-api .
```

2. Push to Google Container Registry:
```bash
docker push gcr.io/[PROJECT-ID]/ucla-clubs-api
```

3. Deploy to Cloud Run:
```bash
gcloud run deploy ucla-clubs-api \
  --image gcr.io/[PROJECT-ID]/ucla-clubs-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

4. Test the deployed API:
```bash
curl -X POST "[YOUR-CLOUD-RUN-URL]/predict" \
  -H "Content-Type: application/json" \
  -d '{"query":"machine learning artificial intelligence", "neighbors":5}'
```

---

## Environment Variables

No sensitive environment variables are required for this project.

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
