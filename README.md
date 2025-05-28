# UCLA Club Recommender 

## STATS 418 Final Project, 2025

This project is helping the UCLA Student to find club that best match their interests.

This is how the directory looks like

Main Repo:
	| data
		| webscrap.ipynb
		| ucla_orgs_cleaned.csv
	| eda
		eda.ipynb
	| proposal
		| project proposal.pdf
	| Docker
		| Dockerfile
		| Docker-compose.yml
	| curl_test.sh
	| requirements.txt
	| app.py
	| embeddings
		| build_index.py
		| club_descriptions.json
		| club embeddings.npy
		| club_names.json
		| faiss_dex.bin
	| model
		| vectorizer.joblib
		| clubs.json
		| nn_model.joblib
	| shiny_app
		| app.R
		| www
			| logo.png
	

Data:
The data is webscrap from the UCLA website: https://community.ucla.edu/studentorgs, it include 4 features: Category, Name, Description, URL, total has 48 features and 2,829 and 1,439 unique clubs.

On user interface, user will see three sections
1. Table Mode:  is simply uses the KNN (Cosin) to calculate similarity score base the user input. After the user input, based on the similarity score, it will output top 5 match clubs include: Name, Description, URL and Similarity Score. The KNN model store as Flask API

2.  Chat Mode: use the Gemini API with the prompt:         
f"User is interested in: {text}\n\n"
        "Here are some UCLA clubs:\n" +
        "\n".join(snippets) +
        "\n\n"
        "Recommend the top 3 clubs and explain each in JSON only, using this schema:\n"
        "{\n"
        "  \"recommendations\": [\n"
        "    {\"club\": \"<Club Name>\", \"explanation\": \"<Why it fits>\"},\n"
        "    …\n"
        "  ]\n"
        "}"??? I think should change a little bit

The purpose of this mode is answer any questions of the user have for the UCLA club Recommender based on the Category, Club Name, Description, and provide the url of the reference. And necessarily provide the recommend of the which club is matched for the student ask. 

3. Visualization Mode
The user can use this to see like the word cloud, distribution of the category by count of the clubs,....(still thinkings)


The goal is to take our locally deployed model(s) to deploy them to Google Cloud Run. In this way, as long as your instance is running whomever has the endpoint information and post requirements can make a request to your API. 

