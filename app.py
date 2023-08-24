import streamlit as st
from azure.cosmos import CosmosClient

# Azure Cosmos DBの設定
URL = 'https://adachitakehirodemo3.documents.azure.com:443/'
KEY = 'C7Z6MXR3EUj5DGngcK4dF84ZZr0yfjPhZPCheo635tFgbUIbZ3GZJG3MWD3lis5PDkHAW63w7BAZACDbPuTKGw=='
DATABASE_NAME = 'SampleTestDB'
CONTAINER_NAME = 'Test'

client = CosmosClient(URL, credential=KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

st.title("Azure Cosmos DB with Streamlit!")

# データのアップロード
st.subheader("Upload Data to Cosmos DB")
data_key = st.text_input("Enter a key:")
data_value = st.text_input("Enter a value:")

if st.button("Upload"):
    item_body = {
        "id": data_key,
        "value": data_value
    }
    container.upsert_item(item_body)
    st.success(f"Uploaded data with key: {data_key}")

# データの取得と表示
st.subheader("Retrieve Data from Cosmos DB")
query_key = st.text_input("Enter key to retrieve:")

if st.button("Retrieve"):
    query = f"SELECT * FROM c WHERE c.id = '{query_key}'"
    results = list(container.query_items(query=query, enable_cross_partition_query=True))
    
    if results:
        st.write(results[0])
    else:
        st.warning(f"No data found for key: {query_key}")
