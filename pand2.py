# import pandas as pd
# # dictionary with at least 5 keys and 5 values and some nan values
# import numpy as np
# # Create a dictionary with names, ages, and cities
# dictionary = {
#     "Names": ["Justas", "Jonas", "Mantas", "Tomas", "Andrius"],
#     "Ages": [20, 21, 20, np.nan, 24],
#     "Cities": ["Vilnius", "Kaunas", "Klaipeda", np.nan, "Šiauliai"],
#     "Country": ["Lithuania", "Lithuania", "Latvia", "Latvia", "Estonia"],
#     "Hobbies": ["Reading", "Gaming", "Sports", "Traveling", "Cooking"],
#     "Scores": [85, 90, 20, 88, np.nan]
# }

# def create_dataframe(data):
#     """Create a DataFrame from the provided dictionary."""
#     df = pd.DataFrame(data)
#     return df
# df = create_dataframe(dictionary)

# # lists of lists
# # lists_of_lists = [
# #     ["Justas", 20, "Vilnius"],
# #     ["Jonas", 21, "Kaunas"],
# #     ["Mantas", 22, "Klaipeda"]
# # ]
# # print(create_dataframe(lists_of_lists))

# # print(df.head(2))  # Display the first two rows of the DataFrame

# # print(df.shape)

# # df.info()  # Display information about the DataFrame, including data types and non-null counts
# # print(df.describe(include="all"))  # Display summary statistics for numerical columns

# # print(df.isna().sum())  # Check for NaN values in the DataFrame
# # print(df.nunique())
# # names = df[["Names", "Ages", "Cities"]] # Convert specific columns to a list of lists
# # print(names)

# # print(df["Names"].unique())  # Get unique names from the "Names" column
# # print(df.values)
# # print(df['Names'].value_counts())

# # kaip ir su series, su dataframe galima naudoti loc ir iloc
# # print(df.loc[0])  # Get the first row of the DataFrame
# # print(df[df['Scores'] > 80])  # Filter rows where 'Scores' are greater than 80

# # print(pd.isnull(df))
# # df["Scores"].fillna(50, inplace=True)  # Fill NaN values with 50
# # print(df)
# # df.dropna(axis=1,thresh=5,inplace=True)  # Drop columns with NaN values
# # print(df)

# # df['Country'] = ["Latvia", "Lithuania", "Estonia", "Finland", "Sweden"]  # Add a new column
# # print(df)

# # df.drop(columns=["Country"], inplace=True)  # Drop the 'Country' column
# # df.drop(index=[0, 1], inplace=True)  # Drop the first two rows
# # print(df)
# # df.replace({"Ages": {20: 21, 21: 22}}, inplace=True)  # Replace values in the 'Ages' column
# # print(df)

# def group_by_country(df):
#     grouped_df = df.groupby("Country")  # Group by 'Country' and calculate the mean of numerical columns
#     print(grouped_df)
#     for country, group in grouped_df:
#         print(f"Country: {country}")
#         print(group['Scores'].mean())

# # group_by_country(df)

# # agg
# def aggregate_data(df):
#     """Aggregate data by 'Country' and calculate mean of 'Scores'."""
#     aggregated_df = df.groupby("Country").agg({"Scores": ["mean", "sum"], "Ages": "mean"})
#     print(aggregated_df)
#     return aggregated_df
# # print(aggregate_data(df))

# # df.sort_values(by="Scores", ascending=False, inplace=True)  # Sort DataFrame by 'Scores' in descending order
# # print(df)columns={"Names": "Name", "Ages": "Age"})  # Rename columns
# changed_df.drop(columns=["Cities"], inplace=True)  # Drop the 'Cities' column

# concacanated = pd.concat([df, changed_df], axis=0, ignore_index=True)  # Concatenate DataFrames along rows
# print(concacanated)
# # merge
# merged = pd.merge(df, changed_df, on="Hobbies", how="inner")  # Merge DataFrames on 'Name' column
# print(merged)
# # df.sort_index(inplace=True)  # Sort the DataFrame by index
# # print(df)  # Display the DataFrame after sorting by index
# # df.reset_index(inplace=True, drop=True)  # Reset the index of the DataFrame
# # print(df)  # Display the DataFrame after sorting and resetting the index

# changed_df = df.rename(

# import pandas as pd
# df = pd.read_csv('train.csv', index_col=0)  # Read a CSV file into a DataFrame
# print(df)
# print(df.describe())
# df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill NaN values in 'Age' column with the mean
# print(df.describe())
# df.to_csv('train_filled.csv')  # Save the modified DataFrame to a new CSV file