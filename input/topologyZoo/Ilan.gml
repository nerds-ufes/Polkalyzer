graph [
  DateObtained "21/10/10"
  GeoLocation "Israel"
  GeoExtent "Country"
  Network "ILAN"
  Provenance "Primary"
  Access 0
  Source "http://www.iucc.ac.il/eng/info/units/Ilan2.htm"
  Version "1.0"
  DateType "Historic"
  Type "REN"
  Backbone 1
  Commercial 0
  label "ILAN"
  Customer 1
  IX 0
  LastAccess "21/10/10"
  Layer "IP"
  Classification "Backbone Customer"
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 0
  NetworkDate "2008"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Open University"
    Country "Israel"
    Longitude 34.86667
    Internal 1
    Latitude 32.18333
    type "Purple Node"
  ]
  node [
    id 1
    label "Haifa University"
    Country "Israel"
    Longitude 34.98917
    Internal 1
    Latitude 32.81556
    type "Purple Node"
  ]
  node [
    id 2
    label "Technion"
    Country "Israel"
    Longitude 34.98917
    Internal 1
    Latitude 32.81556
    type "Purple Node"
  ]
  node [
    id 3
    label "Bar Ilan University"
    Country "Israel"
    Longitude 34.81417
    Internal 1
    Latitude 32.08056
    type "Purple Node"
  ]
  node [
    id 4
    label "Hebrew University"
    Country "Israel"
    Longitude 35.2253
    Internal 1
    Latitude 31.77902
    type "Purple Node"
  ]
  node [
    id 5
    label "Ben Gurion University"
    Country "Israel"
    Longitude 34.95167
    Internal 1
    Latitude 29.56111
  ]
  node [
    id 6
    label "Weizmann Institute"
    Country "Israel"
    Longitude 34.81861
    Internal 1
    Latitude 31.89694
    type "Purple Node"
  ]
  node [
    id 7
    label "Tel Aviv University"
    Country "Israel"
    Longitude 34.76667
    Internal 1
    Latitude 32.06667
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
    Country "Israel"
    Longitude 34.88503
    Internal 1
    Latitude 32.09174
    type "Orange Node"
  ]
  node [
    id 12
    label "Tel Aviv GigaPoP"
    Country "Israel"
    Longitude 34.76667
    Internal 1
    Latitude 32.06667
    type "Orange Node"
  ]
  node [
    id 13
    label "Int'l backup "
    Internal 0
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
    LinkSpeedUnits "G"
    LinkLabel "2.5Gb/s"
    LinkSpeedRaw 2500000000.0
  ]
  edge [
    source 10
    target 11
  ]
  edge [
    source 12
    target 13
    LinkSpeed "600"
    LinkSpeedUnits "M"
    LinkLabel "600Mb/s"
    LinkSpeedRaw 600000000.0
  ]
]
