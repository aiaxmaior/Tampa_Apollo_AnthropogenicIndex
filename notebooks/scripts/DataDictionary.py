import pandas as pd
import numpy as np

measurements= {'SDI':'Shannon Diversity Index',
               'WQI' : 'Water Quality Index',
               'TBNI': 'Tampa Bay Nekton Index',
               'TBBI':  'Tampa Bay Benthic Index',
                                           
              }
organizations= {'TBEP':'Tampa Bay Estuary Program',
                'FWC': 'Florida Fish and Wildflife Commission',
                'NOAA':  'National Oceanic and Atmospheric',
                'NMFS':  'National Marine Fisheries Service',
                'HC':    'Hillsborough County',
                'HCPA':  'Hillsborough COunty Property'

    
}
locations={
    'HB': 'Hillsborough Bay',
    'MTB': 'Middle Tampa Bay',
    'OTB': 'Old Tampa Bay',
    'LTB': 'Lower Tampa Bay'

}
compounds={
    'Nit': 'Nitrates',
    'Phos': 'Phosphate'
}
terminology={
    'Anth.Gen.': 'Anthropogenic',

}
tests={
    'ADF':'AugmentedDickey-Fuller Test'
}
dic={
    'measurement': measurements,
    'organization': organizations,
    'location': locations
}


dic_df=pd.DataFrame()
dic_df=pd.DataFrame(pd.concat([pd.Series(measurements)
                               ,pd.Series(locations)
                               ,pd.Series(compounds)
                               ,pd.Series(organizations)
                              ]))