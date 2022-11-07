graph [
  DateObtained "23/03/11"
  GeoLocation "Ireland"
  GeoExtent "Country"
  Customer 0
  Network "Hibernia Atlantic (Ireland)"
  IX 0
  Provenance "Primary"
  Access 0
  Source "http://www.hiberniaatlantic.com/Ireland_network.html"
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
  label "hibernia_ireland"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Dublin"
    Internal 1
    Latitude 53.34399
    Country "Ireland"
    type "Large Node"
    Longitude -6.26719
  ]
  node [
    id 1
    label "Galway"
    Internal 1
    Latitude 53.27194
    Country "Ireland"
    type "Small Node"
    Longitude -9.04889
  ]
  node [
    id 2
    label "Limerick"
    Internal 1
    Latitude 52.66472
    Country "Ireland"
    type "Small Node"
    Longitude -8.62306
  ]
  node [
    id 3
    label "Cork"
    Internal 1
    Latitude 51.89861
    Country "Ireland"
    type "Small Node"
    Longitude -8.49583
  ]
  node [
    id 4
    label "Waterford"
    Internal 1
    Latitude 52.25833
    Country "Ireland"
    type "Small Node"
    Longitude -7.11194
  ]
  node [
    id 5
    label "Portlaioise"
    Internal 1
    Latitude 53.03441
    Country "Ireland"
    type "Small Node"
    Longitude -7.29979
  ]
  node [
    id 8
    label ""
    Internal 0
  ]
  node [
    id 9
    label ""
    Internal 0
  ]
  edge [
    source 0
    target 8
    LinkLabel "Green Link"
  ]
  edge [
    source 0
    target 9
    LinkLabel "Green Link"
  ]
  edge [
    source 0
    target 4
    LinkLabel "Blue Link"
  ]
  edge [
    source 0
    target 5
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
    source 2
    target 5
    LinkLabel "Blue Link"
  ]
  edge [
    source 3
    target 4
    LinkLabel "Blue Link"
  ]
]
