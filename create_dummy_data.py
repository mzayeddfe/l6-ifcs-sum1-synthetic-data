#import needed packages 

import pandas as pd 
import numpy as np 

#create a time identifier column 200 times
time_identifier = "Autumn Term"

# create a time period column 

time_period = "202425"

# define geographic levels
geographic_levels = ["National", "Regional", "Local Authority"]

#create country_code

country_code = "E92000001"

#create country name 

country_name = "England"

#create region_code

region_dict = {
    "E12000001": "North East",
    "E12000002": "North West",
    "E12000003": "Yorkshire and The Humber",
    "E12000004": "East Midlands",
    "E12000005": "West Midlands",
    "E12000006": "East of England",
    "E12000007": "London",
    "E12000008": "South East",
    "E12000009": "South West",
    "E13000001": "Inner London",
    "E13000002": "Outer London"
}


#create la_code
# Local Authority dictionary: code -> {"name": ..., "parent_geography_code": ...}
la_dict = {
    "E06000001": {"name": "Hartlepool", "parent_geography_code": "E12000001"},
    "E06000002": {"name": "Middlesbrough", "parent_geography_code": "E12000001"},
    "E06000003": {"name": "Redcar and Cleveland", "parent_geography_code": "E12000001"},
    "E06000004": {"name": "Stockton-on-Tees", "parent_geography_code": "E12000001"},
    "E06000005": {"name": "Darlington", "parent_geography_code": "E12000001"},
    "E06000006": {"name": "Halton", "parent_geography_code": "E12000002"},
    "E06000007": {"name": "Warrington", "parent_geography_code": "E12000002"},
    "E06000008": {"name": "Blackburn with Darwen", "parent_geography_code": "E12000002"},
    "E06000009": {"name": "Blackpool", "parent_geography_code": "E12000002"},
    "E06000010": {"name": "Kingston upon Hull, City of", "parent_geography_code": "E12000003"},
    "E06000011": {"name": "East Riding of Yorkshire", "parent_geography_code": "E12000003"},
    "E06000012": {"name": "North East Lincolnshire", "parent_geography_code": "E12000003"},
    "E06000013": {"name": "North Lincolnshire", "parent_geography_code": "E12000003"},
    "E06000014": {"name": "York", "parent_geography_code": "E12000003"},
    "E06000015": {"name": "Derby", "parent_geography_code": "E12000004"},
    "E06000016": {"name": "Leicester", "parent_geography_code": "E12000004"},
    "E06000017": {"name": "Rutland", "parent_geography_code": "E12000004"},
    "E06000018": {"name": "Nottingham", "parent_geography_code": "E12000004"},
    "E06000019": {"name": "Herefordshire, County of", "parent_geography_code": "E12000005"},
    "E06000020": {"name": "Telford and Wrekin", "parent_geography_code": "E12000005"},
    "E06000021": {"name": "Stoke-on-Trent", "parent_geography_code": "E12000005"},
    "E06000022": {"name": "Bath and North East Somerset", "parent_geography_code": "E12000009"},
    "E06000023": {"name": "Bristol, City of", "parent_geography_code": "E12000009"},
    "E06000024": {"name": "North Somerset", "parent_geography_code": "E12000009"},
    "E06000025": {"name": "South Gloucestershire", "parent_geography_code": "E12000009"},
    "E06000026": {"name": "Plymouth", "parent_geography_code": "E12000009"},
    "E06000027": {"name": "Torbay", "parent_geography_code": "E12000009"},
    "E06000028": {"name": "Bournemouth", "parent_geography_code": "E12000009"},
    "E06000029": {"name": "Poole", "parent_geography_code": "E12000009"},
    "E06000030": {"name": "Swindon", "parent_geography_code": "E12000009"},
    "E06000031": {"name": "Peterborough", "parent_geography_code": "E12000006"},
    "E06000032": {"name": "Luton", "parent_geography_code": "E12000006"},
    "E06000033": {"name": "Southend-on-Sea", "parent_geography_code": "E12000006"},
    "E06000034": {"name": "Thurrock", "parent_geography_code": "E12000006"},
    "E06000035": {"name": "Medway", "parent_geography_code": "E12000008"},
    "E06000036": {"name": "Bracknell Forest", "parent_geography_code": "E12000008"},
    "E06000037": {"name": "West Berkshire", "parent_geography_code": "E12000008"},
    "E06000038": {"name": "Reading", "parent_geography_code": "E12000008"},
    "E06000039": {"name": "Slough", "parent_geography_code": "E12000008"},
    "E06000040": {"name": "Windsor and Maidenhead", "parent_geography_code": "E12000008"},
    "E06000041": {"name": "Wokingham", "parent_geography_code": "E12000008"},
    "E06000042": {"name": "Milton Keynes", "parent_geography_code": "E12000008"},
    "E06000043": {"name": "Brighton and Hove", "parent_geography_code": "E12000008"},
    "E06000044": {"name": "Portsmouth", "parent_geography_code": "E12000008"},
    "E06000045": {"name": "Southampton", "parent_geography_code": "E12000008"},
    "E06000046": {"name": "Isle of Wight", "parent_geography_code": "E12000008"},
    "E06000047": {"name": "County Durham", "parent_geography_code": "E12000001"},
    "E06000048": {"name": "Northumberland", "parent_geography_code": "E12000001"},
    "E06000049": {"name": "Cheshire East", "parent_geography_code": "E12000002"},
    "E06000050": {"name": "Cheshire West and Chester", "parent_geography_code": "E12000002"},
    "E06000051": {"name": "Shropshire", "parent_geography_code": "E12000005"},
    "E06000052": {"name": "Cornwall", "parent_geography_code": "E12000009"},
    "E06000053": {"name": "Isles of Scilly", "parent_geography_code": "E12000009"},
    "E06000054": {"name": "Wiltshire", "parent_geography_code": "E12000009"},
    "E06000055": {"name": "Bedford", "parent_geography_code": "E12000006"},
    "E06000056": {"name": "Central Bedfordshire", "parent_geography_code": "E12000006"},
    "E06000057": {"name": "Northumberland", "parent_geography_code": "E12000001"},
    "E06000058": {"name": "Bournemouth, Christchurch and Poole", "parent_geography_code": "E12000009"},
    "E06000059": {"name": "Dorset", "parent_geography_code": "E12000009"},
    "E06000060": {"name": "Buckinghamshire", "parent_geography_code": "E12000008"},
    "E06000061": {"name": "North Northamptonshire", "parent_geography_code": "E12000004"},
    "E06000062": {"name": "West Northamptonshire", "parent_geography_code": "E12000004"},
    "E06000063": {"name": "Cumberland", "parent_geography_code": "E12000002"},
    "E06000064": {"name": "Westmorland and Furness", "parent_geography_code": "E12000002"},
    "E06000065": {"name": "North Yorkshire", "parent_geography_code": "E12000003"},
    "E06000066": {"name": "Somerset", "parent_geography_code": "E12000009"},
    "E08000001": {"name": "Bolton", "parent_geography_code": "E12000002"},
    "E08000002": {"name": "Bury", "parent_geography_code": "E12000002"},
    "E08000003": {"name": "Manchester", "parent_geography_code": "E12000002"},
    "E08000004": {"name": "Oldham", "parent_geography_code": "E12000002"},
    "E08000005": {"name": "Rochdale", "parent_geography_code": "E12000002"},
    "E08000006": {"name": "Salford", "parent_geography_code": "E12000002"},
    "E08000007": {"name": "Stockport", "parent_geography_code": "E12000002"},
    "E08000008": {"name": "Tameside", "parent_geography_code": "E12000002"},
    "E08000009": {"name": "Trafford", "parent_geography_code": "E12000002"},
    "E08000010": {"name": "Wigan", "parent_geography_code": "E12000002"},
    "E08000011": {"name": "Knowsley", "parent_geography_code": "E12000002"},
    "E08000012": {"name": "Liverpool", "parent_geography_code": "E12000002"},
    "E08000013": {"name": "St. Helens", "parent_geography_code": "E12000002"},
    "E08000014": {"name": "Sefton", "parent_geography_code": "E12000002"},
    "E08000015": {"name": "Wirral", "parent_geography_code": "E12000002"},
    "E08000016": {"name": "Barnsley", "parent_geography_code": "E12000003"},
    "E08000017": {"name": "Doncaster", "parent_geography_code": "E12000003"},
    "E08000018": {"name": "Rotherham", "parent_geography_code": "E12000003"},
    "E08000019": {"name": "Sheffield", "parent_geography_code": "E12000003"},
    "E08000020": {"name": "Gateshead", "parent_geography_code": "E12000001"},
    "E08000021": {"name": "Newcastle upon Tyne", "parent_geography_code": "E12000001"},
    "E08000022": {"name": "North Tyneside", "parent_geography_code": "E12000001"},
    "E08000023": {"name": "South Tyneside", "parent_geography_code": "E12000001"},
    "E08000024": {"name": "Sunderland", "parent_geography_code": "E12000001"},
    "E08000025": {"name": "Birmingham", "parent_geography_code": "E12000005"},
    "E08000026": {"name": "Coventry", "parent_geography_code": "E12000005"},
    "E08000027": {"name": "Dudley", "parent_geography_code": "E12000005"},
    "E08000028": {"name": "Sandwell", "parent_geography_code": "E12000005"},
    "E08000029": {"name": "Solihull", "parent_geography_code": "E12000005"},
    "E08000030": {"name": "Walsall", "parent_geography_code": "E12000005"},
    "E08000031": {"name": "Wolverhampton", "parent_geography_code": "E12000005"},
    "E08000032": {"name": "Bradford", "parent_geography_code": "E12000003"},
    "E08000033": {"name": "Calderdale", "parent_geography_code": "E12000003"},
    "E08000034": {"name": "Kirklees", "parent_geography_code": "E12000003"},
    "E08000035": {"name": "Leeds", "parent_geography_code": "E12000003"},
    "E08000036": {"name": "Wakefield", "parent_geography_code": "E12000003"},
    "E08000037": {"name": "Gateshead", "parent_geography_code": "E12000001"},
    "E08000038": {"name": "Barnsley", "parent_geography_code": "E12000003"},
    "E08000039": {"name": "Sheffield", "parent_geography_code": "E12000003"},
    "E09000001": {"name": "City of London", "parent_geography_code": "E12000007"},
    "E09000002": {"name": "Barking and Dagenham", "parent_geography_code": "E12000007"},
    "E09000003": {"name": "Barnet", "parent_geography_code": "E12000007"},
    "E09000004": {"name": "Bexley", "parent_geography_code": "E12000007"},
    "E09000005": {"name": "Brent", "parent_geography_code": "E12000007"},
    "E09000006": {"name": "Bromley", "parent_geography_code": "E12000007"},
    "E09000007": {"name": "Camden", "parent_geography_code": "E12000007"},
    "E09000008": {"name": "Croydon", "parent_geography_code": "E12000007"},
    "E09000009": {"name": "Ealing", "parent_geography_code": "E12000007"},
    "E09000010": {"name": "Enfield", "parent_geography_code": "E12000007"},
    "E09000011": {"name": "Greenwich", "parent_geography_code": "E12000007"},
    "E09000012": {"name": "Hackney", "parent_geography_code": "E12000007"},
    "E09000013": {"name": "Hammersmith and Fulham", "parent_geography_code": "E12000007"},
    "E09000014": {"name": "Haringey", "parent_geography_code": "E12000007"},
    "E09000015": {"name": "Harrow", "parent_geography_code": "E12000007"},
    "E09000016": {"name": "Havering", "parent_geography_code": "E12000007"},
    "E09000017": {"name": "Hillingdon", "parent_geography_code": "E12000007"},
    "E09000018": {"name": "Hounslow", "parent_geography_code": "E12000007"},
    "E09000019": {"name": "Islington", "parent_geography_code": "E12000007"},
    "E09000020": {"name": "Kensington and Chelsea", "parent_geography_code": "E12000007"},
    "E09000021": {"name": "Kingston upon Thames", "parent_geography_code": "E12000007"},
    "E09000022": {"name": "Lambeth", "parent_geography_code": "E12000007"},
    "E09000023": {"name": "Lewisham", "parent_geography_code": "E12000007"},
    "E09000024": {"name": "Merton", "parent_geography_code": "E12000007"},
    "E09000025": {"name": "Newham", "parent_geography_code": "E12000007"},
    "E09000026": {"name": "Redbridge", "parent_geography_code": "E12000007"},
    "E09000027": {"name": "Richmond upon Thames", "parent_geography_code": "E12000007"},
    "E09000028": {"name": "Southwark", "parent_geography_code": "E12000007"},
    "E09000029": {"name": "Sutton", "parent_geography_code": "E12000007"},
    "E09000030": {"name": "Tower Hamlets", "parent_geography_code": "E12000007"},
    "E09000031": {"name": "Waltham Forest", "parent_geography_code": "E12000007"},
    "E09000032": {"name": "Wandsworth", "parent_geography_code": "E12000007"},
    "E09000033": {"name": "Westminster", "parent_geography_code": "E12000007"},
    "E10000001": {"name": "Bedfordshire", "parent_geography_code": "E12000006"},
    "E10000002": {"name": "Buckinghamshire", "parent_geography_code": "E12000008"},
    "E10000003": {"name": "Cambridgeshire", "parent_geography_code": "E12000006"},
    "E10000004": {"name": "Cheshire", "parent_geography_code": "E12000002"},
    "E10000005": {"name": "Cornwall and Isles of Scilly", "parent_geography_code": "E12000009"},
    "E10000006": {"name": "Cumbria", "parent_geography_code": "E12000002"},
    "E10000007": {"name": "Derbyshire", "parent_geography_code": "E12000004"},
    "E10000008": {"name": "Devon", "parent_geography_code": "E12000009"},
    "E10000009": {"name": "Dorset", "parent_geography_code": "E12000009"},
    "E10000010": {"name": "Durham", "parent_geography_code": "E12000001"},
    "E10000011": {"name": "East Sussex", "parent_geography_code": "E12000008"},
    "E10000012": {"name": "Essex", "parent_geography_code": "E12000006"},
    "E10000013": {"name": "Gloucestershire", "parent_geography_code": "E12000009"},
    "E10000014": {"name": "Hampshire", "parent_geography_code": "E12000008"},
    "E10000015": {"name": "Hertfordshire", "parent_geography_code": "E12000006"},
    "E10000016": {"name": "Kent", "parent_geography_code": "E12000008"},
    "E10000017": {"name": "Lancashire", "parent_geography_code": "E12000002"},
    "E10000018": {"name": "Leicestershire", "parent_geography_code": "E12000004"},
    "E10000019": {"name": "Lincolnshire", "parent_geography_code": "E12000004"},
    "E10000020": {"name": "Norfolk", "parent_geography_code": "E12000006"},
    "E10000021": {"name": "Northamptonshire", "parent_geography_code": "E12000004"},
    "E10000022": {"name": "Northumberland", "parent_geography_code": "E12000001"},
    "E10000023": {"name": "North Yorkshire", "parent_geography_code": "E12000003"},
    "E10000024": {"name": "Nottinghamshire", "parent_geography_code": "E12000004"},
    "E10000025": {"name": "Oxfordshire", "parent_geography_code": "E12000008"},
    "E10000026": {"name": "Shropshire", "parent_geography_code": "E12000005"},
    "E10000027": {"name": "Somerset", "parent_geography_code": "E12000009"},
    "E10000028": {"name": "Staffordshire", "parent_geography_code": "E12000005"},
    "E10000029": {"name": "Suffolk", "parent_geography_code": "E12000006"},
    "E10000030": {"name": "Surrey", "parent_geography_code": "E12000008"},
    "E10000031": {"name": "Warwickshire", "parent_geography_code": "E12000005"},
    "E10000032": {"name": "West Sussex", "parent_geography_code": "E12000008"},
    "E10000033": {"name": "Wiltshire", "parent_geography_code": "E12000009"},
    "E10000034": {"name": "Worcestershire", "parent_geography_code": "E12000005"},
}
#create la_name


#define education phases

education_phases = ["Primary", "Secondary", "Special", "Total"]


#create an empty list
main_data=[]

# create a for loop so every geographic level gets variables 


# for each level in geographic levels 
for geo in geographic_levels:
    # if the level is national
    if geo == "National":
        # then do a for loop for each education phase in the education phase list
        for phase in education_phases:

            # create log normally distributed head counts to append later 
            headcount = int(np.clip(np.random.lognormal(1e7, 5e6), 12e3, 2e8))
            #create suspension numbers to append later - normally distributed too
            suspensions = int(np.clip(np.random.normal(2e1, 4e3),2e2,1e3 ))
            #create susp_rate col to append later - normally distributed
            susp_rate = int(np.clip(np.random.normal(100000, 30000), 0, 200000))
            # append the following to the empty list
            main_data.append({ 
                # put the time identifer as is
                "time_identifier": time_identifier,
                # put the time period as is
                "time_period": time_period,
                # use each geographic level
                "geographic_levels": geo,
                # use country code as is because it's the same throughout 
                "country_code": country_code,
                # use country name as is because it's the same throughout 
                "country_name": country_name,
                # leave region code empty because this is national level so no regional data
                "region_code": "",
                # leave region name empty because this is national level so no regional data
                "region_name": "",
                # use each education phase
                "education_phases": phase,
                # use the headcount data generated earlier 
                "headcount": headcount,
                #use the suspensions number generated earlier 
                "suspensions": suspensions
            })
    # now do the regional 
    elif geo == "Regional":
        # for each region code and name in the region dictionary
        for code, name in region_dict.items():
            # for each education phase
            for phase in education_phases:
                # create log normally distributed head counts for region
                headcount = int(np.clip(np.random.lognormal(1e5, 5e5), 1e3, 3e6))
                # append the data for this region and phase
                main_data.append({
                    # put the time identifer as is
                    "time_identifier": time_identifier,
                    # put the time period as is
                    "time_period": time_period,
                    # use each geographic level
                    "geographic_levels": geo,
                    # use country code as is because it's the same throughout 
                    "country_code": country_code,
                    # use country name as is because it's the same throughout 
                    "country_name": country_name,
                    # use the region code for this row
                    "region_code": code,
                    # use the region name for this row
                    "region_name": name,
                    # use each education phase
                    "education_phases": phase,
                    # use the headcount data generated earlier 
                    "headcount": headcount
                })
    # now do la level
    else:
        # for each local authority code and info in the la dictionary
        for la_code, la_info in la_dict.items():
            # get the parent region code for this LA
            parent_region_code = la_info["parent_geography_code"]
            # get the LA name
            la_name = la_info["name"]
            # get the region name from the region dictionary
            region_name = region_dict[parent_region_code]
            # for each education phase
            for phase in education_phases: 
                # create normally distributed head counts for LA
                headcount = int(np.clip(np.random.lognormal(1e3, 4e3), 1e2, 3e4))
                # append the data for this LA and phase
                main_data.append({
                    # put the time identifer as is
                    "time_identifier": time_identifier,
                    # put the time period as is
                    "time_period": time_period,
                    # use each geographic level
                    "geographic_levels": geo, 
                    # use country code as is because it's the same throughout 
                    "country_code": country_code,
                    # use country name as is because it's the same throughout 
                    "country_name": country_name, 
                    # use the parent region code for this LA
                    "region_code": parent_region_code, 
                    # use the region name for this LA
                    "region_name": region_name, 
                    # use the LA code for this row
                    "la_code": la_code,
                    # use the LA name for this row
                    "la_name": la_name, 
                    # use each education phase
                    "education_phases": phase,
                    # use the headcount data generated earlier 
                    "headcount": headcount
                })


df = pd.DataFrame(main_data)

print(df)

df.to_csv("example.csv", index = False)

