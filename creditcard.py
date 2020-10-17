import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_roc_curve,plot_confusion_matrix,plot_precision_recall_curve
from sklearn.metrics import precision_score,recall_score

def main():
    st.title("Default of Credit Card Clients")
    st.sidebar.title("Default of Credit Card Clients")
    
    st.markdown("Our client is a credit card company. They have brought us a dataset that includes some demographics and recent financial data (the past six months) for a sample of 30,000 of their account holders. This data is at the credit account level; in other words, there is one row for each account (you should always clarify what the definition of a row is, in a dataset). Rows are labeled by whether in the next month after the six month historical data period, an account owner has defaulted, or in other words, failed to make the minimum payment.")
    st.markdown("The problem statement we are trying to address here is a classification problem. We have a dataset that has the payment history of a particular account holder, using this we need to predict whether a particular account holder will be a defaulter in the next month or not.")
    
    st.markdown("So, Let's evaluate our model with different Evaluation metrices as the metrices provide us how effective our model is.")


   
                
    st.sidebar.markdown("Let\'s do it")
    
   
    data = pd.read_csv('https://raw.githubusercontent.com/Technocolabs100/Project-Data-Set-Repository/master/Data%20set/cleaned_data.csv')
    
    
    
    
    
    @st.cache(persist=True)
    def split(data):
         
         y= data['default payment next month']
         x= data.drop(columns=['ID', 'SEX', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
                   'EDUCATION_CAT', 'graduate school', 'high school', 
                   'others', 'university','default payment next month'])
       
         
         
         x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=24)
         return x_train,x_test,y_train,y_test
     
    def plot_metrics(metrics_list):
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(Model,x_test,y_test,display_labels=class_names)
       
      
            st.pyplot()
        
        
        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            plot_roc_curve(Model,x_test,y_test)
       
      
            st.pyplot()
            
        if 'Precision Recall Curve' in metrics_list:
            st.subheader("Precision Recall Curve")
            plot_precision_recall_curve(Model,x_test,y_test)

            st.pyplot()
            
            
     
    x_train,x_test,y_train,y_test = split(data)
    class_names = ['Default','Not Default']
    
    st.sidebar.subheader('Choose Model')
    Model = st.sidebar.selectbox("Model",('Logistic Regression','Random Forest'))
    
    if Model == "Logistic Regression":
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C(Regularization parameter)",0.01,10.0,step=0.01,key='C_LR')
        max_iter = st.sidebar.slider("Maximum Number of Iterations",100,500,key='max_iter')
        metrics = st.sidebar.selectbox("Which metrics to plot?",('ROC Curve','Precision Recall Curve','Confusion Matrix'))
        
        if st.sidebar.button("Classify",key='classify'):
            st.subheader("Logistic Regression Results")
            Model = LogisticRegression(C=C,max_iter=max_iter)
            Model.fit(x_train,y_train)
            accuracy = Model.score(x_test,y_test)
            y_pred = Model.predict(x_test)
            st.write("Accuracy:",accuracy.round(2))
            st.write("Precision:",precision_score(y_test,y_pred).round(2))
            st.write("Recall:",recall_score(y_test,y_pred).round(2))
            plot_metrics(metrics)
            
           
   
            
    if Model == "Random Forest":
        st.sidebar.subheader("Model Hyperparameters")
        n_estimators = st.sidebar.number_input("The number of trees in the forest",100,5000,step=10,key='n_est')
        max_depth = st.sidebar.number_input("The maximum depth of the tree",1,20,step=1,key='max_depth')
        bootstrap = st.sidebar.radio("Bootstrap samples when building trees",('True','False'),key='bootstrap')
        metrics = st.sidebar.selectbox("Which metrics to plot?",('ROC Curve','Precision Recall Curve','Confusion Matrix'),key='1')
        
        if st.sidebar.button("Classify",key='class'):
            st.subheader("Random Forest Result")
            Model = RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth,bootstrap=bootstrap)
            Model.fit(x_train,y_train)
            accuracy = Model.score(x_test,y_test)
            y_pred = Model.predict(x_test)
            st.write("Accuracy:",accuracy.round(2))
            st.write("Precision:",precision_score(y_test,y_pred).round(2))
            st.write("Recall:",recall_score(y_test,y_pred).round(2))
            plot_metrics(metrics)
        
    
     
    
    if st.sidebar.checkbox("Show Raw Data",False):
        st.subheader("Credit Card Default Data")
        st.write(data)




if __name__ == '__main__':
    main()

             
    
     
        
             
        
        
        

