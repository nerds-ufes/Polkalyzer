graph [
  DateObtained "23/03/11"
  GeoLocation "Canada"
  GeoExtent "Country"
  Customer 0
  Network "Hibernia Atlantic (Canada)"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.hiberniaatlantic.com/Canada_network.html"
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
  label "hibernia_canada"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Edmundston"
    Internal 1
    Latitude 47.3737
    Country "Canada"
    type "Green Node"
    Longitude -68.32512
  ]
  node [
    id 1
    label "Quebec"
    Internal 1
    Latitude 46.81228
    Country "Canada"
    type "Green Node"
    Longitude -71.21454
  ]
  node [
    id 2
    label "Montreal"
    Internal 1
    Latitude 45.50884
    Country "Canada"
    type "Green Node"
    Longitude -73.58781
  ]
  node [
    id 3
    label "Toronto"
    Internal 1
    Latitude 43.70011
    Country "Canada"
    type "Green Node"
    Longitude -79.4163
  ]
  node [
    id 4
    label "Buffalo"
    Internal 1
    Latitude 55.85017
    Country "Canada"
    type "Green Node"
    Longitude -108.48475
  ]
  node [
    id 5
    label "Albany"
    Internal 1
    Latitude 46.28343
    Country "Canada"
    type "Green Node"
    Longitude -63.64872
  ]
  node [
    id 6
    label "Boston"
    Internal 1
    Latitude 49.87002
    Country "Canada"
    type "Green Node"
    Longitude -121.44399
  ]
  node [
    id 7
    label "Halifax"
    Internal 1
    Latitude 44.646
    Country "Canada"
    type "Green Node"
    Longitude -63.57333
  ]
  node [
    id 8
    label "Moncton"
    Internal 1
    Latitude 46.11594
    Country "Canada"
    type "Green Node"
    Longitude -64.80186
  ]
  node [
    id 9
    label ""
    hyperedge 1
    Internal 1
  ]
  node [
    id 10
    label ""
    Internal 0
  ]
  node [
    id 11
    label ""
    Internal 0
  ]
  node [
    id 12
    label "New York"
    Internal 1
    Latitude 43.08342
    Country "Canada"
    type "Yellow Node"
    Longitude -79.06627
  ]
  edge [
    source 0
    target 8
    LinkLabel "Green Link"
  ]
  edge [
    source 0
    target 1
    LinkLabel "Green Link"
  ]
  edge [
    source 1
    target 2
    LinkLabel "Green Link"
  ]
  edge [
    source 2
    target 3
    LinkLabel "Green Link"
  ]
  edge [
    source 2
    target 5
    LinkLabel "Green Link"
  ]
  edge [
    source 3
    target 4
    LinkLabel "Green Link"
  ]
  edge [
    source 4
    target 5
    LinkLabel "Green Link"
  ]
  edge [
    source 5
    target 12
    LinkLabel "Green Link"
  ]
  edge [
    source 6
    target 9
    LinkLabel "Blue Link"
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
    target 9
    LinkLabel "Blue Link"
  ]
  edge [
    source 7
    target 11
    LinkLabel "Blue Link"
  ]
  edge [
    source 9
    target 10
    LinkLabel "Blue Link"
  ]
]
