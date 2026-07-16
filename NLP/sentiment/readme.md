# Sentiment Analysis — End-to-End NLP Project

A complete, self-contained NLP pipeline for binary sentiment classification (positive vs. negative), built with `scikit-learn`. No external datasets or internet access required — the labeled dataset is generated programmatically so the whole notebook runs offline out of the box.

## What it does

1. **Builds a labeled dataset** of review-style sentences (positive/negative)
2. **Exploratory data analysis** — class balance, text length, top words per class
3. **Text preprocessing** — lowercasing, punctuation removal, stopword filtering
4. **Feature engineering** — TF-IDF vectorization (unigrams + bigrams)
5. **Trains & compares models** — Naive Bayes, Logistic Regression, Linear SVM
6. **Hyperparameter tuning** with `GridSearchCV`
7. **Evaluation** — classification report, confusion matrix
8. **Interpretability** — top positive/negative predictive words
9. **Saves the trained model** (`.pkl`) for reuse
10. **Runs inference** on new, unseen text

## Project structure

```
NLP/
├── .gitignore
├── LICENSE
├── NLP_1.ipynb        # Main notebook — run top to bottom
└── Readme.md
└──requirements.txt     # Python dependencies
└──sentiment_model.pkl
└──tfidf_vectorizer.pkl
```

## Setup

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/<your-username>/project1.git
cd project1/NLP

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Launch Jupyter and run the notebook:

```bash
jupyter notebook NLP_1.ipynb
```

Run all cells top to bottom. At the end, you can test the model on your own text:

```python
predict_sentiment("This was an incredible experience!")
# -> {'sentiment': 'Positive', 'confidence': 0.83}
```

The trained model and vectorizer are saved as `sentiment_model.pkl` and `tfidf_vectorizer.pkl` (not committed to the repo — see `.gitignore` — regenerate by re-running the notebook).

## Results

All three baseline models reach high accuracy on the held-out test set, since the synthetic dataset is template-based and cleanly separable. On real-world text (see below), expect more variation between models.

## Using real data instead

Swap the dataset-generation cell for:

```python
df = pd.read_csv("your_file.csv")  # needs a `text` column and a `label` column (0/1)
```

Everything downstream (cleaning, TF-IDF, modeling, evaluation) works unchanged.

## Next steps

- Swap in a real dataset (IMDB, Yelp, Amazon reviews)
- Try word embeddings or transformer-based features
- Extend to multi-class sentiment (negative/neutral/positive)
- Wrap `predict_sentiment` in a Flask/FastAPI endpoint

## License

MIT — see [LICENSE](LICENSE).
