import os
import csv


filePath = os.path.realpath(__file__)
directory = os.path.dirname(filePath)
dataset = []
with open(f"{directory}\\housing_sf_other_w_census.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dataset.append(row)

muni_ids = set()

# pop_sum = {}
percent_sf = {}
hh_sum = {}
# male_sum = {}
# female_sum = {}
# pop_u18_sum = {}
# pop_18_64_sum = {}
# pop_65o_sum = {}
# nhwhi_sum = {}
# nhaa_sum = {}
# nhna_sum = {}
# nhas_sum = {}
# nhpi_sum = {}
# nhoth_sum = {}
# nhmlt_sum = {}
# lat_sum = {}

# incu10_sum = {}
# inc1015_sum = {}
# inc1520_sum = {}
# inc2025_sum = {}
# inc2530_sum = {}
# inc3035_sum = {}
# inc3540_sum = {}
# inc4045_sum = {}
# inc4550_sum = {}
# inc5060_sum = {}
# inc6075_sum = {}
# i7599_sum = {}
# i100125_sum = {}
# i125150_sum = {}
# i150200_sum = {}
# in200o_sum = {}

fhh_sum = {}
fhh2_sum = {}
fhh3_sum = {}
fhh4_sum = {}
fhh5_sum = {}
fhh6_sum = {}
fhh7o_sum = {}
nfhh_sum = {}
nfhh1_sum = {}
nfhh2_sum = {}
nfhh3_sum = {}
nfhh4_sum = {}
nfhh5_sum = {}
nfhh6_sum = {}
nfhh7o_sum = {}


# attribute_sums = [percent_sf, pop_sum, male_sum, female_sum, pop_u18_sum, pop_18_64_sum, pop_65o_sum, nhwhi_sum, nhaa_sum, nhna_sum, nhas_sum, nhpi_sum, nhoth_sum, nhmlt_sum, lat_sum, hh_sum]
# attributes = ["%_single_family", "pop", "male", "female", "pop_u18", "pop_18_64", "pop_65o", "nhwhi", "nhaa", "nhna", "nhas", "nhpi", "nhoth", "nhmlt", "lat", "hh"]

# attribute_sums = [percent_sf,
#                     hh_sum,
#                     incu10_sum,
#                     inc1015_sum,
#                     inc1520_sum,
#                     inc2025_sum,
#                     inc2530_sum,
#                     inc3035_sum,
#                     inc3540_sum,
#                     inc4045_sum,
#                     inc4550_sum,
#                     inc5060_sum,
#                     inc6075_sum,
#                     i7599_sum,
#                     i100125_sum,
#                     i125150_sum,
#                     i150200_sum,
#                     in200o_sum
#                     ]
# attributes = ["%_single_family", "hh",
#                 "incu10",
#                 "inc1015",
#                 "inc1520",
#                 "inc2025",
#                 "inc2530",
#                 "inc3035",
#                 "inc3540",
#                 "inc4045",
#                 "inc4550",
#                 "inc5060",
#                 "inc6075",
#                 "i7599",
#                 "i100125",
#                 "i125150",
#                 "i150200",
#                 "in200o"
#                 ]

attribute_sums = [percent_sf,
                    hh_sum,
                    fhh_sum,
                    fhh2_sum,
                    fhh3_sum,
                    fhh4_sum,
                    fhh5_sum,
                    fhh6_sum,
                    fhh7o_sum,
                    nfhh_sum,
                    nfhh1_sum,
                    nfhh2_sum,
                    nfhh3_sum,
                    nfhh4_sum,
                    nfhh5_sum,
                    nfhh6_sum,
                    nfhh7o_sum
                    ]
attributes = ["%_single_family",
                "hh",
                "fhh",
                "fhh2",
                "fhh3",
                "fhh4",
                "fhh5",
                "fhh6",
                "fhh7o",
                "nfhh",
                "nfhh1",
                "nfhh2",
                "nfhh3",
                "nfhh4",
                "nfhh5",
                "nfhh6",
                "nfhh7o"
                ]

for data in dataset:
    if float(data["%_single_family"]) == 0 or float(data["%_single_family"]) == 100:
        for a_sum, att in zip(attribute_sums, attributes):
            muni_id = data["muni_id"]
            muni_ids.add(muni_id)
            if muni_id not in a_sum.keys():
                a_sum[muni_id] = 0
            if att in ["%_single_family"]:
                a_sum[muni_id] = float(data[att])
            else:
                a_sum[muni_id] += float(data[att])

with open(f"{directory}\\housing_sf_other_w_census_agg_hh.csv", 'w', newline='', encoding="utf8") as outputFile:
    dataWriter = csv.DictWriter(outputFile, fieldnames=["sum_muni_id", *["sum_" + att for att in attributes]])
    dataWriter.writeheader()
    for m_id in muni_ids:
        row = {"sum_muni_id": m_id}
        for a_sum, att in zip(attribute_sums, attributes):
            row["sum_" + att] = a_sum[m_id]
        dataWriter.writerow(row)