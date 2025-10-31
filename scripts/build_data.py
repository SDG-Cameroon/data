from sdg.open_sdg import open_sdg_build

def alter_data(df):
  if "REF_AREA" in df:
    df["GeoCode"]=df["REF_AREA"]
  return df

open_sdg_build(config='config_data.yml', alter_data=alter_data)
