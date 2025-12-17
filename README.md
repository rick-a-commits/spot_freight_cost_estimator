# Spot Freight Cost Estimator

## Project Overview

This project analyzes an imaginary company’s logistics data to understand shipment costs, carriers, and routes, and then builds a machine learning model to **predict spot freight costs** based on historical data.

The predicted cost is intended to act as a **decision-support guide during spot freight negotiations**, particularly when contracted carriers cannot meet demand and ad‑hoc (spot) freight solutions are required.

The project has evolved from a single exploratory notebook into a **structured, reproducible, and deployable cost‑estimation tool**.

---

## Dataset Description

The dataset contains historical shipment records with operational, geographic, and cost‑related features:

| Column Name             | Description                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **shipment_id**         | Unique identifier for each shipment.                                                               |
| **carrier_name**        | Name of the shipping company or carrier handling the shipment (e.g., Maersk, DPD).                 |
| **truck_type**          | Type of truck used for shipment (e.g., Fridge, Box, Tautliner), indicating equipment and capacity. |
| **distance_km**         | Distance of the shipment route in kilometers.                                                      |
| **weight_tons**         | Weight of the shipment in metric tons.                                                             |
| **volume_m3**           | Volume of the shipment cargo in cubic meters.                                                      |
| **delivery_time_days**  | Estimated or planned delivery time in days.                                                        |
| **priority_level**      | Shipping priority category (e.g., Standard, Express), indicating speed and urgency of delivery.    |
| **origin_country**      | Country from which the shipment originates.                                                        |
| **destination_country** | Country where the shipment is delivered.                                                           |
| **fuel_price_eur_l**    | Fuel price in euros per liter at the time of shipment, affecting transportation cost.              |
| **cost_eur**            | Total cost of the shipment in euros (target variable).                                             |

---

## Project Structure

* **EDA.ipynb** – Exploratory Data Analysis to understand cost drivers, distributions, and relationships
* **models.ipynb** – Feature engineering, model training, evaluation, and selection
* **app.py** – Streamlit application for interactive cost prediction
* **best_model.pkl** – Serialized trained model used for inference
* **scaled_data.pkl / encoded_data.pkl** – Saved preprocessing artifacts
* **x_train_numeric.csv / x_test_numeric.csv** – Train/test splits for reproducibility
* **shipment_costs_10000.csv** – Input dataset
* **requirements.txt** – Python dependencies

---

## Modeling Approach

* **Model type:** Linear Regression
* **Target variable:** `cost_eur`
* **Evaluation metric:** R² score
* **Performance:** R² ≈ **0.84** on the test set

The model captures the relationship between shipment characteristics, distance, fuel prices, and service constraints to produce cost estimates suitable for real‑world negotiation support.

---

## Deployment

The trained model is **deployable via Streamlit** using `app.py`, allowing users to:

* Input shipment characteristics
* Apply the same preprocessing pipeline used during training
* Receive an estimated spot freight cost instantly

### How to Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Use Case

This project is designed as a **proof‑of‑concept pricing tool** for:

* Logistics planners
* Procurement teams
* Supply chain analysts

It demonstrates how historical logistics data can be transformed into a practical cost‑estimation system to support time‑sensitive spot freight decisions.

---

## Future Improvements

* Add additional models (e.g., Random Forest, Gradient Boosting) for comparison
* Expand evaluation metrics (MAE, RMSE, residual analysis)
* Package preprocessing and inference into a unified pipeline
* Add automated tests and CI workflows
* Deploy the app to a cloud platform