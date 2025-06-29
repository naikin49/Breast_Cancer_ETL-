from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    X = df.drop(columns=["ID", "class"])
    y = (df["class"] == "M").astype(int)  # M = 1, B = 0
    X_scaled = StandardScaler().fit_transform(X)
    return X_scaled, y
