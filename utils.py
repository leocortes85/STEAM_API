import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import ast
import os


def load_json(json_path):
    """
    Loads a JSON file and returns a DataFrame.

    Parameters:
    - json_path: Path of the JSON file to load.

    Returns:
    - DataFrame loaded from JSON file.
    """
    # read each line in json file
    rows = []
    with open(json_path, encoding='utf-8') as f:
        for line in f.readlines():
            rows.append(ast.literal_eval(line))

    
    df = pd.DataFrame(rows)
    
    return df


def save_to_csv(dfs, names):

    """
    Saves a DataFrame to a CSV file in a specific directory.
        Parameters:
        - df: DataFrame to save.
        - file_name: Name of the CSV file.
    """
    for df, name in zip(dfs, names):
        archivo = f'data/csv/{name}.csv'
        df.to_csv(archivo, index=False, encoding='utf-8')
        print(f"DataFrame '{name}' saved as '{archivo}'")


def save_to_pq(dfs, names):

    """
    Saves a DataFrame to a parquet file in a specific directory.
        Parameters:
        - df: DataFrame to save.
        - file_name: Name of the parquet file.
    """
    for df, name in zip(dfs, names):
        archivo = f'data/{name}.parquet'
        pq.write_table(pa.Table.from_pandas(df), archivo)
        print(f"DataFrame '{name}' save as '{archivo}'")


def data_summ(df):
    '''
    This function provides detailed information about the dtype and null values present in a dataframe
    '''

    info_dict = {"Column": [], "Data_type": [], "No_miss_Qty": [], "%Missing": [], "Missing_Qty": []}
    

    for column in df.columns:
        
        info_dict["Column"].append(column)
        info_dict["Data_type"].append(df[column].apply(type).unique())
        info_dict["No_miss_Qty"].append(df[column].count())
        info_dict["%Missing"].append(round(df[column].isnull().sum() * 100 / len(df), 2))
        info_dict['Missing_Qty'].append(df[column].isnull().sum())

    df_info = pd.DataFrame(info_dict)
    
    print("\nTotal rows: ", len(df))
    print("\nTotal full null rows: ", df.isna().all(axis=1).sum())
    
    
    return df_info


def duplicates(df, column):
    '''
    Checks and displays duplicate rows in a DataFrame based on a specific column.

    This function takes as input a DataFrame and the name of a specific column.
    Then, identify duplicate rows based on the content of the specified column,
    filters and sorts them for easier comparison.

    Parameters:
        df (pandas.DataFrame): The DataFrame to search for duplicate rows.
        column (str): The name of the column based on which to check for duplicates.

    Returns:
        pandas.DataFrame or str: A DataFrame containing the filtered and sorted duplicate rows,
        lists for inspection and comparison, or the message "No Duplicates" if no duplicates are found.
    '''
    # Duplicate rows are filtered out
    duplicated_rows = df[df.duplicated(subset=column, keep=False)]
    if duplicated_rows.empty:
        return "There are no duplicates"
    
    # sort duplicate rows to compare with each other
    duplicated_rows_sorted = duplicated_rows.sort_values(by=column)
    return duplicated_rows_sorted


def drop_duplicates(df, column):
    '''
    This function counts the null values in each row to organize the dataframe in order of null values, 
    in order to eliminate duplicate records that have the same value 
    without affecting the row that has the most valid records.
    '''

    # temporary column 
    df['temp_index'] = range(len(df))

    # Count null values in each row
    df['num_null'] = df.isnull().sum(axis=1)

    # Sort by the specified column and the number of nulls
    df = df.sort_values(by=[column, 'num_null'])

    # Drop duplicates, keep the first occurrence
    df = df.drop_duplicates(subset=column, keep='first')

    # Sort again by the temporary column and remove it
    df = df.sort_values(by='temp_index').drop(['temp_index', 'num_null'], axis=1)

    # Reset the index
    df = df.reset_index(drop=True)

    return df

def replace_all_nulls(df):
    '''
    Recieves a df as parameter and fill all the null values per column depending on their dType
    '''

    for column in df.columns:
        mask = df[column].notnull()
        dtype = df[column][mask].apply(type).unique()

        if dtype[0] == str: 
            df[column] = df[column].fillna('No data')
        elif dtype[0] == float:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
        elif dtype[0] == list:
            df[column] = df[column].fillna('No data')


    



