graph [
  DateObtained "20/10/10"
  GeoLocation "Azerbaijan"
  GeoExtent "Country"
  Customer 1
  Network "Azrena"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.azrena.org/about_en.htm"
  Version "1.0"
  Type "REN"
  LastAccess "20/10/10"
  Layer "IP"
  Classification "Backbone Customer"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2010-10"
  label "AZRENA"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Economical Uni"
    Internal 1
    type "Router"
  ]
  node [
    id 1
    label "Local ISP"
    Internal 0
  ]
  node [
    id 2
    label "Silk Highway"
    Internal 0
  ]
  node [
    id 3
    label "VSAT Station"
    Internal 1
    type "Router"
  ]
  node [
    id 4
    label "Technical Uni"
    Internal 1
  ]
  node [
    id 5
    label "RENASCENE"
    Internal 1
  ]
  node [
    id 6
    label "Architecture-Building Uni"
    Internal 1
  ]
  node [
    id 7
    label "Foreign Language Uni."
    Internal 1
  ]
  node [
    id 8
    label "Khazar Uni"
    Internal 1
  ]
  node [
    id 9
    label "NOC"
    Internal 1
    type "Router"
  ]
  node [
    id 10
    label "Wireless server"
    Internal 1
    type "Router"
  ]
  node [
    id 11
    label "Wireless router"
    Internal 1
    type "Router"
  ]
  node [
    id 12
    label ""
    Internal 1
    type "Switch"
  ]
  node [
    id 13
    label "Dialup server"
    Internal 1
    type "Switch"
  ]
  node [
    id 14
    label "ANAS users"
    Internal 0
  ]
  node [
    id 15
    label "Distribution switch"
    Internal 1
    type "Switch"
  ]
  node [
    id 16
    label "Geology"
    Internal 1
    type "Switch"
  ]
  node [
    id 17
    label "Physics"
    Internal 1
    type "Switch"
  ]
  node [
    id 18
    label "Information Tech."
    Internal 1
  ]
  node [
    id 19
    label "Baku Uni"
    Internal 1
  ]
  node [
    id 20
    label "Cybenetics"
    Internal 1
  ]
  node [
    id 21
    label "Shamsa Obs."
    Internal 1
  ]
  edge [
    source 0
    target 9
    LinkType "Serial"
    LinkLabel "serial"
  ]
  edge [
    source 1
    target 9
    LinkType "Serial"
    LinkLabel "serial"
  ]
  edge [
    source 1
    target 9
    LinkType "Serial"
    LinkLabel "Serial"
  ]
  edge [
    source 1
    target 9
    LinkType "Serial"
    LinkLabel "Serial"
  ]
  edge [
    source 2
    target 3
    LinkType "Serial"
    LinkLabel "serial"
  ]
  edge [
    source 3
    target 9
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 4
    target 10
    LinkType "Wireless"
    LinkLabel "wireless"
  ]
  edge [
    source 5
    target 10
    LinkType "Wireless"
    LinkLabel "Wireless"
  ]
  edge [
    source 6
    target 10
    LinkType "Wireless"
    LinkLabel "wireless"
  ]
  edge [
    source 7
    target 11
    LinkType "Wireless"
    LinkLabel "Wireless"
  ]
  edge [
    source 8
    target 11
    LinkType "Wireless"
    LinkLabel "wireless"
  ]
  edge [
    source 9
    target 12
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 10
    target 12
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 11
    target 12
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 12
    target 13
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 12
    target 15
    LinkType "Ethernet"
    LinkLabel "Ethernet"
  ]
  edge [
    source 13
    target 14
    LinkType "Serial"
    LinkLabel "Serial"
  ]
  edge [
    source 13
    target 14
    LinkType "Serial"
    LinkLabel "Serial"
  ]
  edge [
    source 13
    target 14
    LinkType "Serial"
    LinkLabel "Serial"
  ]
  edge [
    source 15
    target 16
    LinkType "Fiber"
    LinkLabel "fiber"
  ]
  edge [
    source 15
    target 17
    LinkType "Fiber"
    LinkLabel "fiber"
  ]
  edge [
    source 15
    target 18
    LinkType "Fiber"
    LinkLabel "fiber"
  ]
  edge [
    source 18
    target 19
    LinkType "Fiber"
    LinkLabel "fiber"
  ]
  edge [
    source 18
    target 20
    LinkType "Ethernet"
    LinkLabel "ethernet"
  ]
  edge [
    source 18
    target 21
    LinkType "Ethernet"
    LinkLabel "ethernet"
  ]
]
