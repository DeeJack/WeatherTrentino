# waste.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _total_
From column: _undifferentiated_
``` python
return str(float(getValue("differentiated")) + float(getValue("undifferentiated")))
```

#### _URI_
From column: _id_
``` python
return getValue("id")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _URI_ | `uri` | `Waste_GID-1031`|
| _codEnte_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_cod_ente` | `Waste_GID-1031`|
| _differentiated_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_differentiated` | `Waste_GID-1031`|
| _id_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_waste_id` | `Waste_GID-1031`|
| _total_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_total` | `Waste_GID-1031`|
| _undifferentiated_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_undifferentiated` | `Waste_GID-1031`|
| _year_ | `http://www.semanticweb.org/loren/ontologies/2024/10/weather_trentino#has_year` | `Waste_GID-1031`|


## Links
| From | Property | To |
|  --- | -------- | ---|
