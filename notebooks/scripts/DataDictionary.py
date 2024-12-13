import pandas as pd
import numpy as npim

# # # # # # # # # #      Data Dictionary Script      # # # # # # # # # # 
# Notes:   

# To access the data dictionary, run this script inside of the Jupyter notebook.

# You can access the dictionary in two ways, in its dictionary form or as a df:





######      Enables df to help describe terminology found in the notebooks and through the project

########################### Data Dictionary applied in the Juptyer notebooks ########################
#
#      J:Brainstation\BS Git\Tampa_Apollo_AnthropogenicIndex\notebooks\Anthrogenic.ipynb
#      J:\Brainstation\BS Git\Tampa_Apollo_AnthropogenicIndex\notebooks\AnthropogenicPressure_ProcEdaBLModel.ipynb.ipynb
#      J:\Brainstation\BS Git\Tampa_Apollo_AnthropogenicIndex\notebooks\Benthic_EDA_beta.ipynb
#      J:\Brainstation\BS Git\Tampa_Apollo_AnthropogenicIndex\notebooks\Final_A.P.Index_RNN.ipynb.ipynb
#      J:\Brainstation\BS Git\Tampa_Apollo_AnthropogenicIndex\note notebooks\EstuarineEcosystems_ProcEdaBLModel.ipynb.ipynb
      

indices= {'SDI':'Shannon Diversity Index',          
          'WQI' : 'Water Quality Index',
               'TBNI': 'Tampa Bay Nekton Index',
               'TBBI':  'Tampa Bay Benthic Index'
                                           
              }
organizations= {'TBEP':'Tampa Bay Estuary Program',
                'FWC': 'Florida Fish and Wildflife Commission',
                'NOAA':  'National Oceanic and Atmospheric',
                'NMFS':  'National Marine Fisheries Service',
                'HC':    'Hillsborough County',
                'HCPA':  'Hillsborough COunty Property'

    
}

measurements={

    'ug/L' : 'micrograms per liter- value: 10E-6',
    'mg/G' : 'milligrams per liter- value: 10E-3'
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
    'location': locations,
    'indices': indices,
    'compound': compounds,
    'terminology': terminology,
    'test':tests
}


dic_df=pd.DataFrame(columns=['definition'])
dic_df=pd.DataFrame(pd.concat([pd.Series(measurements)
                               ,pd.Series(locations)
                               ,pd.Series(compounds)
                               ,pd.Series(organizations)
                              ]))
