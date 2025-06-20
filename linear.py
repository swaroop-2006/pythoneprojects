import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_linear_regression_dataset.csv")

def gradient_decent(m_now,b_now,points,l):
   m_gradient=0
   b_gradient=0
   n=len(points)
   for i in range(n):
       x = points.iloc[i].Hours_Studied
       y = points.iloc[i].Exam_Marks
       m_gradient += -(2/n)*((y-(m_now*x+b_now))*x)
       b_gradient += -(2/n)*(y-(m_now*x+b_now))
       
   
   m = m_now - l*m_gradient 
   b = b_now - l*b_gradient
   return m,b

m=0
b=0
l=0.0001
epochs=300
for i in range(epochs):
  if i%50 == 0:
   print(f"Epoch:{i}")
m,b= gradient_decent(m,b,data,l)   
print(m,b)
predicted = [m*x + b for x in data.Hours_Studied]

plt.scatter(data.Hours_Studied,data.Exam_Marks,color="black")
plt.plot(data.Hours_Studied, predicted, color="red")
plt.show()
   
  