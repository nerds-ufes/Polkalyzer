graph [
  DateObtained "22/10/10"
  GeoLocation "Beijing, China"
  GeoExtent "Metro"
  Customer 0
  Network "NSFCNET"
  IX 0
  Provenance "Primary"
  Note "Hard to tell if multiple POS OC-48 links"
  Source "http://www.cn.apan.net/nsfcmap.htm"
  Version "1.0"
  Type "REN"
  LastAccess "7/10/10"
  Access 0
  Layer "IP"
  Classification "Testbed Backbone"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2010-10"
  label "NSFCNET"
  Testbed 1
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "APAN/STAR"
    Internal 0
  ]
  node [
    id 1
    label "CERNET"
    Internal 0
  ]
  node [
    id 2
    label "Tsinghua Unviersity"
    Internal 1
    type "Router"
  ]
  node [
    id 3
    label "Natural Science Foundation of China"
    Internal 1
    type "Router"
  ]
  node [
    id 4
    label "Beijing University of Posts and Telecommunications"
    Internal 1
    type "Router"
  ]
  node [
    id 5
    label "Beijing University of Aeronautics and Astronautics"
    Internal 1
    type "Router"
  ]
  node [
    id 6
    label "China Academy of Sciences"
    Internal 1
    type "Router"
  ]
  node [
    id 7
    label "CSTNET"
    Internal 0
  ]
  node [
    id 8
    label "Peking University"
    Internal 1
    type "Router"
  ]
  node [
    id 9
    label "CERNET"
    Internal 0
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 2
    LinkLabel "GE"
  ]
  edge [
    source 2
    target 3
    LinkLabel "DPT ring"
  ]
  edge [
    source 2
    target 5
    LinkLabel "DPT Ring"
  ]
  edge [
    source 2
    target 6
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 2
    target 8
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 3
    target 4
    LinkLabel "DPT Ring"
  ]
  edge [
    source 4
    target 5
    LinkLabel "DPT Ring"
  ]
  edge [
    source 6
    target 8
    LinkType "OC-48"
    LinkLabel "POS OC-48"
    LinkNote "POS "
  ]
  edge [
    source 6
    target 7
    LinkLabel "GE"
  ]
]
