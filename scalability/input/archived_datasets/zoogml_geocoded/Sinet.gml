graph [
  DateObtained "22/10/10"
  GeoLocation "Japan"
  GeoExtent "Country"
  Network "Sinet"
  Provenance "Primary"
  Access 0
  Source "http://www.sinet.ad.jp/topology"
  Version "1.0"
  DateType "Current"
  Type "REN"
  Backbone 1
  Commercial 0
  label "Sinet"
  Customer 0
  IX 0
  LastAccess "3/08/10"
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 0
  NetworkDate "2010-08"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Sapporo DC"
    Country "Japan"
    Longitude 141.34694
    Latitude 43.06417
    type "Core Node"
  ]
  node [
    id 1
    label "Sendai DC"
    Country "Japan"
    Longitude 140.87194
    Latitude 38.26889
    type "Core Node"
  ]
  node [
    id 2
    label "Fukuoka DC"
    Country "Japan"
    Longitude 130.41806
    Latitude 33.60639
    type "Core Node"
  ]
  node [
    id 3
    label "Hiroshima DC"
    Country "Japan"
    Longitude 132.45937
    Latitude 34.39627
    type "Core Node"
  ]
  node [
    id 4
    label "Matsuyama DC"
    Country "Japan"
    Longitude 132.76574
    Latitude 33.83916
    type "Core Node"
  ]
  node [
    id 5
    label "Osaka DC"
    Country "Japan"
    Longitude 135.50218
    Latitude 34.69374
    type "Core Node"
  ]
  node [
    id 6
    label "Kyoto DC"
    Country "Japan"
    Longitude 135.75385
    Latitude 35.02107
    type "Core Node"
  ]
  node [
    id 7
    label "Nagoya DC"
    Country "Japan"
    Longitude 136.90641
    Latitude 35.18147
    type "Core Node"
  ]
  node [
    id 8
    label "Kanazawa DC"
    Country "Japan"
    Longitude 136.62556
    Latitude 36.59444
    type "Core Node"
  ]
  node [
    id 9
    label "Tsukuba DC"
    Country "Japan"
    Longitude 140.1
    Latitude 36.2
    type "Core Node"
  ]
  node [
    id 10
    label "Tokyo DC2"
    Country "Japan"
    Longitude 139.5813
    Latitude 35.61488
    type "Core Node"
  ]
  node [
    id 11
    label "Tokyo DC1"
    Country "Japan"
    Longitude 139.5813
    Latitude 35.61488
    type "Core Node"
  ]
  node [
    id 12
    label "Tokyo DC3"
    Country "Japan"
    Longitude 139.5813
    Latitude 35.61488
    type "Core Node"
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
    LinkSpeedUnits "G"
    LinkLabel "40Gbps"
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
    LinkSpeedUnits "G"
    LinkLabel "40Gbps"
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
