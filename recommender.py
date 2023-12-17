from surprise import Dataset, Reader
from surprise import KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# 1. Import Libraries
import random

# 2. Load Dataset
data = Dataset.load_builtin('ml-100k')  # MovieLens 100k dataset
trainset, testset = train_test_split(data, test_size=0.25)

# 3. Create a Model (Using KNN)
model = KNNBasic(sim_options={'user_based': True})

# 4. Train the Model
model.fit(trainset)

# 5. Make Predictions on the Test Set
predictions = model.test(testset)

# 6. Evaluate Accuracy
accuracy.rmse(predictions)

# 7. Example Recommendation Function
def get_top_n_recommendations(predictions, n=10):
    from collections import defaultdict

    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

# Get top 10 recommendations for each user
top_n_recommendations = get_top_n_recommendations(predictions, n=10)

# Print the recommended items for each user
for uid, user_ratings in top_n_recommendations.items():
    print(uid, [iid for (iid, _) in user_ratings])
