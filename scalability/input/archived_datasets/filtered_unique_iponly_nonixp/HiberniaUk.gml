graph [
  DateObtained "23/03/11"
  GeoLocation "UK"
  GeoExtent "Country"
  Customer 0
  Network "Hibernia Atlantic (UK)"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.hiberniaatlantic.com/UK_network.html"
  Version "1.0"
  Type "COM"
  LastAccess "23/03/11"
  Layer "IP"
  Classification "Backbone Transit"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 1
  Backbone 1
  Commercial 0
  NetworkDate "2011-03"
  label "hibernia_uk"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Cambridge"
    Internal 1
    Latitude 52.2
    Country "United Kingdom"
    type "Small Node"
    Longitude 0.11667
  ]
  node [
    id 1
    label "Peterborough"
    Internal 1
    Latitude 52.57364
    Country "United Kingdom"
    type "Small Node"
    Longitude -0.24777
  ]
  node [
    id 2
    label "Leicester"
    Internal 1
    Latitude 52.63333
    Country "United Kingdom"
    type "Small Node"
    Longitude -1.13333
  ]
  node [
    id 3
    label "Sheffield"
    Internal 1
    Latitude 53.38297
    Country "United Kingdom"
    type "Small Node"
    Longitude -1.4659
  ]
  node [
    id 4
    label "Leeds"
    Internal 1
    Latitude 53.79648
    Country "United Kingdom"
    type "Small Node"
    Longitude -1.54785
  ]
  node [
    id 5
    label "Bracewell"
    Internal 1
    Latitude 53.93225
    Country "United Kingdom"
    type "Small Node"
    Longitude -2.20958
  ]
  node [
    id 6
    label "Liverpool"
    Internal 1
    Latitude 53.41058
    Country "United Kingdom"
    type "Small Node"
    Longitude -2.97794
  ]
  node [
    id 7
    label "Birmingham"
    Internal 1
    Latitude 52.46667
    Country "United Kingdom"
    type "Small Node"
    Longitude -1.91667
  ]
  node [
    id 8
    label "Bristol"
    Internal 1
    Latitude 51.45
    Country "United Kingdom"
    type "Small Node"
    Longitude -2.58333
  ]
  node [
    id 9
    label "Reading"
    Internal 1
    Latitude 51.45625
    Country "United Kingdom"
    type "Small Node"
    Longitude -0.97113
  ]
  node [
    id 12
    label "Southport"
    Internal 1
    Latitude 53.64779
    Country "United Kingdom"
    type "Large Node"
    Longitude -3.00648
  ]
  node [
    id 13
    label "London"
    Internal 1
    Latitude 51.50853
    Country "United Kingdom"
    type "Large Node"
    Longitude -0.12574
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
    Internal 1
    Latitude 53.48095
    Country "United Kingdom"
    type "Large Node"
    Longitude -2.23743
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
