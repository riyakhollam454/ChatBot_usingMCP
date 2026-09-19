import pandas as pd 
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Sales Server")


def load_data():
    return pd.read_csv(r"C:\Users\riyak\OneDrive\Desktop\MCP_proj\Sales_data.csv")


# Tool - 1

@mcp.tool()

def get_total_sales() -> float:
    """Calculate total sales from the sales data."""

    df = load_data() 

    total_sales = (df["Quantity"] * df["Price"]).sum()

    return float(total_sales)

# Tool - 2 

@mcp.tool()

def get_product_sales(product:str)->float:
    """Calculate sales for specific Product from the sales data."""
    df = load_data()

    product_df = df[df["Product"].str.lower() == product.lower()]

    if product_df.empty:
        return 0.0
    
    sales = (product_df["Quantity"] * product_df["price"]).sum()
    return float(sales)

# Tool - 3 

@mcp.tool()
def get_category_sales(category: str) -> float:
    """Calculate total sales for a specific category."""
    
    df = load_data()
    
    category_df = df[df["Category"].str.lower() == category.lower()]
    
    if category_df.empty:
        return 0.0
    
    sales = (category_df["Quantity"] * category_df["Price"]).sum()
    
    return float(sales)

# Tool - 4 

@mcp.tool()
def get_top_product() -> str:
    """Find the product with highest sales."""

    df = load_data()

    df["Sales"] = df["Quantity"] * df["Price"]

    product_sales = df.groupby("Product")["Sales"].sum()

    top_product = product_sales.idxmax()

    return top_product


# Run MCP server

if __name__ == "__main__":
    mcp.run()
