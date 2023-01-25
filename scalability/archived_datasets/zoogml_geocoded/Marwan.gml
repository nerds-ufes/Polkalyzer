graph [
  DateObtained "22/10/10"
  GeoLocation "Morocco"
  GeoExtent "Country"
  Network "MARWAN"
  Provenance "Primary"
  Access 0
  Source "http://www.marwan.ma/forms/network.htm"
  Version "1.0"
  DateType "Current"
  Type "REN"
  Backbone 1
  Commercial 0
  label "MARWAN"
  Customer 1
  IX 0
  LastAccess "21/10/10"
  Layer "ATM"
  Classification "Backbone Customer"
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 0
  NetworkDate "2010-10"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Institution 1"
    Internal 1
  ]
  node [
    id 1
    label "University 3"
    Internal 1
  ]
  node [
    id 2
    label "University 1"
    Internal 1
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
    label ""
    Internal 1
  ]
  node [
    id 6
    label "University 4"
    Internal 1
  ]
  node [
    id 7
    label ""
    Internal 1
  ]
  node [
    id 8
    label ""
    Internal 1
  ]
  node [
    id 9
    label "Casa"
    Country "Morocco"
    Longitude -7.61916
    Internal 1
    Latitude 33.59278
  ]
  node [
    id 10
    label "Rabat"
    Country "Morocco"
    Longitude -6.83255
    Internal 1
    Latitude 34.01325
  ]
  node [
    id 11
    label "Agadir"
    Country "Morocco"
    Longitude -9.59815
    Internal 1
    Latitude 30.42018
  ]
  node [
    id 12
    label "Marrkech"
    Country "Morocco"
    Longitude -8.00828
    Internal 1
    Latitude 31.63148
  ]
  node [
    id 13
    label "Fes"
    Country "Morocco"
    Longitude -4.9998
    Internal 1
    Latitude 34.03715
  ]
  node [
    id 14
    label "Tanger"
    Country "Morocco"
    Longitude -5.81365
    Internal 1
    Latitude 35.78058
  ]
  node [
    id 15
    label "University 2"
    Internal 1
  ]
  edge [
    source 0
    target 8
    LinkSpeed "2"
    LinkSpeedUnits "M"
    LinkLabel "2Mb/s"
    LinkSpeedRaw 2000000.0
  ]
  edge [
    source 1
    target 8
    LinkSpeed "2"
    LinkSpeedUnits "M"
    LinkLabel "2Mb/s"
    LinkSpeedRaw 2000000.0
  ]
  edge [
    source 2
    target 14
    LinkSpeed "34"
    LinkSpeedUnits "M"
    LinkLabel "34Mb/s"
    LinkSpeedRaw 34000000.0
  ]
  edge [
    source 3
    target 5
    LinkSpeed "34"
    LinkSpeedUnits "M"
    LinkLabel "34Mb/s"
    LinkSpeedRaw 34000000.0
  ]
  edge [
    source 4
    target 5
    LinkSpeed "34"
    LinkSpeedUnits "M"
    LinkLabel "34Mb/s"
    LinkSpeedRaw 34000000.0
  ]
  edge [
    source 5
    target 7
    LinkSpeed "155"
    LinkSpeedUnits "M"
    LinkLabel "155 Mb/s"
    LinkSpeedRaw 155000000.0
  ]
  edge [
    source 6
    target 7
    LinkSpeed "2"
    LinkSpeedUnits "M"
    LinkLabel "2Mb/s"
    LinkSpeedRaw 2000000.0
  ]
  edge [
    source 7
    target 8
    LinkType "MPLS"
    LinkLabel "MPLS"
  ]
  edge [
    source 7
    target 8
    LinkType "MPLS"
    LinkLabel "MPLS"
  ]
  edge [
    source 7
    target 10
    LinkSpeed "155"
    LinkSpeedUnits "M"
    LinkLabel "155Mb/s"
    LinkSpeedRaw 155000000.0
  ]
  edge [
    source 8
    target 9
    LinkSpeed "155"
    LinkSpeedUnits "M"
    LinkLabel "155Mb/s"
    LinkSpeedRaw 155000000.0
  ]
  edge [
    source 9
    target 10
    LinkType "ATM"
    LinkLabel "ATM"
  ]
  edge [
    source 9
    target 14
    LinkType "ATM"
    LinkLabel "ATM"
  ]
  edge [
    source 10
    target 11
    LinkType "ATM"
    LinkLabel "ATM"
  ]
  edge [
    source 11
    target 12
    LinkType "ATM"
    LinkLabel "ATM"
  ]
  edge [
    source 11
    target 15
    LinkSpeed "34"
    LinkSpeedUnits "M"
    LinkLabel "34Mb/s"
    LinkSpeedRaw 34000000.0
  ]
  edge [
    source 12
    target 13
    LinkType "ATM"
    LinkLabel "ATM"
  ]
  edge [
    source 13
    target 14
    LinkType "ATM"
    LinkLabel "ATM"
  ]
]
