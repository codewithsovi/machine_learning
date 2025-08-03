from sklearn.datasets import load_iris

iris = load_iris()

# explanatory variables (features)
X = iris.data
print("Shape dari X:", X.shape)

# nampilin nama variables
feature_name = iris.feature_names
print(feature_name)

# nampilin datanya
print(X)

# =============================================
# response variables (target)
y = iris.target
print("Shape dari y:", y.shape)

# nampilin nama variable 
target_name = iris.target_names
print(target_name) 

# nampilin datanya
print(y)