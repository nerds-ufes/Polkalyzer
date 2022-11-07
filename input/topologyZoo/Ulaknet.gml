graph [
  DateObtained "21/10/10"
  GeoLocation "Turkey"
  GeoExtent "Country"
  Customer 0
  Network "ULAKNET"
  IX 0
  Provenance "Primary"
  Note "Very sparse webpage"
  Source "http://www.ulakbim.gov.tr/hakkimizda/tarihce/ulaknet/YeniUlak2010.jpg"
  Version "1.0"
  Type "REN"
  LastAccess "21/10/10"
  Access 0
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2010-10"
  label "ULAKNET"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Istanbul"
    Internal 1
    Latitude 41.01384
    Country "Turkey"
    type "Red Colour"
    Longitude 28.94966
  ]
  node [
    id 1
    label "iZMiR"
    Internal 1
    Latitude 38.41273
    Country "Turkey"
    type "Red Colour"
    Longitude 27.13838
  ]
  node [
    id 2
    label "Ankara"
    Internal 1
    Latitude 39.91987
    Country "Turkey"
    type "Red Colour"
    Longitude 32.85427
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
    LinkLabel "5Gbps"
    LinkSpeedUnits "G"
    LinkSpeedRaw 5000000000.0
  ]
  edge [
    source 0
    target 4
    LinkSpeed "5"
    LinkLabel "5Gbps"
    LinkSpeedUnits "G"
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
    LinkLabel "5Gbps"
    LinkSpeedUnits "G"
    LinkSpeedRaw 5000000000.0
  ]
]
