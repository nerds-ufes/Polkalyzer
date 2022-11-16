graph [
  DateObtained "21/10/10"
  GeoLocation "Israel"
  GeoExtent "Country"
  SvnVersion 8043
  Customer 1
  Network "ILAN"
  Classification "Backbone Customer"
  Creator "Topology Zoo Toolset"
  LastAccess "21/10/10"
  Transit 0
  Backbone 1
  Commercial 0
  Layer "IP"
  NetworkDate "2008"
  Access 0
  Source "http://www.iucc.ac.il/eng/info/units/Ilan2.htm"
  Version "1.0"
  Testbed 0
  Developed "developed"
  label "ILAN"
  Type "REN"
  node [
    id 0
    label "Open University"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 1
    label "Haifa University"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 2
    label "Technion"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 3
    label "Bar Ilan University"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 4
    label "Hebrew University"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 5
    label "Ben Gurion University"
    Internal 1
  ]
  node [
    id 6
    label "Weizmann Institute"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 7
    label "Tel Aviv University"
    Internal 1
    type "Purple Node"
  ]
  node [
    id 8
    label "External Users"
    Internal 0
  ]
  node [
    id 9
    label "GEANT 2 Germany"
    Internal 0
  ]
  node [
    id 10
    label "IIX"
    Internal 0
  ]
  node [
    id 11
    label "Petach Tikva GigaPoP"
    Internal 1
    type "Orange Node"
  ]
  node [
    id 12
    label "Tel Aviv GigaPoP"
    Internal 1
    type "Orange Node"
  ]
  node [
    id 13
    label "Int'l backup "
    Internal 1
    type "Orange Node"
  ]
  edge [
    source 0
    target 11
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 1
    target 11
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 1
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 2
    target 12
  ]
  edge [
    source 3
    target 11
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 3
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 4
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 5
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 6
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 7
    target 11
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 7
    target 12
    LinkLabel "300M-1Gb/s"
  ]
  edge [
    source 8
    target 11
  ]
  edge [
    source 9
    target 11
    LinkSpeed "2.5"
    LinkLabel "2.5Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 10
    target 11
  ]
  edge [
    source 12
    target 13
    LinkSpeed "600"
    LinkLabel "600Mb/s"
    LinkSpeedUnits "M"
  ]
]
