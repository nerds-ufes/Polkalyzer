graph [
  DateObtained "22/10/10"
  GeoLocation "Tokyo, Japan"
  GeoExtent "Metro"
  SvnVersion 8043
  Customer 0
  Network "T-lex"
  Classification "Backbone Transit"
  Creator "Topology Zoo Toolset"
  LastAccess "3/08/10"
  Transit 1
  Backbone 1
  Commercial 0
  Layer "Layer 2"
  NetworkDate "C"
  Access 0
  Source "http://www.t-lex.net/"
  Version "1.0"
  Testbed 0
  Developed "developed"
  label "t-lex"
  Type "REN"
  node [
    id 0
    label "DR Data Reservoir"
    Internal 0
  ]
  node [
    id 1
    label "U-Tokyo akihabara"
    Internal 0
  ]
  node [
    id 2
    label "JGN2"
    Internal 0
  ]
  node [
    id 3
    label "APAN-JP AS7660"
    Internal 0
  ]
  node [
    id 4
    label "WIDE AS2500"
    Internal 0
  ]
  node [
    id 5
    label "ASCC/TW AS9264"
    Internal 0
  ]
  node [
    id 6
    label "BigIron 15000 AS23814"
    Internal 1
  ]
  node [
    id 7
    label "NetIron N140G AS23814"
    Internal 1
  ]
  node [
    id 8
    label "Cat 6500 AS23814"
    Internal 1
  ]
  node [
    id 9
    label "ONS-15454"
    Internal 1
  ]
  node [
    id 10
    label "Pacific NW Gigapop (Seattle, WA)"
    Internal 0
  ]
  node [
    id 11
    label "Future IEEAF Asian Extension"
    Internal 0
  ]
  edge [
    source 0
    target 7
  ]
  edge [
    source 1
    target 7
  ]
  edge [
    source 2
    target 7
  ]
  edge [
    source 3
    target 7
  ]
  edge [
    source 4
    target 7
  ]
  edge [
    source 5
    target 6
  ]
  edge [
    source 6
    target 9
  ]
  edge [
    source 6
    target 9
    LinkLabel "8*GbE"
  ]
  edge [
    source 6
    target 7
  ]
  edge [
    source 7
    target 8
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10GE"
    LinkNote "E"
  ]
  edge [
    source 7
    target 9
    LinkLabel "WANPHY"
  ]
  edge [
    source 8
    target 9
    LinkLabel "WANPHY"
  ]
  edge [
    source 8
    target 9
    LinkType "OC-48"
    LinkLabel "OC-48"
  ]
  edge [
    source 9
    target 10
    LinkType "OC-12"
    LinkLabel "OC-12"
  ]
  edge [
    source 9
    target 10
    LinkType "OC-192"
    LinkLabel "OC-192"
  ]
  edge [
    source 9
    target 11
    LinkType "OC-192"
    LinkLabel "OC-192 (Future)"
    LinkStatus "Future"
  ]
]
