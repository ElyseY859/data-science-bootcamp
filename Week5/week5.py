import pandas as pd
#1050
def actor_director_cooperation(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    result = result[result['count'] >= 3]  
    return result[['actor_id', 'director_id']]

#1667
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    users = users.sort_values('user_id')
    return users

#175
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, on='personId', how='left')
    return result[['firstName', 'lastName', 'city', 'state']]

#176
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    second_highest = unique_salaries.iloc[1] 
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})

#1327
def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    feb_orders = orders[
        (orders['order_date'].dt.year == 2020) & 
        (orders['order_date'].dt.month == 2)
    ]
    product_units = feb_orders.groupby('product_id')['unit'].sum().reset_index()
    product_units = product_units[product_units['unit'] >= 100]
    result = products.merge(product_units, on='product_id')
    return result[['product_name', 'unit']]

#1378
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = employees.merge(employee_uni, on='id', how='left')
    return result[['unique_id', 'name']]

#50
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id', 'first_date']
    first_login['next_day'] = first_login['first_date'] + pd.Timedelta(days=1)
    activity_set = set(zip(activity['player_id'], activity['event_date']))
    first_login['logged_next_day'] = first_login.apply(
        lambda row: (row['player_id'], row['next_day']) in activity_set, 
        axis=1
    )
    fraction = round(first_login['logged_next_day'].sum() / len(first_login), 2)
    return pd.DataFrame({'fraction': [fraction]})

#1075
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, on='employee_id')
    result = merged.groupby('project_id')['experience_years'].mean().reset_index()
    result.columns = ['project_id', 'average_years']
    result['average_years'] = result['average_years'].round(2)
    return result

#185
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    merged['rank'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    result = merged[merged['rank'] <= 3]
    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result
