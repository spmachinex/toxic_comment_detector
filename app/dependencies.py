import pickle
from .schemas import Comment

def check_toxicity(comment: Comment):
    # Load your model and vectorizer
    vectorizer = pickle.load(open("Vectorize.pickle", "rb"))
    model = pickle.load(open("Pickle_LR_Model.pkl", "rb"))

    # Transform the comment
    transformed_comment = vectorizer.transform([comment.comments])
    prediction = model.predict_proba(transformed_comment)[:, 1]

    return {"toxicity": prediction[0]}
