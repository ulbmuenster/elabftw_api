# %% [markdown]
# # Start Script & establish a connection to elabFTW

# %% [markdown]
# ## 1. Generate an API Key ("schreibgeschützt"): https://elab-staging.uni-muenster.de/ucp.php?tab=4
#
# (API Docs: https://doc.elabftw.net/api/v2/)

# %%
from elabftw_api_client import ElabFTW

# %%
API_KEY = ""
ftw = ElabFTW(
    "https://elab-staging.uni-muenster.de/",
    API_KEY,
)

# %% [markdown]
# ## Check connection

# %%
ftw.check_connection()

# %% [markdown]
# ## Get all items (ressources) you have access to
#
# Returns a list of dictionaries.

# %%
items = ftw.get_ressources()

# %% [markdown]
# Your can access all titels for example like this:

# %%
for item in items:
    print(item["title"])

# %% [markdown]
# If this returns nothing, you might not have any items yet. Check https://elab-staging.uni-muenster.de/database.php to make sure.

# %% [markdown]
# # Create a new ressource

# %% [markdown]
# ### Get all current ressource categories

# %%
for category in ftw.get_ressource_categories():
    print(category["title"] + " (ID:" + str(category["id"]) + ")")

# %% [markdown]
# Prepare a new ressouce. Allowed arguments are:
#
# - `category_id` as `int`
# - `tags` as a list of `str`
# - `tittle` as `str`
# - `body` as `str`
# - `metadata` as `dict`

# %%
metadata = {"testkey": "ABC", "second key": "DEF"}
new_item = ftw.create_ressource(
    category_id=18, title="Random test name", body="Random test body", metadata=metadata
)

# %% [markdown]
# ## Read CSV and create Ressources

# %%
import pandas as pd

df = pd.read_csv("items.csv")
df

# %% [markdown]
# Reading an Excel file is equally simple: `df = pd.read_excel("items.csv")`

# %%
df2 = pd.read_excel("Example_cons.xlsx")
df2

# %%
for index, row in df.iterrows():
    print(f"Creating item {row['title']}")
    body = f"Supplier: {row['Supplier']},\nNo: {row['No']},\nStock: {row['Stock']}"
    metadata = {"Supplier": row["Supplier"], "No": row["No"], "Stock": row["Stock"]}
    ftw.create_ressource(
        category_id=18, title=row["title"], body=body, metadata=metadata
    )

# %%
