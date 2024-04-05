# Modifiziere den Code, um eine exakte Übereinstimmung der Produkt-Namen zu erfordern

# Ergebnisse initialisieren
exact_match_results = {}

# Durchlaufe jede Zeile in der Datei
for index, row in data.iterrows():
    business_group = row['businessGroupName']
    product_name = row['productName']
    resource_name = row['resourceName']  # Verwende resourceName statt tenantId
    
    # Wenn die Geschäftsgruppe noch nicht in den Ergebnissen ist, initialisiere sie mit Produktnamen und resourceNames
    if business_group not in exact_match_results:
        exact_match_results[business_group] = {
            'Storage Fast Platinum Basic': False, 
            'Managed OS Basic': False,
            'resourceNames': set()  # Verwende ein Set, um Duplikate zu vermeiden
        }
    
    # Füge den resourceName zur Geschäftsgruppe hinzu
    exact_match_results[business_group]['resourceNames'].add(resource_name)
    
    # Prüfe auf exakte Übereinstimmung mit den gesuchten Produktnamen
    if product_name in products_to_check:
        exact_match_results[business_group][product_name] = True

# Vorbereitung der korrigierten Daten für die Excel-Datei unter Berücksichtigung der exakten Übereinstimmung
exact_match_data_for_excel = []
for business_group, details in exact_match_results.items():
    for resource_name in details['resourceNames']:
        exact_match_data_for_excel.append({
            'Business Group Name': business_group,
            'Resource Name': resource_name,
            'Storage Fast Platinum Basic': details['Storage Fast Platinum Basic'],
            'Managed OS Basic': details['Managed OS Basic']
        })

# Umwandeln in DataFrame und speichere es, wenn es Daten gibt
if exact_match_data_for_excel:
    exact_match_df_to_save = pd.DataFrame(exact_match_data_for_excel)
    exact_match_output_file_path = '/mnt/data/exakte_match_ergebnisse.xlsx'
    # Speichere das DataFrame in einer Excel-Datei
    exact_match_df_to_save.to_excel(exact_match_output_file_path, index=False)
    exact_match_output_file_path  # Rückgabe des Pfades zur exakten Match-Datei
else:
    exact_match_output_file_path = None  # Keine Daten gefunden, die den exakten Match-Kriterien entsprechen

exact_match_output_file_path
