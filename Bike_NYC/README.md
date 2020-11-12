# BIKE NYC DATASET

## Data Description

The bikesharing datasets are collected from [U.S. open data portals](https://www.citibikenyc.com/system-data). The dataset time span is more than four years. The total number of historical flow records is around 49 million and each record contains the start station, start time, stop station, stop time, etc. The file tree of Bike NYC dataset look likes:

```
│  README.md
│
├─Context
│      station_1_context.csv
│      station_list.csv
│
├─Graph
│      correlation_network.csv
│      distance_network.csv
│      interaction_network.csv
│
└─STData
        demand_stdata.csv
        spatial_node.csv
```

## Dataset Time Span

**2013-07-01 ~ 2017-09-30**

## Temporal Granularity

**60 minutes**

## Bike Demand Data

Bike demand data is a kind of spatiotemporal data and thus stored in `STData` sub directory. This directory consists of following files:

* `demand_stdata.csv`
* `spatial_node.csv`

 `demand_stdata.csv` is organized with shape [time_step, station_numbers] and its value represent the bike demand. `spatial_node.csv` stores the spatial information of bike stations including the latitude and longitude information.

##  Graph Data

`Graph` directory stores different types of graph information that can represent diverse correlation among stations. For the Bike NYC  dataset, we build three graphs, namely distance, correlation and interaction and store them in following files.

* `distance_network.csv`
* `correlation_network.csv`
* `interaction _network.csv`

Distance graph reflects the spatial distances among different stations, we build it by calculating the euclidean distance (e.g. if the distance $d_{a.b}$ between node $a$ and node $b$ is larger than a given threshold, the adjacent matrix will be set to 1, otherwise it will be set to 0). Correlation graph is built by calculating the pearson correlation coefficient and interaction graph is built by counting the monthly interaction flow.

The network file is like this：

```
	S0_TO_S0	S0_TO_S1	S0_TO_S2	...
[Time]	0	0	0	0	0	0	0	...

```

The columns of network file denote the weight between two stations and the row index represent time horizon which means the graph can be temporally dynamic. Note that the graph also can be static when the row index is `static`.

## Context Data

Context can help characterize the situation of an entity, where an entity can be a person, place, or physical or computational object, and are useful in urban application. Context data was stored in `Context` directory including following files: 

* `station_1_context.csv`
* `station_list.csv`

Context data is organized like spatiotemporal data. 