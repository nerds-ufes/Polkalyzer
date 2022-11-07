graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Customer 1
  Network "NSF"
  IX 0
  Provenance "Secondary"
  Access 0
  Source "http://www.nthelp.com/images/nsf.jpg"
  Version "1.0"
  Type "REN"
  LastAccess "14/01/11"
  Layer "IP"
  Classification "Backbone Transit Customer "
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 1
  Backbone 1
  Commercial 0
  NetworkDate "2011-01"
  label "nsfnet"
  Testbed 0
  Developed 1
  SvnVersion 8123
  node [
    id 0
    label "NorthWestNet, Seattle"
    Latitude 47.60621
    Country "United States"
    Longitude -122.33207
  ]
  node [
    id 1
    label "BARRnet, Palo Alto"
    Latitude 37.44188
    Country "United States"
    Longitude -122.14302
  ]
  node [
    id 2
    label "San Diego Supercomputer Center"
    Latitude 32.71533
    Country "United States"
    Longitude -117.15726
  ]
  node [
    id 3
    label "Westnet, Salt Lake City"
    Latitude 40.76078
    Country "United States"
    Longitude -111.89105
  ]
  node [
    id 4
    label "NCAR, Boulder"
    Latitude 40.01499
    Country "United States"
    Longitude -105.27055
  ]
  node [
    id 5
    label "MIDnet, Lincoln, NE"
    Latitude 40.8
    Country "United States"
    Longitude -96.66696
  ]
  node [
    id 6
    label "NCSA, University of Illinois, Champaign"
    Latitude 40.11642
    Country "United States"
    Longitude -88.24338
  ]
  node [
    id 7
    label "Merit Univ of Michigan, Ann Arbor"
    Latitude 42.27756
    Country "United States"
    Longitude -83.74088
  ]
  node [
    id 8
    label "Pittsburgh Supercomputer Center"
    Latitude 40.44062
    Country "United States"
    Longitude -79.99589
  ]
  node [
    id 9
    label "Cornell Theory Center, Ithaca NY"
    Latitude 42.44063
    Country "United States"
    Longitude -76.49661
  ]
  node [
    id 10
    label "Jon Von Neumann Center, Princeton, NJ"
    Latitude 40.34872
    Country "United States"
    Longitude -74.65905
  ]
  node [
    id 11
    label "SURANET, Georgia Tech, Atlanta"
    Latitude 33.749
    Country "United States"
    Longitude -84.38798
  ]
  node [
    id 12
    label "SEQSUINET, Rice University, Houston"
    Latitude 29.76328
    Country "United States"
    Longitude -95.36327
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
