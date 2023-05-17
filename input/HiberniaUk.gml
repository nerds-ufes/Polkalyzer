graph [
  DateObtained "23/03/11"
  GeoLocation "UK"
  GeoExtent "Country"
  Network "Hibernia Atlantic (UK)"
  Provenance "Primary"
  Access 0
  Source "http://www.hiberniaatlantic.com/UK_network.html"
  Version "1.0"
  DateType "Current"
  Type "COM"
  Backbone 1
  Commercial 0
  label "hibernia_uk"
  Customer 0
  IX 0
  LastAccess "23/03/11"
  Layer "IP"
  Classification "Backbone Transit"
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 1
  NetworkDate "2011-03"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Cambridge"
    Country "United Kingdom"
    Longitude 0.11667
    Internal 1
    Latitude 52.2
    type "Small Node"
  ]
  node [
    id 1
    label "Peterborough"
    Country "United Kingdom"
    Longitude -0.24777
    Internal 1
    Latitude 52.57364
    type "Small Node"
  ]
  node [
    id 2
    label "Leicester"
    Country "United Kingdom"
    Longitude -1.13333
    Internal 1
    Latitude 52.63333
    type "Small Node"
  ]
  node [
    id 3
    label "Sheffield"
    Country "United Kingdom"
    Longitude -1.4659
    Internal 1
    Latitude 53.38297
    type "Small Node"
  ]
  node [
    id 4
    label "Leeds"
    Country "United Kingdom"
    Longitude -1.54785
    Internal 1
    Latitude 53.79648
    type "Small Node"
  ]
  node [
    id 5
    label "Bracewell"
    Country "United Kingdom"
    Longitude -2.20958
    Internal 1
    Latitude 53.93225
    type "Small Node"
  ]
  node [
    id 6
    label "Liverpool"
    Country "United Kingdom"
    Longitude -2.97794
    Internal 1
    Latitude 53.41058
    type "Small Node"
  ]
  node [
    id 7
    label "Birmingham"
    Country "United Kingdom"
    Longitude -1.91667
    Internal 1
    Latitude 52.46667
    type "Small Node"
  ]
  node [
    id 8
    label "Bristol"
    Country "United Kingdom"
    Longitude -2.58333
    Internal 1
    Latitude 51.45
    type "Small Node"
  ]
  node [
    id 9
    label "Reading"
    Country "United Kingdom"
    Longitude -0.97113
    Internal 1
    Latitude 51.45625
    type "Small Node"
  ]
  node [
    id 12
    label "Southport"
    Country "United Kingdom"
    Longitude -3.00648
    Internal 1
    Latitude 53.64779
    type "Large Node"
  ]
  node [
    id 13
    label "London"
    Country "United Kingdom"
    Longitude -0.12574
    Internal 1
    Latitude 51.50853
    type "Large Node"
  ]
  node [
    id 14
    label ""
    Internal 0
  ]
  node [
    id 15
    label ""
    Internal 0
  ]
  node [
    id 16
    label "Manchester"
    Country "United Kingdom"
    Longitude -2.23743
    Internal 1
    Latitude 53.48095
    type "Large Node"
  ]
  edge [
    source 0
    target 1
    LinkLabel "Blue Link"
  ]
  edge [
    source 0
    target 13
    LinkLabel "Blue Link"
  ]
  edge [
    source 1
    target 2
    LinkLabel "Blue Link"
  ]
  edge [
    source 2
    target 3
    LinkLabel "Blue Link"
  ]
  edge [
    source 3
    target 4
    LinkLabel "Blue Link"
  ]
  edge [
    source 4
    target 5
    LinkLabel "Blue Link"
  ]
  edge [
    source 5
    target 12
    LinkLabel "Blue Link"
  ]
  edge [
    source 6
    target 16
    LinkLabel "Green Link"
  ]
  edge [
    source 6
    target 12
    LinkLabel "Green Link"
  ]
  edge [
    source 7
    target 8
    LinkLabel "Green Link"
  ]
  edge [
    source 7
    target 16
    LinkLabel "Green Link"
  ]
  edge [
    source 8
    target 9
    LinkLabel "Green Link"
  ]
  edge [
    source 9
    target 13
    LinkLabel "Green Link"
  ]
  edge [
    source 9
    target 15
    LinkLabel "Green Link"
  ]
  edge [
    source 13
    target 14
    LinkLabel "Blue Link"
  ]
]
