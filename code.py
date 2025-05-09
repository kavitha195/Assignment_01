import streamlit as st
import pandas as pd
import sqlite3
# Connect to SQLite (This will create a new database file if it doesn't exist)
connection = sqlite3.connect('food_management.db')

# Creates a database file 'food_management.db'
print("Connected to SQLite database!")

#Create a cursor object
cursor = connection.cursor()
st.sidebar.title(":red[Navigation]")
st.header(":blue[LOCAL FOOD WASTAGE MANAGEMENT SYSTEM]")

# load csv data files
A = pd.read_csv(r"C:\Users\jothi\Desktop\GUVI_1 Project\providers_data.csv")
B = pd.read_csv(r"C:\Users\jothi\Desktop\GUVI_1 Project\receivers_data.csv")
C = pd.read_csv(r"C:\Users\jothi\Desktop\GUVI_1 Project\food_listings_data.csv")
D = pd.read_csv(r"C:\Users\jothi\Desktop\GUVI_1 Project\claims_data.csv")

# Sidebar selectbox
f1 = st.sidebar.selectbox(":red[Home]", ("Select the DATA", "project introduction", "Dataset tables",))
if f1 == "project introduction":
    selected_table = st.sidebar.selectbox("Select the data ", ["project introduction"])
    st.write("I am over helmed in all humbleness and gratefulness to acknowledge my depth to all thosewho have helped me to put these ideas, well above the level of simplicity and into somethingconcrete.")
    st.image(r"C:\Users\jothi\Downloads\istockphoto-2193896250-1024x1024.jpg")
# Button to trigger data display
if f1 == "Dataset tables":
    st.sidebar.subheader("Dataset tables")
    selected_table = st.sidebar.selectbox("Select the data ", ["Providers", "Receivers", "Food Listings", "Claims"])
    if selected_table == "Providers":
        st.subheader("Providers Data")
        st.dataframe(A)
    elif selected_table == "Receivers":
        st.subheader("Receivers Data")
        st.dataframe(B)
    elif selected_table == "Food Listings":
        st.subheader("Food Listings Data")
        st.dataframe(C)
    elif selected_table == "Claims":
        st.subheader("Claims Data")
        st.dataframe(D)
    else:
        st.write("Please select a dataset.")
connection.commit()

# Create a PROVIDERS table
cursor.execute('''
CREATE TABLE IF NOT EXISTS providers (
    Provider_ID INTEGER PRIMARY KEY,
    Provider_Name TEXT,
    Type TEXT,
    Address TEXT,
    City TEXT,
    Contact TEXT)
''')
# Commit the changes (required to save)
connection.commit()
print("Table created successfully!")
#Creating RECEIVERS tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Receivers (
        Receiver_ID INTEGER PRIMARY KEY,
        Name TEXT,
        Type TEXT,
        City TEXT,
        Contact TEXT
    )
''')
# Commit the changes (required to save)
connection.commit()
print("Table created successfully!")
#Creating Food_listings tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FOOD_LISTINGS (
        FOOD_ID INTEGER PRIMARY KEY,
        FOOD_Name TEXT,
        QUANITTY INTEGER,
        Expiry_Date DATE,
        Provider_ID INTEGER,
        Provider_Type TEXT,
        Location TEXT,
        food_Type TEXT,
        Meal_Type TEXT

    )
''')
# Commit the changes (required to save)
connection.commit()
print("Table created successfully!")
#Creating CLAIM tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Claims (
        CLAIM_ID INTEGER PRIMARY KEY,
        FOOD_ID INTEGER,
        Receiver_ID INTEGER,
        Status TEXT,
        Timestamp DATETIME

    )
''')
# Commit the changes (required to save)
connection.commit()
print("Table created successfully!")

#values insert in to Providers table

for row in A.values.tolist():
   provider_ID = row[0]  # Assuming Provider_ID is the first element in the row
   cursor.execute("SELECT 1 FROM providers WHERE Provider_ID = ?", (provider_ID,))
   existing_provider = cursor.fetchone()

if not existing_provider:
        cursor.execute('''
            INSERT INTO providers (Provider_ID, Provider_Name, Type, Address, City, Contact)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', row)


#values insert in to receivers table

for row in B.values.tolist():
   Receiver_id = row[0]  # Assuming receivers_ID is the first element in the row
   cursor.execute("SELECT 1 FROM Receivers WHERE Receiver_ID = ?", (Receiver_id,))
   existing_Receiver = cursor.fetchone()

if not existing_Receiver:
        cursor.execute('''
            INSERT INTO receivers (receiver_ID, Name, Type, City, Contact)
            VALUES (?, ?, ?, ?, ?)
            ''', row)

connection.commit()

#values insert in to Food_listings table
for row in C.values.tolist():
    FOOD_ID = row[0]  # Assuming food_ID is the first element in the row
    cursor.execute("SELECT 1 FROM FOOD_LISTINGS WHERE FOOD_ID = ?", (FOOD_ID,))
    existing_FOOD_LISTINGS = cursor.fetchone()

if not existing_FOOD_LISTINGS:
        cursor.execute('''
            INSERT INTO FOOD_LISTINGS (FOOD_ID, FOOD_Name, QUANITTY,Expiry_Date, provider_ID, provider_Type, Location, food_Type, Meal_Type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )
        ''', row)

connection.commit()
print("Table values insert sucessfully")
#values insert in to Claims table
for row in D.values.tolist():
    CLAIM_ID = row[0]  # Assuming receivers_ID is the first element in the row
    cursor.execute("SELECT 1 FROM Claims WHERE CLAIM_ID = ?", (CLAIM_ID,))
    existing_Claims = cursor.fetchone()

if not existing_Claims:
        cursor.execute('''
            INSERT INTO Claims (CLAIM_ID, FOOD_ID, Receiver_ID, Status, Timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', row)

connection.commit()
print("Table values insert sucessfully")


data_path = r"C:\Users\jothi\Desktop\GUVI_1 Project\providers_data.csv"
 

# Load data
df = pd.read_csv(data_path)

# Sidebar

# st.sidebar.title("CRUD operations")
st.sidebar.markdown("<h3 style='font-size: 18px;'>CRUD operations</h3>", unsafe_allow_html=True)

#crud_operation = st.sidebar.selectbox("Select operation", ["Select","Create", "Read", "Update", "Delete"])

# Create

#if crud_operation == "Create":
 #   st.subheader("Create New Provider")
  #  provider_id = st.text_input("Provider ID")
   # name = st.text_input("Name")
    #type_ = st.text_input("Type")
#df = pd.read_csv(data_path)
#st.sidebar.markdown("<h3 style='font-size: 18px;'>CRUD operations</h3>", unsafe_allow_html=True)

## CRUD OPERATIONS
# File paths
provider_path = r"C:\Users\jothi\Desktop\GUVI_1 Project\providers_data.csv"
receiver_path = r"C:\Users\jothi\Desktop\GUVI_1 Project\receivers_data.csv"
food_path = r"C:\Users\jothi\Desktop\GUVI_1 Project\food_listings_data.csv"
Claims_path = r"C:\Users\jothi\Desktop\GUVI_1 Project\claims_data.csv"

# Sidebar
dataset_option = st.sidebar.selectbox("Select Dataset", ["Providers","receivers", "Food Listings", "Claims"])
crud_operation = st.sidebar.selectbox("Select Operation", ["Select", "Create", "Read", "Update", "Delete"])
# Load the appropriate dataset
if dataset_option == "providers":
    data_path = provider_path
elif dataset_option == "receivers":
    data_path = receiver_path
elif dataset_option == "Food listings":
    data_path = food_path
elif dataset_option == "Claims":
    data_path = Claims_path



# Create
if crud_operation == "Create":
    st.subheader(f"Create New {dataset_option}")
    if dataset_option == "Providers":
        Provider_ID = st.text_input("Provider ID")
        Name = st.text_input("Name")
        Type = st.text_input("Type")
        City = st.text_input("City")
        Contact = st.text_input("Contact")

        if st.button("Add Provider"):
            new_data = {
                "Provider_ID": Provider_ID,
                "Name": Name,
                "Type": Type,
                "City": City,
                "Contact": Contact
            }
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(data_path, index=False)
            st.success("Provider added successfully!")
            st.dataframe(df)


    elif dataset_option == "receivers":
        Receiver_ID = st.text_input("receiver ID")
        Name = st.text_input("Name")
        Type = st.text_input("Type")
        City = st.text_input("City")
        Contact = st.text_input("Contact")

        if st.button("Add receiver"):
            new_data = {
                "receiver_ID": receiver_ID,
                "Name": Name,
                "Type": Type,
                "City": City,
                "Contact": Contact
            }
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(data_path, index=False)
            st.success("receiver added successfully!")
            st.dataframe(df)

    elif dataset_option == "Food Listings":
        Food_ID = st.text_input("Food ID")
        Food_Name = st.text_input("Food Name")
        Quantity = st.text_input("Quanitty")
        Expiry_Date = st.text_input("Expiry Date")
        Provider_ID = st.text_input("Provider ID")
        Provider_Type = st.text_input("Provider Type")
        Location = st.text_input("Location")
        Food_Type = st.text_input("Food Type")
        Meal_Type = st.text_input("Meal Type")

        if st.button("Add Food Listing"):
            new_data = {
                "Food_ID": Food_ID,
                "Food_Name": Food_Name,
                "Quantity": Quantity,
                "Expiry_Date": Expiry_Date,
                "Provider_ID": Provider_ID,
                "Provider_Type": Provider_Type,
                "Location": Location,
                "Food_Type": Food_Type,
                "Meal_Type": Meal_Type
            }
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(data_path, index=False)
            st.success("Food listing added successfully!")
            st.dataframe(df)

    elif dataset_option == "Claims":
        Claim_ID = st.text_input("Claim ID")
        Food_ID = st.text_input("Food ID")
        Receiver_ID = st.text_input("receiver ID")
        Status = st.text_input("Status")
        Timestamp = st.text_input("Timestamp")

        if st.button("Add Claim"):
            new_data = {
                "Claim_ID": Claim_ID,
                "Food_ID": Food_ID,
                "Receiver_ID": Receiver_ID,
                "Status": Status,
                "Timestamp": Timestamp
            }
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(data_path, index=False)
            st.success("Claim added successfully!")
            st.dataframe(df)


# Read
elif crud_operation == "Read":
    st.subheader(f"{dataset_option} Records")
    st.dataframe(df)

# Update
elif crud_operation == "Update":
    st.subheader(f"Update {dataset_option} Info")
    st.dataframe(df)
    if len(df) > 0:
        row_index = st.number_input("Row index to update", min_value=0, max_value=len(df)-1, step=1)
        selected = df.iloc[row_index]
        if dataset_option == "Providers":
            Provider_ID = st.text_input("Provider ID", selected["Provider_ID"])
            Name = st.text_input("Name", selected["Name"])
            Type = st.text_input("Type", selected["Type"])
            City = st.text_input("City", selected["City"])
            Contact = st.text_input("Contact", selected["Contact"])

            if st.button("Update Provider"):
                df.at[row_index, "Provider_ID"] = Provider_ID
                df.at[row_index, "Name"] = Name
                df.at[row_index, "Type"] = Type
                df.at[row_index, "City"] = City
                df.at[row_index, "Contact"] = Contact
                df.to_csv(data_path, index=False)
                st.success("Provider updated successfully!")
                st.dataframe(df)

        elif dataset_option == "receivers":
            Receiver_ID = st.text_input("receiver ID", selected["receiver_ID"])
            Name = st.text_input("Name", selected["Name"])
            Type = st.text_input("Type", selected["Type"])
            City = st.text_input("City", selected["City"])
            Contact = st.text_input("Contact", selected["Contact"])

            if st.button("Update receiver"):
                df.at[row_index, "receiver_ID"] = receiver_ID
                df.at[row_index, "Name"] = Name
                df.at[row_index, "Type"] = Type
                df.at[row_index, "City"] = City
                df.at[row_index, "Contact"] = Contact
                df.to_csv(data_path, index=False)
                st.success("receiver updated successfully!")
                st.dataframe(df)

        elif dataset_option == "Food Listings":
            Food_ID = st.text_input("Food ID", selected["Food_ID"])
            Food_Name = st.text_input("Food Name", selected["Food_Name"])
            Quantity = st.text_input("Quanitty", selected["Quanitty"])
            Expiry_Date = st.text_input("Expiry Date", selected["Expiry_Date"])
            Provider_ID = st.text_input("Provider ID", selected["Provider_ID"])
            Provider_Type = st.text_input("Provider Type", selected["Provider_Type"])
            Location = st.text_input("Location", selected["Location"])
            Food_Type = st.text_input("Food Type", selected["Food_Type"])
            Meal_Type = st.text_input("Meal Type", selected["Meal_Type"])

            if st.button("Update Food Listing"):
                df.at[row_index, "Food_ID"] = Food_ID
                df.at[row_index, "Food_Name"] = Food_Name
                df.at[row_index, "Quanitty"] = Quanitty
                df.at[row_index, "Expiry_Date"] = Expiry_Date
                df.at[row_index, "Provider_ID"] = Provider_ID
                df.at[row_index, "Provider_Type"] = Provider_Type
                df.at[row_index, "Location"] = Location
                df.at[row_index, "Food_Type"] = Food_Type
                df.at[row_index, "Meal_Type"] = Meal_Type
                df.to_csv(data_path, index=False)
                st.success("Food listing updated successfully!")
                st.dataframe(df)

        elif dataset_option == "Claims":
            Claim_ID = st.text_input("Claim ID", selected["Claim_ID"])
            Food_ID = st.text_input("Food ID", selected["Food_ID"])
            Receiver_ID = st.text_input("receiver ID", selected["receiver_ID"])
            Status = st.text_input("Status", selected["Status"])
            Timestamp = st.text_input("Timestamp", selected["Timestamp"])

            if st.button("Update Claim"):
                df.at[row_index, "Claim_ID"] = Claim_ID
                df.at[row_index, "Food_ID"] = Food_ID
                df.at[row_index, "receiver_ID"] = Receiver_ID
                df.at[row_index, "Status"] = Status
                df.at[row_index, "Timestamp"] = Timestamp
                df.to_csv(data, index=False)
                st.success("Claim updated successfully!")
                st.dataframe(df)

        
# Delete
elif crud_operation == "Delete":
    st.subheader(f"Delete {dataset_option}")
    st.dataframe(df)
    if len(df) > 0:
        row_index = st.number_input("Row index to delete", min_value=0, max_value=len(df)-1, step=1)
        if st.button(f"Delete {dataset_option[:-1]}"):
            df = df.drop(index=row_index).reset_index(drop=True)
            df.to_csv(data_path, index=False)
            st.success(f"{dataset_option[:-1]} deleted successfully!")
            st.dataframe(df)



st.sidebar.subheader("Learners SQL Query")

query_option = st.sidebar.selectbox("Choose a query to run:", (
    "1. Which city has the highest number of food providers?",
    "2. Get details of provider ID 768",
    "3. Which city has the highest number of food receivers?",
    "4. What is the date and time of the highest food claims?",
    "5. List the most claimed breakfast food"
))

if st.sidebar.button("CLICK"):
    
    # 1. Which city has the highest total quantity of food provided by a provider?
  if query_option == "1. Which city has the highest number of food providers?":
        cursor.execute("""
        SELECT City, Provider_Name, SUM(QUANITTY) AS TotalQuantity
        FROM FOOD_LISTINGS
        JOIN providers ON FOOD_LISTINGS.Provider_ID = providers.Provider_ID
        GROUP BY City, Provider_Name
        ORDER BY TotalQuantity DESC
        LIMIT 1;
        """)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=[i[0]for i in cursor.description])
        st.write("City with highest total quantity of food provided:")
        st.dataframe(df)


    # 2. Get details of provider ID 768
  elif query_option == "2. Get details of provider ID 768":
        cursor.execute("SELECT * FROM providers WHERE Provider_ID = 768;")
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)
        st.write("Details of provider ID 768:")
        st.dataframe(df)

    # 3. Which city has the highest number of food receivers?
  elif query_option == "3. Which city has the highest number of food receivers?":
        cursor.execute("""
            SELECT City, COUNT(*) AS ReceiverCount
            FROM receivers
            GROUP BY City
            ORDER BY ReceiverCount DESC
            LIMIT 1;
        """)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=["City", "ReceiverCount"])
        st.write("City with most food receivers:")
        st.dataframe(df)

    # 4. What is the date and time of the highest food claims?
  elif query_option == "4. What is the date and time of the highest food claims?":
        cursor.execute("""
            SELECT Timestamp, FOOD_Name, QUANITTY
            FROM Claims
            JOIN FOOD_LISTINGS ON Claims.FOOD_ID = FOOD_LISTINGS.FOOD_ID
            ORDER BY QUANITTY DESC
            LIMIT 1;
        """)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=["Timestamp", "FOOD_Name", "QUANITTY"])
        st.write("Highest food claim record:")
        st.dataframe(df)

    # 5. List the most claimed breakfast food
  elif query_option == "5. List the most claimed breakfast food":
        cursor.execute("""
            SELECT FOOD_Name, COUNT(*) AS ClaimCount
            FROM FOOD_LISTINGS
            JOIN Claims ON FOOD_LISTINGS.FOOD_ID = Claims.FOOD_ID
            WHERE Meal_Type = 'Breakfast'
            GROUP BY FOOD_Name
            ORDER BY ClaimCount DESC
            LIMIT 1;
        """)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=["FOOD_Name", "ClaimCount"])
        st.write("Most claimed breakfast food:")
        st.dataframe(df)


connection.commit()


# GIVEN SQL QUERIES


st.sidebar.subheader("SQL Queries")
query_option = st.sidebar.selectbox("Select the Query", (
    "Select the Query",
    "1.How many food providers and receivers are there in each city?",
    "2.Which type of food provider contributes the most food?",
    "3.What is the contact information of food providers in a specific City?",
    "4.Which receivers have claimed the most food?",
    "5.What is the total quantity of food available from all providers?",
    "6.Which city has the highest number of food listings?",
    "7.What are the most commonly available food types?",
    "8.How many food claims have been made for each food item?",
    "9.Which provider has had the highest number of successful food claims?",
    "10.What percentage of food Claims are completed vs. pending vs. canceled?",
    "11.What is the average quanitty of food claimed per receiver?",
    "12.Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?",
    "13.What is the total quanitty of food donated by each provider?"
))

## 1.How many food providers and receivers are there in each city?
if query_option == "1.How many food providers and receivers are there in each city?":
    cursor.execute("""
    SELECT p.City, COUNT(DISTINCT p.Provider_ID) AS ProviderCount,
    COUNT(DISTINCT r.Receiver_ID) AS ReceiverCount
    FROM providers p
    LEFT JOIN receivers r ON p.City = r.City
    GROUP BY p.City
    ORDER BY p.City;
    """)
    st.write("food providers and receivers are there in each city:")
    st.dataframe(pd.DataFrame(cursor.fetchall(), columns=["City", "Providers", "Receivers"]))
    
    

##2. Which type of food provider contributes the most food?
elif query_option == "2.Which type of food provider contributes the most food?":
    cursor.execute("""
     SELECT Provider_Type, SUM(QUANITTY) AS TotalQuantity
     FROM FOOD_LISTINGS
     GROUP BY Provider_Type
     ORDER BY TotalQuantity DESC
     LIMIT 1   
     """)
    
    result = cursor.fetchall()
    st.write("food provider contributes are:")
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)

   
 #3.  What is the contact information of food providers in a specific city?  
elif query_option == "3.What is the contact information of food providers in a specific City?":  
    cursor.execute(f"""SELECT Provider_Name, Contact FROM providers where City = "Lake Jesusview" """)
    #st.selectbox = ("enter the city")
    #[city] and Contact = [contact]""") 
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.write("Contact information of food providers is:Lake Jesusview")
    st.dataframe(df)
    
    
##4.Which receivers have claimed the most food?
elif query_option =="4.Which receivers have claimed the most food?":  
    cursor.execute( """
     SELECT
     r.Name,
     COUNT(C.CLAIM_ID) AS TotalClaims
     FROM
     Receivers r
     JOIN
     Claims c ON r.Receiver_ID = c.Receiver_ID
     GROUP BY
     r.Name
     ORDER BY
     TotalClaims DESC
     LIMIT 1; 
     """)
    result = cursor.fetchall()
    st.write("Receiver with the most claims:")
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)
    
    
#5.What is the total quantity of food available from all providers?
elif query_option =="5.What is the total quantity of food available from all providers?":
    cursor.execute( """
     SELECT SUM(QUANITTY) AS TotalFoodQuanitty
     FROM FOOD_LISTINGS;
     """)
    result = cursor.fetchall()
    st.write("Total quanitty of food available from all providers:")
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)

##6.Which city has the highest number of food listings?
elif query_option =="6.Which city has the highest number of food listings?":
    cursor.execute( """
     SELECT Location, COUNT(*) AS ListingCount
     FROM FOOD_LISTINGS
     GROUP BY Location
     ORDER BY ListingCount DESC
     LIMIT 1;
     """)
    result = cursor.fetchone()
    st.write("The city with the highest number of food listings is:")
    df = pd.DataFrame(result, columns=["City"])
    st.dataframe(df)
    
    
##7.What are the most commonly available food types?
elif query_option == "7.What are the most commonly available food types?":
    cursor.execute("""
     SELECT food_Type, COUNT(*) AS FoodTypeCount
     FROM FOOD_LISTINGS
     GROUP BY food_Type
     ORDER BY FoodTypeCount DESC
     LIMIT 5;  
     """)
    result = cursor.fetchall()
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)


##8.How many food claims have been made for each food item?
elif query_option == "8.How many food claims have been made for each food item?":
    cursor.execute("""
     SELECT
     fl.FOOD_Name,
     COUNT(c.CLAIM_ID) AS ClaimCount
     FROM
     FOOD_LISTINGS fl
     LEFT JOIN
     Claims c ON fl.FOOD_ID = c.FOOD_ID
     GROUP BY
     fl.FOOD_Name
     ORDER BY
     ClaimCount DESC;
     """)

    result = cursor.fetchall()
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)  
    

##9.Which provider has had the highest number of successful food claims?
elif query_option == "8.Which provider has had the highest number of successful food claims?":
    cursor.execute("""
     SELECT Provider_Name
     FROM providers
     WHERE Provider_ID IN (
     SELECT Provider_ID
     FROM FOOD_LISTINGS
     WHERE FOOD_ID IN (
        SELECT FOOD_ID
        FROM Claims
        WHERE Status = 'claimed'
        GROUP BY FOOD_ID
        ORDER BY COUNT(*) DESC
        LIMIT 1
        )
        )
   """); 
    result = cursor.fetchall()
    st.write("The highest number of successful food claims:") 
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df) 
    
    
#10.What percentage of food claims are completed vs. pending vs. canceled?    
elif query_option == "10.What percentage of food Claims are completed vs. pending vs. canceled?":
    cursor.execute(f"""
     SELECT Status, CAST(COUNT(*) AS REAL) * 100 / (SELECT COUNT(*) FROM Claims) AS Percentage
     FROM Claims
     GROUP BY Status""")
    result = cursor.fetchall() 
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df) 


#11.What is the average quanitty of food claimed per receiver?
elif query_option == "11.What is the average quanitty of food claimed per receiver?":   
    cursor.execute("""
     SELECT CAST(SUM(fl.QUANITTY) AS REAL) / COUNT(DISTINCT c.Receiver_ID) AS AverageQuanitty
     FROM Claims c
     JOIN FOOD_LISTINGS fl ON c.FOOD_ID = fl.FOOD_ID;
     """)
    result = cursor.fetchone()
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.write("Average quanitty of food claimed per receiver:")
    st.dataframe(df) 

    
##12.Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?
elif query_option == "12.Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?":
    cursor.execute("""
     SELECT Meal_Type, COUNT(*) AS ClaimCount
     FROM FOOD_LISTINGS
     JOIN Claims ON FOOD_LISTINGS.FOOD_ID = Claims.FOOD_ID
     GROUP BY Meal_Type
     ORDER BY ClaimCount DESC
     LIMIT 1;
     """)
    result = cursor.fetchone()
    df = pd.DataFrame(result,columns =[['Meal_Type'],['Claims']])
    #df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.write("The most claimed food is:")
    st.dataframe(df) 

    
##13.What is the total quantity of food donated by each provider?
elif query_option == "13.What is the total quanitty of food donated by each provider?":
    cursor.execute("""
     SELECT p.Provider_Name, SUM(fl.QUANITTY) AS TotalDonatedQuanitty
     FROM providers p
     JOIN FOOD_LISTINGS fl ON p.Provider_ID = fl.Provider_ID
     GROUP BY p.Provider_Name
     ORDER BY TotalDonatedQuanitty DESC;
     """)
    result = cursor.fetchall()
    st.write("Total Quantity of Food Donated by Each Provider:")
    df = pd.DataFrame(result,columns=[i[0]for i in cursor.description])
    st.dataframe(df)
