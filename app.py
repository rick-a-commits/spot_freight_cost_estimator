import streamlit as st
import pandas as pd
import pickle
import shap 
import matplotlib.pyplot as plt
import seaborn as sns


ref_df = pd.read_csv(r"shipment_costs_10000.csv")
X_train_numeric = pd.read_csv(r"x_train_numeric.csv")
X_test_numeric = pd.read_csv(r"x_test_numeric.csv")

max_km = ref_df['distance_km'].max()
min_km = ref_df['distance_km'].min()
max_weight = ref_df['weight_tons'].max()
min_weight = ref_df['weight_tons'].min()
unique_carriers = ref_df['carrier_name'].unique()
unique_trucks = ref_df['truck_type'].unique()
unique_priority = ref_df['priority_level'].unique()

st.title("Freight Cost Estimator")
st.markdown("Powered by ML")

st.header("Gain Price insights into your routes", divider='blue')




with st.sidebar:
     st.header("Select Trip Parameters")
     distance_km = st.slider("Distance in KM", min_km,max_km, 75)
     weight_tons = st.slider("Weight in tons", min_weight,max_weight, 22.0)
     carrier_name = st.selectbox('carrier name', unique_carriers)
     truck_type = st.selectbox('truck type', unique_trucks)
     priority_level = st.selectbox('priority', unique_priority)





df = pd.DataFrame({'distance_km': [distance_km],
                    'weight_tons': [weight_tons],
                    'carrier_name': [carrier_name],
                    'truck_type': [truck_type],
                    'priority_level': [priority_level]})

df_encoders = pd.get_dummies(df[['carrier_name', 'truck_type', 'priority_level']])
df = df.drop(['carrier_name', 'truck_type', 'priority_level'], axis=1)
df = pd.concat([df, df_encoders], axis=1)
with open("encoded_data.pkl", "rb") as f:
    encoders = pickle.load(f)
    for col in encoders.columns:
            if col not in df.columns:
                    df[col] = 0
with open('scaled_data.pkl', 'rb') as g:
    scaled = pickle.load(g)
    df[['distance_km', 'weight_tons']] = scaled.transform(df[['distance_km', 'weight_tons']])

df = df[['distance_km', 'weight_tons', 'carrier_name_DB Schenker', 'carrier_name_DHL', 'carrier_name_DPD', 'carrier_name_Kuehne+Nagel', 'carrier_name_Maersk', 'truck_type_Box', 'truck_type_Fridge',
    'truck_type_Tautliner', 'priority_level_Express','priority_level_Standard']]

with open('best_model.pkl', 'rb') as h:
      model = pickle.load(h)
      suggested_cost = model.predict(df)
      suggested_cost = suggested_cost[0]
      suggested_cost = round(suggested_cost,2)
      
# Set show=False to prevent immediate plotting
      
      
st.write(f"given a distance of **{distance_km} KM** and weight of **{weight_tons} tons**,")
st.write(f"using **{carrier_name}**, **{truck_type} Truck**, and **{priority_level} priority**,")
st.write(f"the suggested price is **{suggested_cost:.2f}** Eur")


with open('best_model.pkl', 'rb') as h:
      model = pickle.load(h)
      explainer = shap.Explainer(model.predict, X_train_numeric.iloc[:200])
      shap_values = explainer(X_test_numeric[:200])
      fig, ax = plt.subplots(figsize=(10, 6))
      shap.plots.beeswarm(shap_values, show=False)
      
      plt.title("Factors inlfuencing Spot Freight Cost - highest to lowers")
      plt.tight_layout()
      st.pyplot(fig)
      

      
      
      

 