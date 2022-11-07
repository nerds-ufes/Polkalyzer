graph [
  DateObtained "22/10/10"
  GeoLocation "Japan"
  GeoExtent "Country"
  Customer 0
  Network "Sinet"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.sinet.ad.jp/topology"
  Version "1.0"
  Type "REN"
  LastAccess "3/08/10"
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2010-08"
  label "Sinet"
  Testbed 0
  Developed 1
  SvnVersion 8123
  node [
    id 0
    label "Sapporo DC"
    Latitude 43.06417
    Country "Japan"
    type "Core Node"
    Longitude 141.34694
  ]
  node [
    id 1
    label "Sendai DC"
    Latitude 38.26889
    Country "Japan"
    type "Core Node"
    Longitude 140.87194
  ]
  node [
    id 2
    label "Fukuoka DC"
    Latitude 33.60639
    Country "Japan"
    type "Core Node"
    Longitude 130.41806
  ]
  node [
    id 3
    label "Hiroshima DC"
    Latitude 34.39627
    Country "Japan"
    type "Core Node"
    Longitude 132.45937
  ]
  node [
    id 4
    label "Matsuyama DC"
    Latitude 33.83916
    Country "Japan"
    type "Core Node"
    Longitude 132.76574
  ]
  node [
    id 5
    label "Osaka DC"
    Latitude 34.69374
    Country "Japan"
    type "Core Node"
    Longitude 135.50218
  ]
  node [
    id 6
    label "Kyoto DC"
    Latitude 35.02107
    Country "Japan"
    type "Core Node"
    Longitude 135.75385
  ]
  node [
    id 7
    label "Nagoya DC"
    Latitude 35.18147
    Country "Japan"
    type "Core Node"
    Longitude 136.90641
  ]
  node [
    id 8
    label "Kanazawa DC"
    Latitude 36.59444
    Country "Japan"
    type "Core Node"
    Longitude 136.62556
  ]
  node [
    id 9
    label "Tsukuba DC"
    Latitude 36.2
    Country "Japan"
    type "Core Node"
    Longitude 140.1
  ]
  node [
    id 10
    label "Tokyo DC2"
    Latitude 35.61488
    Country "Japan"
    type "Core Node"
    Longitude 139.5813
  ]
  node [
    id 11
    label "Tokyo DC1"
    Latitude 35.61488
    Country "Japan"
    type "Core Node"
    Longitude 139.5813
  ]
  node [
    id 12
    label "Tokyo DC3"
    Latitude 35.61488
    Country "Japan"
    type "Core Node"
    Longitude 139.5813
  ]
  edge [
    source 0
    target 8
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 0
    target 1
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 1
    target 9
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 2
    target 3
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 2
    target 4
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 3
    target 6
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 4
    target 5
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 5
    target 6
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 5
    target 7
    LinkSpeed "40"
    LinkLabel "40Gbps"
    LinkSpeedUnits "G"
    LinkSpeedRaw 40000000000.0
  ]
  edge [
    source 6
    target 8
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 7
    target 11
    LinkSpeed "40"
    LinkLabel "40Gbps"
    LinkSpeedUnits "G"
    LinkSpeedRaw 40000000000.0
  ]
  edge [
    source 8
    target 10
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 9
    target 11
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 10
    target 11
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 10
    target 12
    LinkLabel "1-20Gbps"
  ]
]
