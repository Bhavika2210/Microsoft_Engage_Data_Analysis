import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer

pd.set_option('display.max_columns', None)

original_data=pd.read_csv('cars_engage_2022.csv')
data=original_data.copy()

df=data[data['Emission_Norm']=='BS 6'].copy()
df.dropna(axis=1,thresh=214,inplace=True)
# Changed the name of dependent variable to Price and converted that to Integer
df['Price'] = df['Ex-Showroom_Price']
# Rs. 2,92,667: Here 'Rs.' and ',' need to be removed

df['Price']=df['Price'].astype(str).str[4:]
df['Price'] = df.Price.str.replace(',', '')
df['Price'] = df['Price'].astype(int)
df.drop(labels=['Ex-Showroom_Price'], axis=1, inplace=True)
# Doing some mapping for convenience
# Emission Norm
df['Emission_Norm'] = df['Emission_Norm'].map({'BS 6': 6,'nan': 'Missing'})
df.dropna(axis=0, subset=['Emission_Norm'], inplace=True)
df['Emission_Norm'] = df.Emission_Norm.astype(float)

# Fuel-System: mapping it in 1 and 0 as it has only 2 variables i.e **Injection-1 and PGM-Fi-0**
df['Fuel_System'] = df['Fuel_System'].map({'Injection': 1,'PGM - Fi': 0})
df['Fuel_System'] = df.Fuel_System.astype(float)


#! HeadLight Reminder
df['Headlight_Reminder'] = df['Headlight_Reminder'].map({'Yes': 1,'Automatic': 0,})
df.dropna(axis=0, subset=['Headlight_Reminder'], inplace=True)
df['Headlight_Reminder'] = df.Headlight_Reminder.astype(float)


#! Gears
df['Gears'] = df['Gears'].map({'5': 5,'9': 9,'5': 5,'7': 7,'6': 6,'7 Dual Clutch': 7,'4': 4})
df['Gears'] = df.Gears.astype(float)


#! TripMeter
df.Tripmeter = df.Tripmeter.map({'2': 2,'1': 1,'Yes': 3})
df.Tripmeter = df.Tripmeter.astype(float)


#! Power Outlet
df['12v_Power_Outlet'] = df['12v_Power_Outlet'].map({'1': 1,'2': 2,'3': 3,'Yes': 4})
df['12v_Power_Outlet'] = df['12v_Power_Outlet'].astype(float)


#Since these columns have only 2 values, 'Yes' and blank, I am converting them to 0 and 1
def conversion(feature):
    df[feature] = np.where(df[feature].isnull(), 0, 1)


conversion('Fasten_Seat_Belt_Warning')
conversion('Key_Off_Reminder')
conversion('Door_Ajar_Warning')
conversion('USB_Compatibility')
conversion('Navigation_System')
conversion('Average_Speed')
conversion('ABS_(Anti-lock_Braking_System)')
conversion('Seat_Back_Pockets')
conversion('Engine_Immobilizer')
conversion('Gear_Indicator')
conversion('Auto-Dimming_Rear-View_Mirror')
conversion('Multifunction_Display')
conversion('Low_Fuel_Warning')
conversion('FM_Radio')
conversion('Engine_Malfunction_Light')
conversion('Distance_to_Empty')
conversion('ISOFIX_(Child-Seat_Mount)')
conversion('Aux-in_Compatibility')
conversion('Average_Fuel_Consumption')
conversion('Bluetooth')
conversion('CD_/_MP3_/_DVD_Player')
conversion('Central_Locking')
conversion('Child_Safety_Locks')
conversion('EBD_(Electronic_Brake-force_Distribution)')
conversion('Gear_Shift_Reminder')

def stringCut(feature):
    df[feature] = df[feature].astype(str).str[:-3]
    df[feature] = pd.to_numeric(df[feature], errors='coerce')   # If errors=‘coerce’, then invalid parsing will be set as NaN.

stringCut('Height')    # Example: Height= 1652 mm, so to have numerical value, we cut out the last three characters
stringCut('Width')
stringCut('Length')
stringCut('Displacement')
stringCut('Kerb_Weight')
stringCut('Ground_Clearance')
stringCut('Wheelbase')

def stringCut_2(feature):
    df[feature] = df[feature].astype(str).str[:-7]
    df[feature] = pd.to_numeric(df[feature], errors='coerce')


stringCut_2('Boot_Space')
stringCut_2('Fuel_Tank_Capacity')

def string_tyre(feature):
    df[feature] = df[feature].astype(str).str[:-6]
    df[feature] = pd.to_numeric(df[feature], errors='coerce')

string_tyre('Front_Tyre_&_Rim')
string_tyre('Rear_Tyre_&_Rim')
string_tyre('Wheels_Size')


df.ARAI_Certified_Mileage = df['ARAI_Certified_Mileage'].astype(str).str[:-9]
df.ARAI_Certified_Mileage = pd.to_numeric(
    df['ARAI_Certified_Mileage'], errors='coerce')

# for the Power column, example : 95PS – PS stands for PferdStarke (literally, 'horse strength' in German).
def string_cut_10(feature):
    df[feature] = df[feature].astype(str).str[:-10]
    df[feature] = pd.to_numeric(df[feature], errors='coerce')

string_cut_10('Power')
string_cut_10('Torque')

categ_feature=[feature for feature in df.columns if df[feature].dtypes == 'O']
# print('Number of Categorical Feature',len(categ_feature))

num_feature=[feature for feature  in df.columns if df[feature].dtypes!=object]
# print('Number of Numerical Feature', len(num_feature))

df_num_corr = df[num_feature].corr()["Price"][:-1]

# It is important to analyse the correlation between dependant and independant variables to save time and proceed in the right direction
# Correlated features (r2 > 0.5)
high_features_list = df_num_corr[abs(
    df_num_corr) >= 0.5].sort_values(ascending=False)
# print(
#     f"{len(high_features_list)} strongly correlated values with SalePrice:\n{high_features_list}\n")

# Correlated features (0.3 < r2 < 0.5)
low_features_list = df_num_corr[(abs(df_num_corr) < 0.5) & (
    abs(df_num_corr) >= 0.3)].sort_values(ascending=False)
# print(
#     f"{len(low_features_list)} slightly correlated values with SalePrice:\n{low_features_list}")

df.Make.value_counts().sort_values(ascending=False).head(20)

top_10=[x for x in df.Make.value_counts().sort_values(ascending=False).head(10).index]
for label in top_10:
    df[label]=np.where(df['Make']==label,1,0)

df.drop(['Make'],axis=1,inplace=True)
discrete_feature = [feature for feature in num_feature if len(df[feature].unique()) < 25]
continuous_featre = [feature for feature in num_feature if feature not in discrete_feature]

#Feature Engineering


# You can use any Scaling Method MinMax or Standard Scaler
# In Machine Learning, StandardScaler is used to resize the distribution of values
# so that the mean of the observed values is 0 and the standard deviation is 1.
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])



cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="most_frequent")),
    ('cat_encoder', OneHotEncoder(sparse=False))
])

data = df.drop(labels=['Price'], axis=1)


num_attribute = [
    feature for feature in data.columns if df[feature].dtypes != 'O']

cat_attribute = [
    feature for feature in df.columns if df[feature].dtypes == 'O']


final_pipeline = ColumnTransformer([
    ('num', num_pipeline, num_attribute),
    ('cat', cat_pipeline, cat_attribute)
])
num_df=df[num_attribute]

# From the correlation matrix, the following 19 columns are important for us:
highcorr_num_df=num_df[['Power','Wheels_Size','Rear_Tyre_&_Rim','Displacement','Cylinders','Fuel_Tank_Capacity','Front_Tyre_&_Rim','Torque','Fuel_System','Maruti Suzuki',
 'Honda',
 'Tata',
 'Jeep',
 'Kia',
 'Hyundai',
 'Bmw',
 'Ford',
 'Maruti Suzuki R',
 'Mahindra']]

highcorr_num_df_list=list(highcorr_num_df)
pipeline2=ColumnTransformer([('num2', num_pipeline, highcorr_num_df_list)])

final_high_corr=pipeline2.fit_transform(highcorr_num_df)
final_y = df['Price']

# Using Random Forest Regressor where every decision tree has high variance,
# but when we combine all of them together in parallel then the resultant variance is low as each decision tree gets perfectly trained on that particular sample data, and hence
# the output doesn’t depend on one decision tree but on multiple decision trees.
# In the case of a regression problem, the final output is the mean of all the outputs.

reg = RandomForestRegressor(max_depth=19, random_state=0)
reg.fit(final_high_corr, final_y)
predictions=reg.predict(final_high_corr)


# accuracy achieved is 95.94 %

highcorr_num_df.to_csv('df_cars_cleaned.csv')
filename = 'finalized_model.sav'
pickle.dump(reg, open("model.pkl", 'wb'))
model=pickle.load(open("model.pkl",'rb'))