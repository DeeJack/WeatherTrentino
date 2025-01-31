# Climate Change Trentino - KGE 2024

Repository for the report on Climate Change in Trentino, for the Knowledge Engineering course 2024, UNITN.

By **Giacomo Tezza**, **Lorenzo Fumi**

## Abstract

The aim of the project is to create a Knowledge Graph capable to establish a comprehensive and interconnected representation of the factors contributing to climate change within the autonomous province of Trento. This purpose centers on capturing and linking various types of data (geospatial, meteorological, and demographic) over historical time frames, with the goal of illuminating the relationship between human activities, environmental conditions, and resulting climate impacts in this specific region.

By integrating geospatial data, such as that from OpenStreetMap, with historical meteorological records, including temperature trends, air quality metrics, and other environmental indicators, the Knowledge Graph aims to reflect the environmental transformations that have occurred over the years. Additionally, historical demographic data, such as population density, energy consumption, gas usage, water consumption, and waste production, will provide insight into local patterns of resource utilization and waste generation. These variables will collectively inform an understanding of how these human and environmental factors interlink to drive climate change in Trento.

Ultimately, the Knowledge Graph will serve as a tool to clarify the underlying causes of climate change within the context of this region, allowing users to explore the interconnected nature of socio-environmental impacts and aiding in the development of targeted actions or policies to address these issues.

## Project overview

The project aims to construct a Knowledge Graph that provides a complete view of climate change factors within the Trentino territory.
By linking various datasets, the KG facilitates exploration between human activities (population, consumption), environmental conditions (weather, pollution), and climate impacts, while promoting reusability for further research.

## Methdology

The project follows the iTelos methodology, emphasing clarity, reusability, and a systematic approach to knowledge graph engineering.

Phases:

1. Purpose definition: identifying the project goals, defining scope and context;
2. Information Gathering: sourcing and evaluating relevant datasets;
3. Language Definition: defining and formalizing concepts;
4. Knowledge Definition: constructing the taleontology, cleaning and formatting datasets;
5. Entity Definition: matching, identifying, and mapping entities across data sources, creating the KG;
6. Evaluation: Assessing the quality and utility of the knowledge graph;
7. Metadata definition: Defining data about the produced artifacts;

## Getting started

Clone the repository:

```bash
git clone https://github.com/DeeJack/WeatherTrentino.git
```

## Tools and technologies

- Python: language used for scraping, cleaning, formatting, transforming the data;
- Protègé: used for defining the teleontology;
- Karma: used for mapping the data to the teleontology;
- Git: for version control and collaboration;
- GraphDB: for querying the KG using SparQL;

## License

The project is licensed under Apache License 2.0, see [LICENSE](./LICENSE) for more information.

## Contributors

[Lorenzo Fumi](https://github.com/DeeJack)

[Giacomo Tezza](https://github.com/GiacomoTezza)

## Images

<!-- TODO -->