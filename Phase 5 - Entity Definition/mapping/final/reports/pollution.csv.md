# pollution.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _Location_
From column: _Stazione_
``` python
station = getValue("Stazione")
place = "Trento"
if station == "Piana Rotaliana":
    place = "Mezzocorona"
elif station == "Rovereto":
    place = "Rovereto"
elif station == "Borgo Valsugana":
    place = "Borgo Valsugana"
elif station == "Riva del Garda":
    place = "Riva del Garda"
elif station == "A22 (Avio)":
    place = "Avio"
elif station == "Monte Gaza":
    place = "Margone"
return place
```

#### _URI_
From column: _Stazione_
``` python
return getValue("Data") + "T" + getValue("Ora") + getValue("Stazione") + getValue("Inquinante")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Data_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_date` | `Pollution_GID-1051`|
| _Inquinante_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_polluting` | `Pollution_GID-1051`|
| _Location_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_name` | `Location_GID-1011`|
| _Ora_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_hour` | `Pollution_GID-1051`|
| _Stazione_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_station` | `Pollution_GID-1051`|
| _URI_ | `uri` | `Pollution_GID-1051`|
| _Unità di misura_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_measurement_unit` | `Pollution_GID-1051`|
| _Valore_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_value` | `Pollution_GID-1051`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `Pollution_GID-1051` | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#hasLocation` | `Location_GID-1011`|
