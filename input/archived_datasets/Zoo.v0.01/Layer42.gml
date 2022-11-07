graph [
  DateObtained "16/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Network "Layer42"
  Classification ""
  Creator "Topology Zoo Toolset"
  Developed "developed"
  Type "COM"
  Layer "IP"
  label "layer_42"
  Source "http://www.layer42.net/network/national.html"
  Version "1.0"
  NetworkDate "C"
  LastAccess "16/01/11"
  node [
    id 0
    label "Seattle"
  ]
  node [
    id 1
    label "San Francisco"
  ]
  node [
    id 2
    label "Los Angeles"
  ]
  node [
    id 3
    label "Chicago"
  ]
  node [
    id 4
    label "New York City"
  ]
  node [
    id 5
    label "Washington DC"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 4
    target 5
  ]
]
