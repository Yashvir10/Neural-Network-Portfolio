# ML_P1 — Spam Text Classifier
A simple machine learning project that classifies short text messages as **SPAM** or **NOT SPAM** using text preprocessing (NLTK) and a Multinomial Naive Bayes classifier (scikit-learn).

## Overview

This notebook demonstrates a minimal end-to-end NLP pipeline:

1. **Text preprocessing** — lowercasing, punctuation removal, tokenization, stopword removal, and lemmatization.
2. **Feature extraction** — converting cleaned text into numeric features using `CountVectorizer`.
3. **Model training** — fitting a `MultinomialNB` classifier on a small labeled dataset.
4. **Evaluation** — accuracy score and classification report on a held-out test split.
5. **Inference** — predicting labels for new, unseen messages.

## Dataset

A small hand-crafted set of 8 example messages (4 spam, 4 not-spam) is used for demonstration purposes. Labels: `1 = spam`, `0 = not spam`.

## Requirements

```
numpy
scikit-learn
nltk
```

Install with:
```bash
pip install numpy scikit-learn nltk
```

The notebook also downloads the required NLTK resources automatically:
- `punkt`, `punkt_tab`
- `stopwords`
- `wordnet`, `omw-1.4`
- `averaged_perceptron_tagger`, `averaged_perceptron_tagger_eng`

## How to Run

1. Open `ML_P1.ipynb` in Jupyter Notebook / JupyterLab / VS Code.
2. Run all cells in order (top to bottom).
3. The notebook will:
   - Preprocess the sample texts
   - Train a Naive Bayes model
   - Print accuracy and a classification report
   - Predict on two new example messages and print `SPAM` / `NOT SPAM`

## Pipeline Details

**Preprocessing (`preprocess` function):**
- Lowercases text
- Removes non-alphabetic characters
- Tokenizes with `word_tokenize`
- Removes English stopwords
- Lemmatizes tokens (verb form)

**Model:**
- Bag-of-words features via `CountVectorizer`
- `MultinomialNB` classifier
- 75/25 train-test split (`random_state=42`)

## Notes / Possible Improvements

- The dataset is tiny (8 samples) and intended only as a demonstration — accuracy on such a small split isn't statistically meaningful.
- Consider replacing `CountVectorizer` with `TfidfTransformer`/`TfidfVectorizer` (already imported but unused) for weighted features.
- A larger, real-world labeled dataset (e.g., SMS Spam Collection) would be needed for a production-ready model.
