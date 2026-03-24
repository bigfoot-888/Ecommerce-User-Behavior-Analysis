import pandas as pd

# Read the processed data

df_total = pd.read_parquet("../data/processed/df.parquet.gzip")

# Get the number of unique users that participated in the view, cart, and purchase events

df_view = df_total[df_total["event_type"] == "view"]
unique_users_view = df_view["user_id"].nunique()
print(f"Number of unique users that viewed a product: {unique_users_view}")

df_cart = df_total[df_total["event_type"] == "cart"]
unique_users_cart = df_cart["user_id"].nunique()
print(f"Number of unique users that placed products after viewing in their cart: {unique_users_cart}")

df_purchase = df_total[df_total["event_type"] == "purchase"]
unique_users_purchase= df_purchase["user_id"].nunique()
print(f"Number of unique users that purchased a product in their carts: {unique_users_purchase}")

# Get the conversion rates between view-cart and cart-purchase

cart_conversion_rate = (unique_users_cart / unique_users_view) * 100
print(f"Percentage of unique users that placed a product in their cart after viewing it: {round(cart_conversion_rate, 2)}%")

purchase_conversion_rate = (unique_users_purchase / unique_users_cart) * 100
print(f"Percentage of unique users that purchased a product after placing it in their cart: {round(purchase_conversion_rate, 2)}%")

# Make the initial funnel chart

import plotly.express as px
funnel_data = dict(
    number = [unique_users_view, unique_users_cart, unique_users_purchase],
    event = ["View", "Cart", "Purchase"]
)

df_funnel = pd.DataFrame(funnel_data)
df_funnel["prct"] = [100, round(cart_conversion_rate, 2), round(purchase_conversion_rate, 2)]
fig = px.funnel(df_funnel, x = "number", y = "event", title="E-Commerce Funnel Analysis", text="prct")
fig.update_traces(textposition='inside',texttemplate="%{x:.0f\n}<br>%{text:.2f}"+'%')
fig.show()

# The funnel chart grouped by price range as well

df_funnel_price = df_total.groupby(["event_type", "price_range"])["user_id"].nunique().reset_index()
df_funnel_price = df_funnel_price.rename(columns={"user_id": "unique_users"})
df_funnel_price

fig = px.funnel(df_funnel_price, x = "unique_users", y = "event_type", color = "price_range", category_orders={"event_type": ["purchase", "cart", "view"]},)
fig.show()