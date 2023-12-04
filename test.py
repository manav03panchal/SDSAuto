import pandas as pd
import requests


def get_cas_number(chemical_name):
    url = f"https://commonchemistry.cas.org/api/search?q={chemical_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['count'] > 0:
            # Returns the first CAS number found
            return data['results'][0]['rn']
    return None


# List of chemicals to fetch CAS numbers for
chemicals = ['5-hydroxyindole-3-acetic acid', 'Kuromanin chloride', 'Myrtillin chloride', 'Oenin chloride', 'Callistephin chloride', 'Peonidin-3-O-glucoside chloride', 'Adenosine 5′-triphosphate disodium salt hydrate', 'Oxaloacetic Axid', 'DL-norepinephrine hydrochloride', 'enterolactone glucuronide', 'enterolactone sulfate', "daidzein 4'-sulfate", 'genicitin disulfate', '4-methylumbelliferyl glucuronide', '4-methylumbelliferyl sulfate', 'Callistephin chloride', 'N-acetyl-S-allyl-L-cysteine', 'acetylcholine iodide', 'beta-carotene', 'ferulic acid 4-glucuronide', 'ferulic acid 4-sulfate', 'dihydroisoferulic', 'dihydroisoferulic 3-sulfate', '2-Amino-1-methyl-6-phenylimidazo[4,5-b]pyridine N-β-D-Glucuronide Sodium Salt', 'trans-resveratrol', '2-aminophenyl-b-glucuronide', 'rac-Hesperetin 7-O-Sulfate Sodium Salt', 'p-salicylic acid 4-glucuronide potassium', 'apigenin', 'docosapentaeonic acid', 'Phe-Phe', 'linolenic acid', 'palmitin', 'linoleyl-L-carnitine', 'pyridoxamine', 'cholesterol', 'cis-aconitic acid', 'Ne-acetyl-lysine', 'sitagliptin', 'alprazolam', 'repaglinide', 'candesartan', 'glipizide', '5-hydroxymethyl-2-furancarboxylic acid', '2,5-furandicarboxylic acid', '1-methylxanthine', '5-acetylamino-6-amino-3-methyluracil', 'glycodeoxycholic acid 3-glucuronide',
             'taurolithocholic acid 3-sulfate', 'p-cresol sulfate', 'N-methyl-tyramine', 'N8-acetylspermidine', 'N-acetylornithine', 'oleic acid', 'linoleic acid', '7-dehydrocholesterol', 'adenosine 5′-diphosphate', 'melatonin', 'indoxyl sulfate', 'cyclo', 'Retinoic acid', 'Thiamine pyrophosphate', 'distearoyl-glycerophosphocholine', 'retinyl acetate', 'estrone 3-sulfate', '3-methoxytyramine', 'cyclo', 'solanine', 'indolepyruvic acid', 'phosphoethanolamine', 'sebacoyl-carnitine', 'CER', 'acetoacetic acid', '1,2-Dipalmitoyl-sn-glycerol', '3-Hydroxy-3-methylglutaric acid', 'N-alpha-acetyl-lysine', 'Phosphoenolpyruvate', 'dehydroascorbic', 'C18:1 anandamide', 'sphinganine', 'Phosphocreatine', 'arachidic acid', 'nervonic acid', 'D-glucosamine 6-phosphate', 'UDP-glucose disodium salt', 'dimethyl phosphate', 'dimethyl dithiophosphate', "Adenosine 3'':5''-cyclic monophosphate", "Uridine 5'-monophosphate disodium salt", "Uridine 5'-diphosphate disodium", "Guanosine 5'-diphosphate", "Uridine 5'-triphosphate", 'D-2-phosphoglyceric acid', 'epinephrine 4-sulfate', 'ascorbic acid 2-sulfate', 'Glucobrassicanapin Potassium salt', 'Glycoursodeoxycholic acid', 'Glucolepidiin potassium salt', 'Glucoberteroin potassium salt', 'Glucoraphanin potassium salt', 'N-acetyl-L-tyrosine, ethyl ester']
data = {'Name of Chemical': chemicals, 'CAS #': [''] * len(chemicals)}
df = pd.DataFrame(data)

# Iterate through the list and update CAS numbers
for index, row in df.iterrows():
    chemical_name = row['Name of Chemical']
    cas_number = get_cas_number(chemical_name)
    df.at[index, 'CAS #'] = str(cas_number) if cas_number else None

# Save the DataFrame to a CSV file
df.to_csv('chemicals_with_cas.csv', index=False)

print("DataFrame saved to 'chemicals_with_cas.csv'")
