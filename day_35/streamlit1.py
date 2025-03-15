import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

st.write("""
# Random Forest Classifier App
## Made by Aiman Aali Hamdani    
This app predicts the type of iris based on sepal length, sepal width, petal length, and petal width.
""")

# st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('sepal length', 4.3, 7.9, 4.5)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data,index=[0])
    return features
st.sidebar.header('User Input Parameters')
df = user_input_features()


st.subheader('User1 Input Parameters')
st.write(df)

# iris = pd.read_csv('https://raw.githubusercontent.com/streamlit/demo-data/master/iris.csv')
iris=sns.load_dataset('iris')

st.subheader('Iris Dataset')
st.write(iris.head())

st.subheader("Plotly k plots")
fig= px.scatter(iris,x='petal_length',y='sepal_length',color='species')
st.plotly_chart(fig)

st.subheader('Iris bar plot with plotly')
fig1=px.bar(iris,x='species',y='petal_length',color='species')
st.plotly_chart(fig1)

st.subheader('gapminder data visualization animated scatter')
df1 = px.data.gapminder()
fig2=px.scatter(df1, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                      size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig2)

st.subheader("Animated Bar Charts with Plotly Express")
df3 = px.data.gapminder()
fig3 = px.bar(df3, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])
st.plotly_chart(fig3)

st.subheader("3D scatter plot with Plotly Express for iris dataset")

fig4 = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width',color='species')
st.plotly_chart(fig4)

st.subheader("Ab machine learning model banatay hain aur prediction karty hain")
#inputs are X
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# outputs are y
y = iris['species']
st.write(f"X variable ki shape {X.shape}")
st.write(f"y variable ki shape {y.shape}")

model = RandomForestClassifier()
# model=SVC()
# model=KNeighborsClassifier()
model.fit(X, y)

prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write("""
0 = setosa\n
1 = versicolor\n
2 = virginica
""")
st.write(prediction_proba)

