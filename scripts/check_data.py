from sdg.open_sdg import open_sdg_check

def alter_data(df):
  if "REF_AREA" in df:
    df["GeoCode"]=df["REF_AREA"]
  return df

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_data=alter_data)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
