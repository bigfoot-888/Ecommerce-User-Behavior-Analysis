import pandas as pd

def compute_basic_funnel(df_total):
    # Get the number of unique users that participated in the view, cart, and purchase events

    df_view = df_total[df_total["event_type"] == "view"]
    df_view_unique = df_view["user_id"].unique()
    unique_users_view = len(df_view_unique)

    df_cart = df_total[df_total["event_type"] == "cart"]
    df_cart_unique = df_cart.loc[df_cart["user_id"].isin(df_view_unique), "user_id"].unique()
    unique_users_cart = len(df_cart_unique)

    df_purchase = df_total[df_total["event_type"] == "purchase"]
    df_purchase_unique = df_purchase.loc[df_purchase["user_id"].isin(df_cart_unique), "user_id"].unique()
    unique_users_purchase = len(df_purchase_unique)

    # Get the conversion rates between view-cart and cart-purchase

    cart_conversion_rate = (unique_users_cart / unique_users_view) * 100
    print(f"Percentage of unique users that placed a product in their cart after viewing it: {round(cart_conversion_rate, 2)}%")

    purchase_conversion_rate = (unique_users_purchase / unique_users_cart) * 100
    print(f"Percentage of unique users that purchased a product after placing it in their cart: {round(purchase_conversion_rate, 2)}%")

    # Final data to do the funnel analysis

    funnel_data = dict(
        number = [unique_users_view, unique_users_cart, unique_users_purchase],
        event = ["View", "Cart", "Purchase"]
    )

    df_funnel = pd.DataFrame(funnel_data)
    df_funnel["prct"] = [100, round(cart_conversion_rate, 2), round(purchase_conversion_rate, 2)]
    
    return df_funnel

def compute_price_segmented_funnel(df_total):
    segments = ["Low", "Medium", "High"]
    df_funnel_price = pd.DataFrame()

    price_segments = []

    df_view = df_total[df_total["event_type"] == "view"]
    df_cart = df_total[df_total["event_type"] == "cart"]
    df_purchase = df_total[df_total["event_type"] == "purchase"]

    for idx, segment in enumerate(segments):
        
        df_view_unique = df_view.loc[(df_view["price_range"] == segment), "user_id"].unique()
        views = len(df_view_unique)

        df_cart_unique = df_cart.loc[(df_cart["user_id"].isin(df_view_unique)) & (df_cart["price_range"] == segment), "user_id"].unique()
        carts = len(df_cart_unique)

        df_purchase_unique = df_purchase.loc[(df_purchase["user_id"].isin(df_cart_unique)) & (df_purchase["price_range"] == segment), "user_id"].unique()
        purchases = len(df_purchase_unique)
        
        price_segments.append([views, carts, purchases])
        
    df_funnel_price = pd.DataFrame(price_segments)

    df_funnel_price["price_range"] = ["Low", "Medium", "High"]
    df_funnel_price = df_funnel_price.rename(columns = {0: "View", 1: "Cart", 2: "Purchase"})
        
    df_funnel_price["View_Rates"] = [100, 100, 100]
    df_funnel_price["Cart_Rates"] = round((df_funnel_price["Cart"] / df_funnel_price["View"]) * 100, 2)
    df_funnel_price["Purchase_Rates"] = round((df_funnel_price["Purchase"] / df_funnel_price["Cart"]) * 100, 2)
    df_funnel_price["Overall_Conversion_Rate"] = round((df_funnel_price["Purchase"] / df_funnel_price["View"]) * 100, 2)
    
    return df_funnel_price