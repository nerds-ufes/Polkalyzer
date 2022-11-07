graph [
  DateObtained "21/10/10"
  GeoLocation "Israel"
  GeoExtent "Country"
  Customer 1
  Network "ILAN"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.iucc.ac.il/eng/info/units/Ilan2.htm"
  Version "1.0"
  Type "REN"
  LastAccess "21/10/10"
  Layer "IP"
  Classification "Backbone Customer"
  Creator "Topology Zoo Toolset"
  DateType "Historic"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2008"
  label "ILAN"
  Testbed 0
  Developed 1
  SvnVersion 8123
  node [
    id 0
    label "Open University"
    Internal 1
    Latitude 32.18333
    Country "Israel"
    type "Purple Node"
    Longitude 34.86667
  ]
  node [
    id 1
    label "Haifa University"
    Internal 1
    Latitude 32.81556
    Country "Israel"
    type "Purple Node"
    Longitude 34.98917
  ]
  node [
    id 2
    label "Technion"
    Internal 1
    Latitude 32.81556
    Country "Israel"
    type "Purple Node"
    Longitude 34.98917
  ]
  node [
    id 3
    label "Bar Ilan University"
    Internal 1
    Latitude 32.08056
    Country "Israel"
    type "Purple Node"
    Longitude 34.81417
  ]
  node [
    id 4
    label "Hebrew University"
    Internal 1
    Latitude 31.77902
    Country "Israel"
    type "Purple Node"
    Longitude 35.2253
  ]
  node [
    id 5
    label "Ben Gurion University"
    Internal 1
    Latitude 29.56111
    Country "Israel"
    Longitude 34.95167
  ]
  node [
    id 6
    label "Weizmann Institute"
    Internal 1
    Latitude 31.89694
    Country "Israel"
    type "Purple Node"
    Longitude 34.81861
  ]
  node [
    id 7
    label "Tel Aviv University"
    Internal 1
    Latitude 32.06667
    Country "Israel"
    type "Purple Node"
    Longitude 34.76667
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
    Latitude 32.09174
    Country "Israel"
    type "Orange Node"
    Longitude 34.88503
  ]
  node [
    id 12
    label "Tel Aviv GigaPoP"
    Internal 1
    Latitude 32.06667
    Country "Israel"
    type "Orange Node"
    Longitude 34.76667
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
    LinkLabel "2.5Gb/s"
    LinkSpeedUnits "G"
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
    LinkLabel "600Mb/s"
    LinkSpeedUnits "M"
    LinkSpeedRaw 600000000.0
  ]
]
