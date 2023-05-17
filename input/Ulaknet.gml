graph [
  DateObtained "21/10/10"
  GeoLocation "Turkey"
  GeoExtent "Country"
  Network "ULAKNET"
  Provenance "Primary"
  Access 0
  Source "http://www.ulakbim.gov.tr/hakkimizda/tarihce/ulaknet/YeniUlak2010.jpg"
  Version "1.0"
  DateType "Current"
  Type "REN"
  Backbone 1
  Commercial 0
  label "ULAKNET"
  Customer 0
  IX 0
  LastAccess "21/10/10"
  Note "Very sparse webpage"
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 0
  NetworkDate "2010-10"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Istanbul"
    Country "Turkey"
    Longitude 28.94966
    Internal 1
    Latitude 41.01384
    type "Red Colour"
  ]
  node [
    id 1
    label "iZMiR"
    Country "Turkey"
    Longitude 27.13838
    Internal 1
    Latitude 38.41273
    type "Red Colour"
  ]
  node [
    id 2
    label "Ankara"
    Country "Turkey"
    Longitude 32.85427
    Internal 1
    Latitude 39.91987
    type "Red Colour"
  ]
  node [
    id 3
    label "GEANT"
    Internal 0
  ]
  node [
    id 4
    label "Internet"
    Internal 0
  ]
  node [
    id 5
    label "Internet"
    Internal 0
  ]
  edge [
    source 0
    target 1
    LinkLabel "1-4.999Gbps"
  ]
  edge [
    source 0
    target 2
    LinkLabel "5-10Gbps"
  ]
  edge [
    source 0
    target 3
    LinkSpeed "5"
    LinkSpeedUnits "G"
    LinkLabel "5Gbps"
    LinkSpeedRaw 5000000000.0
  ]
  edge [
    source 0
    target 4
    LinkSpeed "5"
    LinkSpeedUnits "G"
    LinkLabel "5Gbps"
    LinkSpeedRaw 5000000000.0
  ]
  edge [
    source 1
    target 2
    LinkLabel "155-599Mbps"
  ]
  edge [
    source 2
    target 5
    LinkSpeed "5"
    LinkSpeedUnits "G"
    LinkLabel "5Gbps"
    LinkSpeedRaw 5000000000.0
  ]
]
