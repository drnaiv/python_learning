import pandas as pd
df = pd.read_csv(r"D:\Data Sciences\Project\UMP Indonesia\UMP Indonesia 2022vs2023.csv", header = 0, delimiter = ';')

def calculate_ump(df, province_name):
    province_data = df[df['Province'].str.contains(province_name)]

    ump = int(province_data['Current Price'].iloc[0])
    tahun = 2023

    while ump < 10000000:
        tahun += 1
        ump += round(ump*0.07)
    return [province_name, tahun, ump]
    # return f"{province_name}, UMP menyentuh Rp 10.000.000 pada tahun {tahun} = {ump}"

provinces = df['Province'].tolist()
results = [calculate_ump(df, province) for province in provinces]
for result in results:
    print(result)

# calculate_ump(df, 'Jawa Tengah')
# calculate_ump(df, 'Jawa Barat')
# Creating a DataFrame
result_df = pd.DataFrame(results, columns=['Province', 'tahun', 'ump'])

# Writing the DataFrame to a CSV file
result_df.to_csv(r"D:\Data Sciences\Project\UMP Indonesia\UMP_10JT.csv", index=False, sep=';')