

#All genes


time bash multiAffinity -a full -o output_m_ppi_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv,input/PPI_layers.csv,input/pathways_layers.csv ; time bash multiAffinity -a full -o output_ppi_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/PPI_layers.csv,input/pathways_layers.csv ; time bash multiAffinity -a full -o output_m_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csvinput/pathways_layers.csv ; time bash multiAffinity -a full -o output_m_ppi -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv,input/PPI_layers.csv ; time bash multiAffinity -a full -o output_m -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv ; time bash multiAffinity -a full -o output_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/pathways_layers.csv ; time bash multiAffinity -a full -o output_ppi -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/PPI_layers.csv ; time bash multiAffinity -o outputcomm_m_ppi_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv,input/PPI_layers.csv,input/pathways_layers.csv ; time bash multiAffinity -o outputcomm_ppi_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/PPI_layers.csv,input/pathways_layers.csv ; time bash multiAffinity -o outputcomm_m_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csvinput/pathways_layers.csv ; time bash multiAffinity -o outputcomm_m_ppi -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv,input/PPI_layers.csv ; time bash multiAffinity -o outputcomm_m -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/metabs_layers.csv ; time bash multiAffinity -o outputcomm_paths -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/pathways_layers.csv ; time bash multiAffinity -o outputcomm_ppi -c input/GSE81928_GeneLevel_Raw_data.csv,input/GSE89775_GeneLevel_Raw_data.csv,input/GSE104766_GeneLevel_Raw_data.csv,input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE81928_filtered_metadata.csv,input/GSE89775_filtered_metadata.csv,input/GSE104766_filtered_metadata.csv,input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/PPI_layers.csv



time bash multiAffinity -a full -o output_base -c input/GSE133039_GeneLevel_Raw_data.csv,input/GSE151347_GeneLevel_Raw_data.csv -m input/GSE133039_filtered_metadata.csv,input/GSE151347_filtered_metadata.csv -n input/PPI_layers.csv