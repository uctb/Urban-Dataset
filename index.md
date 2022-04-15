
## Download UCTB datasets

It is available for the access of datasets in the UCTB format with granularity of 5 minutes and 60 minutes respectively. As described in [4.1. Use datasets from UCTB](https://uctb.github.io/UCTB/md_file/tutorial.html#use-datasets-from-uctb), These datasets were collected from U.S. open data portals.

### 5-minute granularity

|        Attributes        | **New York City** |   **Chicago**   |     **DC**      |   **METR_LA**   |     **PEMS_BAY**      |
| :----------------------: | :---------------: | :-------------: | :-------------: | :-------------: | :-------------: |
|        TimeRange         |  2013.07.01-2017.09.30  | 2013.07.01-2017.09.30 | 2013.07.01-2017.09.30 | 2012.03.01-2012.06.28 | 2017.01.01-2017.07.01 |
|       TimeFitness        |         5         |         5       |         5       |         5       |         5       |
|    TrafficNode.shape     |   (446976, 820)   |  (446976, 585)  |       (446976, 532)        |(34272, 207)|(52128, 325)|
|TrafficMonthlyInteraction.shape|   (51, 820, 820)  |       (51, 585, 585)       |       (51, 532, 532)       |[0]|[0]|
|    StationInfo.shape     |     [820, 5]      |       [585, 5]       |       [532, 5]       |[207,5]|[325,5]|
|     Node.POI.shape       |         [0]       |       [0]       |       [0]       |None|None
|    TrafficGrid.shape     | (446976, 20, 20)  |       (446976, 20, 20)       |       (446976, 20, 20)       |[0]|[0]|
|    GridLatLng.shape      |      [21, 2]      |       [21, 2]       |       [21, 2]       |[0]|[0]|
|     Grid.POI.shape       |         [0]       |       [0]       |       [0]       |None|None|
|     Weather.shape        |         [0]       |       [0]       |       [0]       |[0]|[0]|
|       download               |[66.0M](./Public_Datasets/Bike/5_minutes/Bike_NYC.zip)              |[30.2M](./Public_Datasets/Bike/5_minutes/Bike_Chicago.zip)      |[31.0M](./Public_Datasets/Bike/5_minutes/Bike_DC.zip)|[11.8M](./Public_Datasets/Speed/5_minutes/METR_LA.zip)|[27.9M](./Public_Datasets/Speed/5_minutes/PEMS_BAY.zip)|

### 60-minute granularity

|        Attributes        | **New York City** |   **Chicago**   |     **DC**      |
| :----------------------: | :---------------: | :-------------: | :-------------: |
|        TimeRange         |  2013.07.01-2017.09.30  | 2013.07.01-2017.09.30 | 2013.07.01-2017.09.30 |
|       TimeFitness        |         60         |         60       |         60       |
|    TrafficNode.shape     |   (37248, 820)   |  (37248, 585)  |       (37248, 532)        |
|TrafficMonthlyInteraction.shape|   (51, 820, 820)  |       (51, 585, 585)       |       (51, 532, 532)       |
|    StationInfo.shape     |     [820, 5]      |       [585, 5]       |       [532, 5]       |
|     Node.POI.shape       |         [0]       |       [0]       |       [0]       |
|    TrafficGrid.shape     | (37248, 20, 20)  |       (37248, 20, 20)       |       (37248, 20, 20)       |
|    GridLatLng.shape      |      [21, 2]      |       [21, 2]       |       [21, 2]       |
|     Grid.POI.shape       |         [0]       |       [0]       |       [0]       |
|     Weather.shape        |         [37248, 26]       |       [37248, 26]       |       [37248, 26]       |
|     CheckInFeature.shape        |         [820, 2]       |       [585, 2]       |       [532, 2]       |
|       download               |        [20.5M](./Public_Datasets/Bike/60_minutes/Bike_NYC.zip)      |        [11.0M](./Public_Datasets/Bike/60_minutes/Bike_Chicago.zip)    |      [10.7M](./Public_Datasets/Bike/60_minutes/Bike_DC.zip)      |

### Node visualization

Following shows the map-visualization of bike stations in NYC, Chicago and DC.

<img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_NYC.jpg" style="zoom:30%;height:800px;width:800px;" /> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_Chicago.jpg" style="zoom:30%;height:800px;width:800px;"/> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/Bike_DC.jpg" style="zoom:30%;height:800px;width:800px;" />

Following shows the map-visualization of grid-based ride-sharing stations in METR-LA and PEMS-BAY.

<img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/METR_LA.png" style="zoom:30%;height:800px;width:800px;" /> <img src="https://uctb.github.io/UCTB/sphinx/md_file/src/image/PEMS_BAY.png" style="zoom:30%;height:800px;width:800px;"/> 

### Results on datasets

The result of these datasets can be found [here](https://uctb.github.io/UCTB/md_file/all_results.html).