# Urban Dataset

## 现有的UCTB的格式

```python
DataFormat = {
    "TimeRange": [],    # 起止时间 str eg:['2016-10-01', '2016-11-30']
    "TimeFitness": [],  # 时间粒度 int 单位为min
    "Node": {
        "TrafficNode": [],  # with shape [time_slots, num-of-node] eg:(1440,256) 
        "TrafficMonthlyInteraction": [],
        "StationInfo": [],  # list eg:['0', 0, 34.210542575000005, 108.91390095, 'grid_0']
        "POI": []
    },
    "Grid": {
        "TrafficGrid": [], # with shape [slots, num-of-node. num-of-node] eg:(120, 256, 256)
        "GridLatLng": [],  # 对角线点的经纬度 eg:[[34.20829427, 108.91118]]
        "POI": []
    },
    "ExternalFeature": {
        "Weather": []
    }
}
```

## Design Principle

在uctb里新起一块把spatio temporal prediction的所有dataset抽象出一种通用的以纯文本文件形式存储的数据格式（我们现在用的pickle我感觉还是不太直观，因为必须用程序打开才能看。我觉得比较好的数据集的方式还是要纯文本），而且要比较灵活的可以后续进一步把一些场景融入，比如说graph可以动态变化。然后我们不同的数据集之间的关系，就可以想象称MINIST和fashion-MINIST的关系，比如我可以直接替换一个数据集的目录，所有其他的代码都不用变，我就可以重新run一个实验。原来pickle虽然也可以实现这个功能，但是不能直接用文本文件打开是个很大的问题。

我现在觉得我们需要一个文件夹，然后一个目录是data，每个站点序号一个文件，文件里就是存某种flow，第一列是时间，第二列是值，然后有一个文件夹是graph，存不同类型的graph的邻接表，第三个文件夹是external，包括天气、站点位置等。按这个思路组织一下目录结构，然后用某个数据集的一部分时间做个例子

## 通用数据集方案

| 文件夹/文件夹 |           **内容**            |             **聚合后维度**              | 文件格式 |
| :-----------: | :---------------------------: | :-------------------------------------: | :------: |
|    ST Data    |         存储时空数据          | [time_slots, number_node, feature_dims] |   csv    |
|    Context    |         存储外部数据          | [time_slots, number_node, feature_dims] |   csv    |
|     Graph     |          存储动态图           | [time_steps, number_node, number_node]  |   csv    |
|   README.md   | 数据集的相关信息, 来源/引用等 |                    /                    | markdown |

### ST Data

Crowd flow可能有多种，经过转化后的`ST tensor`应该具有如下维度[time_slots, number_node, feature_dims]，但为求直观，我们不应该直接存tensor，而是应该存matrix，通常情况下，number_node(节点数量)是大于feature_dims(flow的类型，例如inflow和outflow)，因此我们将一个csv存储一种flow，命名为`XXX_stdata.txt`，行代表timestamp，列代表站点序号.

站点信息存储在`spatial_node.csv`中，有以下四类(列)信息，第一列是序号(与Crowd flow对应)，二三列是维度、经度，第四列是留待扩展的信息(每个数据集自定义的信息)

```
	latitude	longitude	[other]
S1	34.156		116.372		other
```

ST DATA文件夹主要有两类信息：

* **XXX_flow.txt**
* **station.txt**

### Context

context与crowd flow类似，聚合后也应该具有以下维度[time_slots, number_node, feature_dims]，但是context数据一般难以获得多个站点的(一般一个城市只是用一个气象观测点的数据代替整个城市的数据)，因此number_node通常为1，我们将一个站点的context数据存在一个csv文件中，行代表timestamp，列代表context类型(例如降雨、风速等等)

* **station_XXX_context.txt**

### Graph

为了便于以后扩展，**需要考虑到时空dynamic**，时间是指每个timestep的graph连接关系不同，需要注意的是站点数量(图节点的数量)也可能发生变化. 参考jure的设计，节点数量不同的认为是不同的network，存储在不同的graph中.

Graph是动态的，存储的是边与边的关系，经过转化后的graph应该具有如下维度[time_slots, number_node, number_node],

#### Prof. jure's design

先调研了SNAP的设计 http://snap.stanford.edu/data/comm-f2f-Resistance.html

|             **File**             |                       **Description**                        |
| :------------------------------: | :----------------------------------------------------------: |
|         network_list.csv         |                   network/network[ID].csv                    |
|     network/network[ID].csv      | Dynamic face-to-face interaction networks. One file per network. |
| network/network[ID]_weighted.csv | Weighted version of dynamic face-to-face interaction networks. One file per network. |

其中的`network_list.csv`格式如下：

```
NETWORK,NUMBER_OF_PARTICIPANTS
0,7
1,8
```

ID表示的网络的序号，NUMBER_OF_PARTICIPANTS表示节点数量，对于每一个ID，有一个csv文件存储着每个网络的时间的变化情况. 

例如`network/network[ID].csv`：

```bash
TIME	P1_TO_LAPTOP	P1_TO_P1	P1_TO_P2	P1_TO_P3	P1_TO_P4	P1_TO_P5	P1_TO_P6
0	0.049	0	0.058	0.152	0.194	0.053	0.137
1	0.054	0	0.086	0.143	0.265	0.06	0.211
2	0.041	0	0.239	0.102	0.207	0.03	0.232
3	0.167	0	0.088	0.118	0.254	0.071	0.104
4	0.386	0	0.112	0.075	0.17	0.04	0.079
5	0.709	0	0.004	0.031	0.127	0.029	0.029
6	0.107	0	0.483	0.125	0.108	0.029	0.092
7	0.021	0	0.192	0.109	0.395	0.043	0.078
8	0.017	0	0.011	0.102	0.547	0.063	0.031
9	0.02	0	0.021	0.085	0.54	0.073	0.044
10	0.474	0	0.023	0.049	0.258	0.047	0.047
11	0.266	0	0.08	0.107	0.23	0.059	0.092
12	0.043	0	0.107	0.141	0.239	0.069	0.16
13	0.22	0	0.135	0.121	0.183	0.044	0.145
14	0.387	0	0.031	0.086	0.21	0.051	0.082
15	0.046	0	0.053	0.135	0.262	0.066	0.19
16	0.041	0	0.054	0.127	0.27	0.056	0.232
17	0.024	0	0.047	0.09	0.168	0.041	0.458
18	0.024	0	0.051	0.21	0.249	0.039	0.226
```

#### 我们的设计

我们的设计可以follow上述设计，不过由于我们的ST数据的站点是静态的（站点固定，只有一个网络，network_list.csv可以不要），只保留`network/network[ID].csv`的形式，同时，我们有多种类型的graph,存多个csv，每种csv代表一种graph. 文件夹目录如下：

* **XXX_network.csv**

### 文件树

以Bike_NYC的数据存储为例，设计的文件目录树如下：

```
│  README.md
│
├─Context
│      station_1_context.csv
│      station_2_context.csv
│
├─Graph
│      correlation_network.csv
│      distance_network.csv
│
└─STData
        in_flow.csv
        out_flow.csv
        station.txt
```



------

## Reference

http://snap.stanford.edu/data/

http://snap.stanford.edu/data/comm-f2f-Resistance.html

