library(TCGAbiolinks)
library(SummarizedExperiment)

# 1. The Query used to download data using TCGAbiolonks
query <- GDCquery(
    project = "TCGA-BRCA", 
    data.category = "Transcriptome Profiling",
    data.type = "Gene Expression Quantification",
    workflow.type = "STAR - Counts"
)

query$results[[1]] <- query$results[[1]][1:50,]

GDCdownload(query, directory = "data/raw")

data <- GDCprepare(query, directory = "data/raw")

# Extract the numeric matrix (the counts)
exp_matrix <- assay(data) 

# Save as a CSV for Python
write.csv(exp_matrix, "data/raw/tcga_brca_counts.csv", row.names = TRUE)

print("Success! CSV created without re-downloading.")
# 1. Extract the clinical metadata
clinical_info <- colData(data)

# 2. Convert to a standard data frame
clinical_df <- as.data.frame(clinical_info)


clinical_flat <- clinical_df[, sapply(clinical_df, function(x) !is.list(x))]

# 4. Save the flattened version
write.csv(clinical_flat, "data/raw/tcga_brca_clinical.csv", row.names = TRUE)

print("Clinical data successfully flattened and exported!")