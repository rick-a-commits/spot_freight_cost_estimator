# Spot Freight Cost Estimator

#### The aim of this notebook is to first analyse an imaginary company's logistics data to understands its costs, carriers and shipping routes. Finally, using historical data, the aim is to build a model that can predict logistical costs given a set of features. This predicted cost should serve as a flexible guide for Spot Freight negotiations when contracted carriers cannot meed requests and a spot freight is needed.

| Column Name              | Description                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------- |
| **shipment\_id**         | Unique identifier for each shipment.                                                               |
| **carrier\_name**        | Name of the shipping company or carrier handling the shipment (e.g., Maersk, DPD).                 |
| **truck\_type**          | Type of truck used for shipment (e.g., Fridge, Box, Tautliner), indicating equipment and capacity. |
| **distance\_km**         | Distance of the shipment route in kilometers.                                                      |
| **weight\_tons**         | Weight of the shipment in metric tons.                                                             |
| **volume\_m3**           | Volume of the shipment cargo in cubic meters.                                                      |
| **delivery\_time\_days** | Estimated or planned delivery time in days.                                                        |
| **priority\_level**      | Shipping priority category (e.g., Standard, Express), indicating speed and urgency of delivery.    |
| **origin\_country**      | Country from which the shipment originates.                                                        |
| **destination\_country** | Country where the shipment is delivered.                                                           |
| **fuel\_price\_eur\_l**  | Fuel price in euros per liter at the time of shipment, affecting transportation cost.              |
| **cost\_eur**            | Total cost of the shipment in euros, the target variable for modeling shipment costs.              |
