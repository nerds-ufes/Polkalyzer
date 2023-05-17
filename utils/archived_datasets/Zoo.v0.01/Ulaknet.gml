graph [
  DateObtained "21/10/10"
  GeoLocation "Turkey"
  GeoExtent "Country"
  Network "ULAKNET"
  Note "Very sparse webpage"
  Source "http://www.ulakbim.gov.tr/hakkimizda/tarihce/ulaknet/YeniUlak2010.jpg"
  Version "1.0"
  Type "REN"
  Backbone 1
  Commercial 0
  label "ULAKNET"
  Customer 0
  LastAccess "21/10/10"
  Access 0
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  Developed "developing"
  Transit 0
  NetworkDate "C"
  Testbed 0
  SvnVersion 8043
  node [
    id 0
    label "Istanbul"
    Internal 1
    type "Red Colour"
  ]
  node [
    id 1
    label "iZMiR"
    Internal 1
    type "Red Colour"
  ]
  node [
    id 2
    label "Ankara"
    Internal 1
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
    LinkLabel "5Gbps"
    LinkSpeedUnits "G"
  ]
  edge [
    source 0
    target 4
    LinkSpeed "5"
    LinkLabel "5Gbps"
    LinkSpeedUnits "G"
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
  ]
]
