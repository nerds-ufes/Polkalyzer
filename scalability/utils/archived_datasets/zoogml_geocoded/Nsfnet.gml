graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Network "NSF"
  Provenance "Secondary"
  Access 0
  Source "http://www.nthelp.com/images/nsf.jpg"
  Version "1.0"
  DateType "Current"
  Type "REN"
  Backbone 1
  Commercial 0
  label "nsfnet"
  Customer 1
  IX 0
  LastAccess "14/01/11"
  Layer "IP"
  Classification "Backbone Transit Customer "
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 1
  NetworkDate "2011-01"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "NorthWestNet, Seattle"
    Country "United States"
    Longitude -122.33207
    Latitude 47.60621
  ]
  node [
    id 1
    label "BARRnet, Palo Alto"
    Country "United States"
    Longitude -122.14302
    Latitude 37.44188
  ]
  node [
    id 2
    label "San Diego Supercomputer Center"
    Country "United States"
    Longitude -117.15726
    Latitude 32.71533
  ]
  node [
    id 3
    label "Westnet, Salt Lake City"
    Country "United States"
    Longitude -111.89105
    Latitude 40.76078
  ]
  node [
    id 4
    label "NCAR, Boulder"
    Country "United States"
    Longitude -105.27055
    Latitude 40.01499
  ]
  node [
    id 5
    label "MIDnet, Lincoln, NE"
    Country "United States"
    Longitude -96.66696
    Latitude 40.8
  ]
  node [
    id 6
    label "NCSA, University of Illinois, Champaign"
    Country "United States"
    Longitude -88.24338
    Latitude 40.11642
  ]
  node [
    id 7
    label "Merit Univ of Michigan, Ann Arbor"
    Country "United States"
    Longitude -83.74088
    Latitude 42.27756
  ]
  node [
    id 8
    label "Pittsburgh Supercomputer Center"
    Country "United States"
    Longitude -79.99589
    Latitude 40.44062
  ]
  node [
    id 9
    label "Cornell Theory Center, Ithaca NY"
    Country "United States"
    Longitude -76.49661
    Latitude 42.44063
  ]
  node [
    id 10
    label "Jon Von Neumann Center, Princeton, NJ"
    Country "United States"
    Longitude -74.65905
    Latitude 40.34872
  ]
  node [
    id 11
    label "SURANET, Georgia Tech, Atlanta"
    Country "United States"
    Longitude -84.38798
    Latitude 33.749
  ]
  node [
    id 12
    label "SEQSUINET, Rice University, Houston"
    Country "United States"
    Longitude -95.36327
    Latitude 29.76328
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
