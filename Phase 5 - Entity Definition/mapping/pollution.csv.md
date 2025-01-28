# pollution.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _Stazione_
``` python
return getValue("Data") + "T" + getValue("Ora") + getValue("Stazione").replace(" ", "").replace(".", "") + getValue("Inquinante")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Data_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_date` | `Pollution_GID-1051`|
| _Inquinante_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_polluting` | `Pollution_GID-1051`|
| _Ora_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_hour` | `Pollution_GID-1051`|
| _Stazione_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#hasStation` | `Pollution_GID-1051`|
| _URI_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_pollution_id` | `Pollution_GID-1051`|
| _Unità di misura_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_measurement_unit` | `Pollution_GID-1051`|
| _Valore_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_value` | `Pollution_GID-1051`|


## Links
| From | Property | To |
|  --- | -------- | ---|
