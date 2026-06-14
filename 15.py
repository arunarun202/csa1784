from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_test_split=0.2, random_state=42)
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)

preds = clf.predict(X_test)
print(f"Model Classification Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")
