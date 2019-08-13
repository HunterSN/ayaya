# ayaya
[c_ct compounds_compound-targets]
  tcmsp:
      single herb;
      single herburl;
      a group of herbs;
      herbs' numble of tcmsp;
  symmap:
      single herb;
      a group of herbs;
  etcm:
      single herb;
      a group of herbs;
      single herburl;
[ct protein_name-gene_name]
  uniprot:
      single protein;
      a group of proteins;
[hebing]
  csvs-csv;
  csvs-txt;

- [x] c_ct.py tcmspzong 获取tcmsp草药的化合物名称（tcmspc.txt）、化合物靶点蛋白名称（tcmspct.txt），导入excel，建立化合物库和化合物_靶点库
- [x] c_ct.py symmapzong 获取symmap草药的化合物名称、化合物pubmed号、cas号（*** symmap.csv）化合物靶点基因名称（symmapct.txt），导入excel，建立化合物库和化合物_靶点库
- [x] hebing.py csv_txt csv_csv 合并*** symmap.csv导出symmapc.txt symmapc.csv，导入excel
- [x] c_ct_1_1.py etcmzong 获取etcm草药的化合物名称、pubmed号、cas号（etcmc.txt）、化合物靶点基因名称（etcmct.txt），导入excel，建立化合物库和化合物_靶点库
- [x] ct.py uniprot 利用tcmsp蛋白质名称获取基因名（uniprotct.txt），导入excel，建立uniprot库
- [x] c_ct_1_1.py tcmspnumzong 获取tcmsp化合物全部mol号，导入excel
- [x] c_smiles tcmspsmilesnumzong 获取tcmsp化合物的pubmed号（tcmsppubmed.txt）及cas号（tcmspcass.txt、tcmspcasonly.txt）
- [x] c_smile.py pubchemwangyezong pubchemzong根据tcmsp、symmap、etcm化合物的pubmed号获取smile表达式、标准名称，导入excel，建立pubmednum库
- [x] shujuzhengli.py standardingprotein 将tcmsp中蛋白名与基因名对应（standardedprotein.txt），去除非人类蛋白
- [x] 将uniprot库中原始蛋白质名及基因名进行去重，并利用shujuzhengli.py qufangkuohao将蛋白质去处的符号与原蛋白质名称进行对应（matchtcmsp.txt）
      
