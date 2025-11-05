#pandas
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address, how='left', on='personId')[['firstName', 'lastName', 'city', 'state']]
