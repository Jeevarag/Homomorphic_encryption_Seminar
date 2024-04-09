import pandas as pd
import numpy as np
import phe as paillier
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class LinModel:
	def __init__(self):
		pass

	def getResults(self):
		df = pd.read_csv('CVD_report.csv')
		y = df['CVD Risk Score']
		X = df.drop('CVD Risk Score', axis=1)
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
		reg = LinearRegression().fit(X_train, y_train)
		y_pred = reg.predict(X_test)
		RMSE = pow(mean_squared_error(y_pred, y_test), 0.5)
		R_squared = r2_score(y_pred, y_test)

		# Print results with titles
		# print("Regression Coefficients:")
		# print(reg.coef_)
		# print("\nRoot Mean Squared Error (RMSE):", RMSE)
		# print("R-squared (R^2):", R_squared)
		#
		return reg, y_pred, RMSE, R_squared

	def getCoef(self):
		return self.getResults()[0].coef_


def main():
	cof=LinModel().getCoef()
	print(cof)


if __name__=='__main__':
	main()