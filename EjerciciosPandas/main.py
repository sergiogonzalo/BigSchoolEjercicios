import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" 
# Nota: He cambiado a Titanic porque es el "Hola Mundo" perfecto para limpieza de datos. 
# Si prefieres uno de series temporales, dímelo, pero el Titanic es ideal para "pensar" en tipos de datos.
df = pd.read_csv(url)

print(df.info())
# Data columns (total 12 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   PassengerId  891 non-null    int64  
#  1   Survived     891 non-null    int64  
#  2   Pclass       891 non-null    int64  
#  3   Name         891 non-null    str    
#  4   Sex          891 non-null    str    
#  5   Age          714 non-null    float64
#  6   SibSp        891 non-null    int64  
#  7   Parch        891 non-null    int64  
#  8   Ticket       891 non-null    str    
#  9   Fare         891 non-null    float64
#  10  Cabin        204 non-null    str    
#  11  Embarked     889 non-null    str    

print("--------Comprobando valores nulos por columna--------\n")
# 1. Limpieza rápida y profesional
print("Nulos por columna: \n", df.isnull().sum())

# num_null_PassengerId = df['PassengerId'].isnull().sum()
# print(f"PassengerId tiene {num_null_PassengerId} valores nulos.")

# num_null_Survived = df['Survived'].isnull().sum()
# num_null_Pclass = df['Pclass'].isnull().sum()
# num_null_Name = df['Name'].isnull().sum()
# num_null_Sex = df['Sex'].isnull().sum()
# num_null_Age = df['Age'].isnull().sum()
# num_null_SibSp = df['SibSp'].isnull().sum()
# num_null_Parch = df['Parch'].isnull().sum()
# num_null_Ticket = df['Ticket'].isnull().sum()
# num_null_Fare = df['Fare'].isnull().sum()

# num_null_Cabin = df['Cabin'].isnull().sum()
# print(f"Cabin tiene {num_null_Cabin} registros nulos") #687

# num_null_Embarked = df['Embarked'].isnull().sum()
# print(f"Embarked tiene {num_null_Embarked} registros nulos") #2

print("\n------------------------------------------------------")
df.drop(columns=['Cabin'], inplace=True) # Elimina filas con valores nulos en la columna 'Cabin'
print("Cabin eliminada del DataFrame")
# df['Cabin'].dropna(inplace=True) # Elimina filas con valores nulos en la columna 'Cabin'

df['Age'] = df['Age'].fillna(df['Age'].median())
print("Valores nulos de Age rellenados con la mediana de la columna")

df_older_than_18 = df[(df['Age'] > 18) & (df['Pclass'] == 1)] # Filtra pasajeros mayores de 18 años y de primera clase
print(f"Hay {len(df_older_than_18)} pasajeros mayores de 18 años y de primera clase")

print(f"La tarifa media es: {df['Fare'].mean()}")
print(f"La tasa de supervivencia agrupado por genero y clase es :")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean() * 100)
reporte = df.groupby(['Sex', 'Pclass'])['Survived'].mean() * 100
# 4. Exportación a JSON (¡No te olvides de esto!)
reporte.to_json("analisis_supervivencia.json")

df['IsAlone'] = (df['SibSp'] == 0) & (df['Parch'] == 0)
print("Columna 'IsAlone' creada para indicar si el pasajero estaba solo o no.")

df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.')
print("Columna 'Title' creada extrayendo el título del nombre del pasajero.")

# Realización de Capping o Winsorizing

print(df[df['Fare'] > 95.0 ].head())# Muestra los registros con tarifas superiores a 95.0 antes de aplicar el capping
df['Fare'] = df['Fare'].apply(lambda x: 95 if x > 95 else x)

print(df[df['Fare'] > 90 ]) # Muestra los registros con tarifas superiores a 95.0 antes de aplicar el capping

df['Sex_Short'] = df['Sex'].apply(lambda x: 'M' if x == 'male' else 'F')

print(df[df['Sex_Short'] == 'M'].head())

df['Age_Group'] = df['Age'].apply(lambda x: 'Child' if x < 18 else ( 'Adult' if 18 <=x < 60 else 'Senior'))


print(df['Age_Group'].value_counts())