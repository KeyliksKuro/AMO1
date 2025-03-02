from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
import pandas as pd
import os

wine_quality = fetch_ucirepo(id = 186)

X = wine_quality.data.features
y = wine_quality.data.targets

print(wine_quality.metadata)
print(wine_quality.variables)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

train_df = pd.concat([pd.DataFrame(X_train),pd.DataFrame(y_train)], axis=1)
test_df = pd.concat([pd.DataFrame(X_test),pd.DataFrame(y_test)], axis=1)

if not os.path.exists("train"):
    os.makedirs("train")
if not os.path.exists("test"):
    os.makedirs("test")

train_df.to_csv('train/train_df.csv', index=False)
test_df.to_csv('test/test_df.csv', index=False)