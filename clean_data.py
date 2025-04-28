import pandas as pd
import numpy as np

def data_cleaning(dataframe, numeric_columns_list, categorical_columns_list):
    dataframe_unclean = dataframe.copy() # Create a copy of the dataframe to avoid modifying the original
    columns_list = dataframe.columns.tolist() #convert the columns to a list
    dataframe = dataframe.drop_duplicates() #remove duplicates
    
    #remove outliers
    for column in numeric_columns_list:
        Q1 = dataframe[column].quantile(0.25)  
        Q3 = dataframe[column].quantile(0.75)  
        IQR = Q3 - Q1  
        outliers = (dataframe[column] < (Q1 - 1.5*IQR)) | (dataframe[column] > (Q3 + 1.5*IQR)) 
        dataframe = dataframe[~outliers]

    #remove missing values
    for column in columns_list:
        if column in numeric_columns_list:
            dataframe[column].fillna(dataframe[column].mean(), inplace=True)
        elif column in categorical_columns_list:
            #dataframe[column].fillna(dataframe[column].mode()[0], inplace=True) # This replaces NaN with the mode (most frequent value) of the column.

            """ 
            To replace NaN values in a categorical column according to the frequency distribution (instead of just the mode), 
            This ensures that missing values are filled in a way that preserves the original distribution of the data.
            This method replaces missing values in a categorical column while strictly preserving the original frequency 
            distribution across all categories (no randomness). It works for any number of categories
            """
            # Get frequency distribution of non-null values
            #column_distribution = dataframe[column].value_counts(normalize=True)  # Probabilities
            
            frequency_dist = dataframe[column].value_counts(normalize=True) # Probabilities
            missing_count = dataframe[column].isna().sum()
    
            # Step 2: Calculate exact imputation counts
            impute_counts = (frequency_dist * missing_count).round().astype(int)
            while impute_counts.sum() != missing_count:
                diff = missing_count - impute_counts.sum()
                impute_counts[impute_counts.idxmax()] += diff
    
            # Step 3: Replace missing values
            missing_indices = dataframe[dataframe[column].isna()].index.tolist()
            replacements = []
            for category, count in impute_counts.items():
                replacements.extend([category] * count)
            dataframe.loc[missing_indices, column] = replacements
            
            """ 
            To replace NaN values in a categorical column according to the frequency distribution (instead of just the mode), 
            use random sampling from the existing categories. 
            This ensures that missing values are filled in a way that preserves the original distribution of the data.
            """
            """
            dataframe[column] = dataframe[column].fillna(pd.Series(np.random.choice(
                column_distribution.index,
                size=len(dataframe),
                p=column_distribution.values)))
        """
        else:
            continue
        print("Data cleaning completed.")
        print(f"Dataframe shape after cleaning: {dataframe.shape}\n Dataframe shape before cleaning: {dataframe_unclean.shape}")
        print(f"Dataframe info after cleaning: {dataframe.info()}\n Dataframe info before cleaning: {dataframe_unclean.info()}")
        print(f"Dataframe description after cleaning: {dataframe.describe()}\n Dataframe description before cleaning: {dataframe_unclean.describe()}")
    return dataframe