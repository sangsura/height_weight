import numpy as np 
import streamlit as st
# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
from sklearn.linear_model import LinearRegression
lrg=LinearRegression(fit_intercept=False)
lrg.fit(Xbar,y)
w=lrg.coef_
st.header("Dự đoán cân nặng dựa trên tiêu chuẩn!!!!")
pre=st.number_input("Nhập chiều cao của bạn (cm) :")
weigh=pre*w[0][1]+w[0][0]
st.write("Cân nặng dự đoán của bạn là của bạn là:",round(weigh,2),"kg")
