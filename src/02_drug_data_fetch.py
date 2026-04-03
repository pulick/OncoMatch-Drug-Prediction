import pandas as pd
import pubchempy as pcp
import time
import re

#used to fetech drug data beased on drug_id and drug_name

enriched_tests=pd.read_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/drug_response_enriched.csv")


unique_drugs = enriched_tests[['DRUG_ID', 'DRUG_NAME']].drop_duplicates()

def get_smiles(name):
    try:
        # Search for the drug by name
        results = pcp.get_compounds(name, 'name')
        if results:
            return results[0].canonical_smiles
    except:
        return None
    return None

print("Fetching SMILES strings... this may take a few minutes.")

# 2. Map the names to SMILES
unique_drugs['SMILES'] = unique_drugs['DRUG_NAME'].apply(get_smiles)


unique_drugs.to_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/drug_smiles_map.csv", index=False)

print(f"Done! Found {unique_drugs['SMILES'].notnull().sum()} SMILES for your drugs.")

def get_smiles_robust(name):
    # Clean the name: Remove parentheses and extra spaces
    clean_name = re.sub(r'\(.*\)', '', str(name)).strip()
    
    try:
        # 1. Try searching the cleaned name
        results = pcp.get_compounds(clean_name, 'name')
        if results:
            return results[0].isomeric_smiles
        
        # 2. If it fails, try the original name just in case
        results = pcp.get_compounds(name, 'name')
        if results:
            return results[0].isomeric_smiles
            
        # Wait 0.5 seconds to avoid being blocked by PubChem
        time.sleep(0.5) 
    except Exception as e:
        print(f"Error searching {name}: {e}")
        return None
    return None

print("Starting robust SMILES fetch...")
unique_drugs['SMILES'] = unique_drugs['DRUG_NAME'].apply(get_smiles_robust)