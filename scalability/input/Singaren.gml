graph [
  DateObtained "22/10/10"
  GeoLocation "Singapore"
  GeoExtent "Country"
  Network "Singaren"
  Provenance "Primary"
  Access 0
  Source "http://www.singaren.net.sg/network.php"
  Version "1.0"
  DateType "Historic"
  Type "REN"
  Backbone 1
  Commercial 0
  label "SingAREN"
  Customer 0
  IX 1
  LastAccess "3/08/10"
  Layer "IP"
  Classification "Backbone IX"
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 0
  NetworkDate "2008"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "NTU"
    Internal 1
  ]
  node [
    id 1
    label "Biopolis"
    Internal 1
  ]
  node [
    id 2
    label "Fusionopolis"
    Internal 1
  ]
  node [
    id 3
    label "NUS"
    Internal 1
  ]
  node [
    id 4
    label "Schools"
    Internal 1
  ]
  node [
    id 5
    label "SingAREN members"
    Internal 1
  ]
  node [
    id 6
    label "SingAREN-GIX"
    Internal 1
  ]
  node [
    id 7
    label "TEIN3"
    Internal 0
  ]
  node [
    id 8
    label "AARNET"
    Internal 0
  ]
  node [
    id 9
    label "Academia Sinica Taiwan"
    Internal 0
  ]
  node [
    id 10
    label "NICT QGPOP APAN-JP Japan"
    Internal 0
  ]
  edge [
    source 0
    target 6
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 1
    target 6
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 2
    target 6
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 3
    target 6
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 4
    target 6
  ]
  edge [
    source 5
    target 6
    LinkLabel "GigE/FE/ATM"
  ]
  edge [
    source 6
    target 7
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 6
    target 8
    LinkType "Gige"
    LinkLabel "GigE"
  ]
  edge [
    source 6
    target 9
    LinkType "STM-1"
    LinkNote "IPLC "
    LinkLabel "IPLC STM-1"
  ]
  edge [
    source 6
    target 10
    LinkType "STM-1"
    LinkNote "IPLC "
    LinkLabel "IPLC STM-1"
  ]
]
