#  Welcome to the UCTB datasets release pages!

## How to load the data?

We've collected some public datasets and processing them into [UCTB dataset format](https://uctb.github.io/UCTB/md_file/tutorial.html#build-your-own-datasets). UCTB dataset is a python build-in dictionary object that could be loaded by [pickle package](https://docs.python.org/3/library/pickle.html). Here is the example of UCTB dataset.

```python
UCTB_dataset = {
    "TimeRange": ['YYYY-MM-DD', 'YYYY-MM-DD'], # time span of datasets (e.g., 2013.07.01-2017.09.30)
    "TimeFitness": 60, # Minutes
    
    "Node": { # Designed for GNNs models, it is a dictionary that stores traffic data.
        "TrafficNode": np.array, # With shape [time, num-of-node]
        "StationInfo": list # elements in it should be [id, build-time, lat, lng, name]
    },

    "Grid": { # Designed for CNNs models, it is a dictionary that stores Grid data.
        "TrafficGrid": [], np.array, # With shape [time, num_rows, num_cols]
        "GridLatLng": [], list # It stores the geographic information of each grid.
    },

    "ExternalFeature": {} # Designed to store external features (e.g., weather), it is currently a reserved key. 
}
```

Here is the example of loading data by pickle package:

```python
import pickle
with open("Bike_NYC.pkl","rb") as fp:
    data = pickle.load(fp)
```

UCTB also provides dataloader (namely `NodeTrafficLoader` and `GridTrafficLoader`) to process data. Please see our [documents ](https://uctb.github.io/UCTB/UCTB.dataset.html)for more information.

```python
# loading Grid traffic
from UCTB.dataset import GridTrafficLoader
data_loader = GridTrafficLoader(dataset="Bike", city="NYC")


# loading Node traffic
from UCTB.dataset import NodeTrafficLoader
data_loader = NodeTrafficLoader(dataset="Bike", city="NYC")
```

## Bike datasets

The bikesharing datasets are collected from U.S. open data portals including New York City (NYC, https://www.citibikenyc.com/system-data), Chicago (CHI, https://www.divvybikes.com/system-data), and DC (https://www.capitalbikeshare.com/system-data). The dataset time span for all three cities is more than four years. The total number of historical flow records is around 49 million, 13 million, and 14 million in NYC, Chicago, and DC, respectively, and each record contains the start station, start time, stop station, stop time, etc. We count the number of bikesharing demands in each station at the next moment.

Following shows the map-visualization of bike stations in NYC, Chicago and DC.

<img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_NYC.jpg" style="zoom: 30%; height: 800px; width: 800px;" /> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_Chicago.jpg" style="zoom: 30%; height: 800px; width: 800px;"/> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_DC.jpg" style="zoom: 30%; height: 800px; width: 800px;" />



**5-minutes granularity data catalog**: https://github.com/uctb/Urban-Dataset/tree/main/Public_Datasets/Bike/5_minutes

**60-minutes granularity data catalog**: https://github.com/uctb/Urban-Dataset/tree/main/Public_Datasets/Bike/60_minutes

Following lists the detail of the datasets:

|        **5-minutes**        | **New York City** |   **Chicago**   |     **DC**      |   **METR_LA**   |     **PEMS_BAY**      |
| :----------------------: | :---------------: | :-------------: | :-------------: | :-------------: | :-------------: |
|        TimeRange         |  2013.07.01-2017.09.30  | 2013.07.01-2017.09.30 | 2013.07.01-2017.09.30 | 2012.03.01-2012.06.28 | 2017.01.01-2017.07.01 |
|       TimeFitness        |         5         |         5       |         5       |         5       |         5       |
|    TrafficNode.shape     |   (446976, 820)   |  (446976, 585)  |       (446976, 532)        |(34272, 207)|(52128, 325)|
|    StationInfo.shape     |     [820, 5]      |       [585, 5]       |       [532, 5]       |[207,5]|[325,5]|
|    TrafficGrid.shape     | (446976, 20, 20)  |       (446976, 20, 20)       |       (446976, 20, 20)       |[0]|[0]|
|    GridLatLng.shape      |      [21, 2]      |       [21, 2]       |       [21, 2]       |[0]|[0]|
|       Size            |[66.0M](./Public_Datasets/Bike/5_minutes/Bike_NYC.zip)              |[30.2M](./Public_Datasets/Bike/5_minutes/Bike_Chicago.zip)      |[31.0M](./Public_Datasets/Bike/5_minutes/Bike_DC.zip)|[11.8M](./Public_Datasets/Speed/5_minutes/METR_LA.zip)|[27.9M](./Public_Datasets/Speed/5_minutes/PEMS_BAY.zip)|

|        **60-minutes**        | **New York City** |   **Chicago**   |     **DC**      |
| :----------------------: | :---------------: | :-------------: | :-------------: |
|        TimeRange         |  2013.07.01-2017.09.30  | 2013.07.01-2017.09.30 | 2013.07.01-2017.09.30 |
|       TimeFitness        |         60         |         60       |         60       |
|    TrafficNode.shape     |   (37248, 820)   |  (37248, 585)  |       (37248, 532)        |
|    StationInfo.shape     |     [820, 5]      |       [585, 5]       |       [532, 5]       |
|    TrafficGrid.shape     | (37248, 20, 20)  |       (37248, 20, 20)       |       (37248, 20, 20)       |
|    GridLatLng.shape      |      [21, 2]      |       [21, 2]       |       [21, 2]       |
|       download               |        [20.5M](./Public_Datasets/Bike/60_minutes/Bike_NYC.zip)      |        [11.0M](./Public_Datasets/Bike/60_minutes/Bike_Chicago.zip)    |      [10.7M](./Public_Datasets/Bike/60_minutes/Bike_DC.zip)      |

##  Speed datasets

The two traffic speed datasets are widely used in STTP research: METR-LA and PEMS-BAY from Los Angeles (LA) County and Bay Area, respectively. In METR-LA, 207 sensors record highway vehicles’ speeds for four months; In PEMS-BAY, there are 325 sensors for six months. Each sensor can be seen as a station, and we predict the traffic speed of each sensor at the next time slot.

Following shows the map-visualization of grid-based ride-sharing stations in METR-LA and PEMS-BAY.

<img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/METR_LA.png" style="zoom: 33%; height: 800px; width: 800px;" /> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/PEMS_BAY.png" style="zoom: 33%; height: 800px; width: 800px;"/> 

**5-minutes granularity data catalog**: https://github.com/uctb/Urban-Dataset/tree/main/Public_Datasets/Speed/5_minutes

Following lists the detail of the datasets:

|   **5-minutes**   |                      **METR_LA**                       |                      **PEMS_BAY**                       |
| :---------------: | :----------------------------------------------------: | :-----------------------------------------------------: |
|     TimeRange     |                 2012.03.01-2012.06.28                  |                  2017.01.01-2017.07.01                  |
|    TimeFitness    |                           5                            |                            5                            |
| TrafficNode.shape |                      (34272, 207)                      |                      (52128, 325)                       |
| StationInfo.shape |                        [207,5]                         |                         [325,5]                         |
| TrafficGrid.shape |                          [0]                           |                           [0]                           |
| GridLatLng.shape  |                          [0]                           |                           [0]                           |
|       Size        | [11.8M](./Public_Datasets/Speed/5_minutes/METR_LA.zip) | [27.9M](./Public_Datasets/Speed/5_minutes/PEMS_BAY.zip) |

## How to get the datasets at other granularities?

We could merge the fine-grained data to obtain the datasets at other granularities (e.g., by summing the 12 flows from the 5-minutes datasets to obtain 60-minutes datasets). UCTB provides the API to merge data. You could specify MergeIndex and MergeWay in the `NodeTrafficLoader` and `GridTrafficLoader`. Here is an example:

```python
from UCTB.dataset import NodeTrafficLoader

# loading 5-minutes datasets
data_loader = NodeTrafficLoader(dataset="Bike", city="NYC") 
print(data_loader.dataset.node_traffic.shape) # with shape (446976, 820)

data_loader = NodeTrafficLoader(dataset="Bike", city="NYC", MergeIndex=12, MergeWay="sum")
print(data_loader.dataset.node_traffic.shape) # with shape (37248, 820)
```

