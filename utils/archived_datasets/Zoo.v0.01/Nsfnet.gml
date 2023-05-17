graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Network "NFS"
  Classification ""
  Creator "Topology Zoo Toolset"
  Developed "developed"
  Type "COM"
  Layer "IP"
  label "nsfnet"
  Source "http://www.nthelp.com/images/nsf.jpg"
  Version "1.0"
  NetworkDate "C"
  LastAccess "14/01/11"
  node [
    id 0
    label "NorthWestNet, Seattle"
  ]
  node [
    id 1
    label "BARRnet, Palo Alto"
  ]
  node [
    id 2
    label "San Diego Supercomputer Center"
  ]
  node [
    id 3
    label "Westnet, Salt Lake City"
  ]
  node [
    id 4
    label "NCAR, Boulder"
  ]
  node [
    id 5
    label "MIDnet, Lincoln, NE"
  ]
  node [
    id 6
    label "NCSA, University of Illinois, Champaign"
  ]
  node [
    id 7
    label "Merit Univ of Michigan, Ann Arbor"
  ]
  node [
    id 8
    label "Pittsburgh Supercomputer Center"
  ]
  node [
    id 9
    label "Cornell Theory Center, Ithaca NY"
  ]
  node [
    id 10
    label "Jon Von Neumann Center, Princeton, NJ"
  ]
  node [
    id 11
    label "SURANET, Georgia Tech, Atlanta"
  ]
  node [
    id 12
    label "SEQSUINET, Rice University, Houston"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 7
    LinkType "T1"
    LinkLabel "T1"
  ]
  edge [
    source 2
    target 12
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 4
    target 6
  ]
  edge [
    source 5
    target 6
  ]
  edge [
    source 6
    target 12
  ]
  edge [
    source 6
    target 7
  ]
  edge [
    source 7
    target 8
  ]
  edge [
    source 7
    target 9
  ]
  edge [
    source 9
    target 10
  ]
  edge [
    source 10
    target 11
  ]
  edge [
    source 11
    target 12
  ]
]
