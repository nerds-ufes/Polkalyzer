graph [
  DateObtained "19/10/10"
  GeoLocation "Austria"
  GeoExtent "Country"
  Network "ACOnet"
  Note "Vienna is unclear - Internal links show which of two internal PoPs they connect to, but external links not clear."
  Source "http://www.aco.net/ueberblick.html?&amp;L=1"
  Version "1.0"
  Type "REN"
  Backbone 1
  Commercial 0
  label "ACONET"
  Customer 0
  LastAccess "19/10/10"
  Access 0
  Layer "IP"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  Developed ""
  Transit 0
  NetworkDate "1/06/09"
  Testbed 0
  SvnVersion 8043
  node [
    id 0
    label "Linz1"
    Internal 1
  ]
  node [
    id 1
    label "Linz2"
    Internal 1
  ]
  node [
    id 2
    label "Salzburg1"
    Internal 1
  ]
  node [
    id 3
    label "Salzburg2"
    Internal 1
  ]
  node [
    id 4
    label "Innsbruck1"
    Internal 1
  ]
  node [
    id 5
    label "Innsbruck2"
    Internal 1
  ]
  node [
    id 6
    label "Dornbirn"
    Internal 1
  ]
  node [
    id 7
    label "Klagenfurt1"
    Internal 1
  ]
  node [
    id 8
    label "Klagenfurt2"
    Internal 1
  ]
  node [
    id 9
    label "Graz1"
    Internal 1
  ]
  node [
    id 10
    label "Graz2"
    Internal 1
  ]
  node [
    id 11
    label "Leoben"
    Internal 1
  ]
  node [
    id 12
    label "Eisenstadt"
    Internal 1
  ]
  node [
    id 13
    label "St. Polter"
    Internal 1
  ]
  node [
    id 14
    label "Krems"
    Internal 1
  ]
  node [
    id 15
    label "Vienna1"
    Internal 1
  ]
  node [
    id 16
    label "Vienna2"
    Internal 1
  ]
  node [
    id 17
    label "GEANT"
    Internal 0
  ]
  node [
    id 18
    label "Level3"
    Internal 0
  ]
  node [
    id 19
    label "VIX"
    Internal 0
  ]
  node [
    id 20
    label "CESNET"
    Internal 0
  ]
  node [
    id 21
    label "SANET"
    Internal 0
  ]
  node [
    id 22
    label "Vienna"
    Internal 1
    doubted 1
  ]
  edge [
    source 0
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 0
    target 1
    LinkLabel "DWDM"
  ]
  edge [
    source 1
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 2
    target 3
    LinkLabel "DWDM"
  ]
  edge [
    source 2
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 3
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 5
    LinkLabel "DWDM"
  ]
  edge [
    source 4
    target 6
    LinkLabel "DWDM"
  ]
  edge [
    source 5
    target 6
    LinkLabel "DWDM"
  ]
  edge [
    source 5
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 7
    target 8
    LinkLabel "DWDM"
  ]
  edge [
    source 7
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 8
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 9
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 9
    target 10
    LinkLabel "DWDM"
  ]
  edge [
    source 9
    target 11
    LinkLabel "DWDM"
  ]
  edge [
    source 10
    target 11
    LinkLabel "DWDM"
  ]
  edge [
    source 10
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 12
    target 16
    LinkLabel "DWDM"
  ]
  edge [
    source 12
    target 15
    LinkLabel "DWDM"
  ]
  edge [
    source 13
    target 14
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 13
    target 15
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 14
    target 16
    LinkType "Ethernet"
    LinkSpeed "1"
    LinkLabel "1G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 15
    target 22
  ]
  edge [
    source 16
    target 22
  ]
  edge [
    source 17
    target 22
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 18
    target 22
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 19
    target 22
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 20
    target 22
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
  ]
  edge [
    source 21
    target 22
    LinkType "Ethernet"
    LinkSpeed "10"
    LinkLabel "10G Ethernet"
    LinkSpeedUnits "G"
  ]
]
