import pandas as pd
import numpy as np
# master_data = pd.read_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/drug_response_enriched.csv")
# smiles_map = pd.read_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/drug_smiles_map.csv")

# final_training_set = pd.merge(master_data, smiles_map[['DRUG_NAME', 'SMILES']], on='DRUG_NAME', how='inner')
# final_training_set = final_training_set.dropna(subset=['SMILES'])

# print(f"Final Dataset Size: {len(final_training_set)} rows.")
# print(f"Unique Drugs: {final_training_set['DRUG_NAME'].nunique()}")

# print(final_training_set)

# final_training_set.to_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/final_training_set.csv", index=False)





import gc
gc.collect()
import psutil, os
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import os


# drug_df=pd.read_csv("C:/Users/abrup/Desktop/OncoMatch-Drug-Prediction/data/processed/final_training_set.csv")
# target_ids = set(drug_df['SANGER_MODEL_ID'].unique())
# print(f"Targeting {len(target_ids)} specific cell lines across {len(drug_df)} tests.")
# gene_chunks = pd.read_csv(
#     "data/processed/tpm_clean.csv", 
#     index_col=0, 
#     chunksize=2000
# )

# matched_gene_data = []

# for i, chunk in enumerate(gene_chunks):
#     # Only keep the columns (cell lines) that exist in our drug tests
#     valid_cols = [col for col in target_ids if col in chunk.columns]
    
#     # Filter the chunk immediately
#     filtered_chunk = chunk[valid_cols].astype(np.float32)
    
#     matched_gene_data.append(filtered_chunk)
    
#     if i % 5 == 0:
#         print(f"Processed {i * 2000} genes...")

# # 4. Combine the filtered pieces
# print("Combining matched biological features...")
# full_gene_df = pd.concat(matched_gene_data)
# del matched_gene_data # Clear memory

# # 5. Transpose (Safe now because we only have ~51 columns instead of 1000)
# print("Transposing matrix for AI alignment...")
# full_gene_df_T = full_gene_df.transpose()
# full_gene_df_T.index.name = 'SANGER_MODEL_ID'
# del full_gene_df

# # 6. Final Merge 
# print("Merging Chemistry and Biology...")
# # We use a right join to ensure we match the drug_df rows exactly
# final_matrix = pd.merge(drug_df, full_gene_df_T, on='SANGER_MODEL_ID', how='inner')

# # 7. Save to Parquet (The "Gold Standard" for fast loading)
# output_path = "data/processed/AI_ready_matrix.parquet"
# print(f"Saving to {output_path}...")
# final_matrix.to_parquet(output_path, index=False, engine='pyarrow')

# print(f"✅ SUCCESS! Final Matrix Shape: {final_matrix.shape}")
# print("You are now officially ready to train your Neural Network.")

