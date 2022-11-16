graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Network "NapNet"
  Classification ""
  Creator "Topology Zoo Toolset"
  Developed "developed"
  Type "COM"
  Layer "IP"
  label "napnet"
  Source "http://www.nthelp.com/images/napnet.jpg"
  Version "1.0"
  NetworkDate "C"
  LastAccess "14/01/11"
  node [
    id 0
    label "Seattle"
  ]
  node [
    id 1
    label "San Jose"
  ]
  node [
    id 2
    label "Minneapolis"
  ]
  node [
    id 3
    label "Chicago"
  ]
  node [
    id 4
    label "Vienna"
  ]
  node [
    id 5
    label "Dallas"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 4
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 5
  ]
]
