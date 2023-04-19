from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Set Here Default Parameters
		switchParameters= {}
		hostParameters= {}
		linkHSParameters= {}
		linkSSParameters= {}
		#Add Switches
		s0 = self.addSwitch('s0',**switchParameters)
		s1 = self.addSwitch('s1',**switchParameters)
		s2 = self.addSwitch('s2',**switchParameters)
		s3 = self.addSwitch('s3',**switchParameters)
		s4 = self.addSwitch('s4',**switchParameters)
		s5 = self.addSwitch('s5',**switchParameters)
		s6 = self.addSwitch('s6',**switchParameters)
		s7 = self.addSwitch('s7',**switchParameters)
		s8 = self.addSwitch('s8',**switchParameters)
		s9 = self.addSwitch('s9',**switchParameters)
		s10 = self.addSwitch('s10',**switchParameters)
		s11 = self.addSwitch('s11',**switchParameters)
		s12 = self.addSwitch('s12',**switchParameters)
		s13 = self.addSwitch('s13',**switchParameters)
		s14 = self.addSwitch('s14',**switchParameters)
		s15 = self.addSwitch('s15',**switchParameters)
		s16 = self.addSwitch('s16',**switchParameters)
		s17 = self.addSwitch('s17',**switchParameters)
		s18 = self.addSwitch('s18',**switchParameters)
		s19 = self.addSwitch('s19',**switchParameters)
		s20 = self.addSwitch('s20',**switchParameters)
		s21 = self.addSwitch('s21',**switchParameters)
		s22 = self.addSwitch('s22',**switchParameters)
		s23 = self.addSwitch('s23',**switchParameters)
		s24 = self.addSwitch('s24',**switchParameters)
		s25 = self.addSwitch('s25',**switchParameters)
		s26 = self.addSwitch('s26',**switchParameters)
		s27 = self.addSwitch('s27',**switchParameters)
		s28 = self.addSwitch('s28',**switchParameters)
		s29 = self.addSwitch('s29',**switchParameters)
		s30 = self.addSwitch('s30',**switchParameters)
		s31 = self.addSwitch('s31',**switchParameters)
		s32 = self.addSwitch('s32',**switchParameters)
		s33 = self.addSwitch('s33',**switchParameters)
		s34 = self.addSwitch('s34',**switchParameters)
		s35 = self.addSwitch('s35',**switchParameters)
		s36 = self.addSwitch('s36',**switchParameters)
		s37 = self.addSwitch('s37',**switchParameters)
		s38 = self.addSwitch('s38',**switchParameters)
		s39 = self.addSwitch('s39',**switchParameters)
		s40 = self.addSwitch('s40',**switchParameters)
		s41 = self.addSwitch('s41',**switchParameters)
		s42 = self.addSwitch('s42',**switchParameters)
		s43 = self.addSwitch('s43',**switchParameters)
		s44 = self.addSwitch('s44',**switchParameters)
		s45 = self.addSwitch('s45',**switchParameters)
		s46 = self.addSwitch('s46',**switchParameters)
		s47 = self.addSwitch('s47',**switchParameters)
		s48 = self.addSwitch('s48',**switchParameters)
		s49 = self.addSwitch('s49',**switchParameters)
		s50 = self.addSwitch('s50',**switchParameters)
		s51 = self.addSwitch('s51',**switchParameters)
		s52 = self.addSwitch('s52',**switchParameters)
		s53 = self.addSwitch('s53',**switchParameters)
		s54 = self.addSwitch('s54',**switchParameters)
		s55 = self.addSwitch('s55',**switchParameters)
		s56 = self.addSwitch('s56',**switchParameters)
		s57 = self.addSwitch('s57',**switchParameters)
		s58 = self.addSwitch('s58',**switchParameters)
		s59 = self.addSwitch('s59',**switchParameters)
		s60 = self.addSwitch('s60',**switchParameters)
		s61 = self.addSwitch('s61',**switchParameters)
		s62 = self.addSwitch('s62',**switchParameters)
		s63 = self.addSwitch('s63',**switchParameters)
		s64 = self.addSwitch('s64',**switchParameters)
		s65 = self.addSwitch('s65',**switchParameters)
		s66 = self.addSwitch('s66',**switchParameters)
		s67 = self.addSwitch('s67',**switchParameters)
		s68 = self.addSwitch('s68',**switchParameters)
		s69 = self.addSwitch('s69',**switchParameters)
		s70 = self.addSwitch('s70',**switchParameters)
		s71 = self.addSwitch('s71',**switchParameters)
		s72 = self.addSwitch('s72',**switchParameters)
		s73 = self.addSwitch('s73',**switchParameters)
		s74 = self.addSwitch('s74',**switchParameters)
		s75 = self.addSwitch('s75',**switchParameters)
		s76 = self.addSwitch('s76',**switchParameters)
		s77 = self.addSwitch('s77',**switchParameters)
		s78 = self.addSwitch('s78',**switchParameters)
		s79 = self.addSwitch('s79',**switchParameters)
		s80 = self.addSwitch('s80',**switchParameters)
		s81 = self.addSwitch('s81',**switchParameters)
		s82 = self.addSwitch('s82',**switchParameters)
		s83 = self.addSwitch('s83',**switchParameters)
		s84 = self.addSwitch('s84',**switchParameters)
		s85 = self.addSwitch('s85',**switchParameters)
		s86 = self.addSwitch('s86',**switchParameters)
		s89 = self.addSwitch('s89',**switchParameters)
		s90 = self.addSwitch('s90',**switchParameters)
		s91 = self.addSwitch('s91',**switchParameters)
		s92 = self.addSwitch('s92',**switchParameters)
		s93 = self.addSwitch('s93',**switchParameters)
		#Add 1 hosts to each switch
		h0 = self.addHost('h0',**hostParameters)
		h1 = self.addHost('h1',**hostParameters)
		h2 = self.addHost('h2',**hostParameters)
		h3 = self.addHost('h3',**hostParameters)
		h4 = self.addHost('h4',**hostParameters)
		h5 = self.addHost('h5',**hostParameters)
		h6 = self.addHost('h6',**hostParameters)
		h7 = self.addHost('h7',**hostParameters)
		h8 = self.addHost('h8',**hostParameters)
		h9 = self.addHost('h9',**hostParameters)
		h10 = self.addHost('h10',**hostParameters)
		h11 = self.addHost('h11',**hostParameters)
		h12 = self.addHost('h12',**hostParameters)
		h13 = self.addHost('h13',**hostParameters)
		h14 = self.addHost('h14',**hostParameters)
		h15 = self.addHost('h15',**hostParameters)
		h16 = self.addHost('h16',**hostParameters)
		h17 = self.addHost('h17',**hostParameters)
		h18 = self.addHost('h18',**hostParameters)
		h19 = self.addHost('h19',**hostParameters)
		h20 = self.addHost('h20',**hostParameters)
		h21 = self.addHost('h21',**hostParameters)
		h22 = self.addHost('h22',**hostParameters)
		h23 = self.addHost('h23',**hostParameters)
		h24 = self.addHost('h24',**hostParameters)
		h25 = self.addHost('h25',**hostParameters)
		h26 = self.addHost('h26',**hostParameters)
		h27 = self.addHost('h27',**hostParameters)
		h28 = self.addHost('h28',**hostParameters)
		h29 = self.addHost('h29',**hostParameters)
		h30 = self.addHost('h30',**hostParameters)
		h31 = self.addHost('h31',**hostParameters)
		h32 = self.addHost('h32',**hostParameters)
		h33 = self.addHost('h33',**hostParameters)
		h34 = self.addHost('h34',**hostParameters)
		h35 = self.addHost('h35',**hostParameters)
		h36 = self.addHost('h36',**hostParameters)
		h37 = self.addHost('h37',**hostParameters)
		h38 = self.addHost('h38',**hostParameters)
		h39 = self.addHost('h39',**hostParameters)
		h40 = self.addHost('h40',**hostParameters)
		h41 = self.addHost('h41',**hostParameters)
		h42 = self.addHost('h42',**hostParameters)
		h43 = self.addHost('h43',**hostParameters)
		h44 = self.addHost('h44',**hostParameters)
		h45 = self.addHost('h45',**hostParameters)
		h46 = self.addHost('h46',**hostParameters)
		h47 = self.addHost('h47',**hostParameters)
		h48 = self.addHost('h48',**hostParameters)
		h49 = self.addHost('h49',**hostParameters)
		h50 = self.addHost('h50',**hostParameters)
		h51 = self.addHost('h51',**hostParameters)
		h52 = self.addHost('h52',**hostParameters)
		h53 = self.addHost('h53',**hostParameters)
		h54 = self.addHost('h54',**hostParameters)
		h55 = self.addHost('h55',**hostParameters)
		h56 = self.addHost('h56',**hostParameters)
		h57 = self.addHost('h57',**hostParameters)
		h58 = self.addHost('h58',**hostParameters)
		h59 = self.addHost('h59',**hostParameters)
		h60 = self.addHost('h60',**hostParameters)
		h61 = self.addHost('h61',**hostParameters)
		h62 = self.addHost('h62',**hostParameters)
		h63 = self.addHost('h63',**hostParameters)
		h64 = self.addHost('h64',**hostParameters)
		h65 = self.addHost('h65',**hostParameters)
		h66 = self.addHost('h66',**hostParameters)
		h67 = self.addHost('h67',**hostParameters)
		h68 = self.addHost('h68',**hostParameters)
		h69 = self.addHost('h69',**hostParameters)
		h70 = self.addHost('h70',**hostParameters)
		h71 = self.addHost('h71',**hostParameters)
		h72 = self.addHost('h72',**hostParameters)
		h73 = self.addHost('h73',**hostParameters)
		h74 = self.addHost('h74',**hostParameters)
		h75 = self.addHost('h75',**hostParameters)
		h76 = self.addHost('h76',**hostParameters)
		h77 = self.addHost('h77',**hostParameters)
		h78 = self.addHost('h78',**hostParameters)
		h79 = self.addHost('h79',**hostParameters)
		h80 = self.addHost('h80',**hostParameters)
		h81 = self.addHost('h81',**hostParameters)
		h82 = self.addHost('h82',**hostParameters)
		h83 = self.addHost('h83',**hostParameters)
		h84 = self.addHost('h84',**hostParameters)
		h85 = self.addHost('h85',**hostParameters)
		h86 = self.addHost('h86',**hostParameters)
		h87 = self.addHost('h87',**hostParameters)
		h88 = self.addHost('h88',**hostParameters)
		h89 = self.addHost('h89',**hostParameters)
		h90 = self.addHost('h90',**hostParameters)
		h91 = self.addHost('h91',**hostParameters)
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0',**linkHSParameters)
		lhs1 = self.addLink('s1','h1',**linkHSParameters)
		lhs2 = self.addLink('s2','h2',**linkHSParameters)
		lhs3 = self.addLink('s3','h3',**linkHSParameters)
		lhs4 = self.addLink('s4','h4',**linkHSParameters)
		lhs5 = self.addLink('s5','h5',**linkHSParameters)
		lhs6 = self.addLink('s6','h6',**linkHSParameters)
		lhs7 = self.addLink('s7','h7',**linkHSParameters)
		lhs8 = self.addLink('s8','h8',**linkHSParameters)
		lhs9 = self.addLink('s9','h9',**linkHSParameters)
		lhs10 = self.addLink('s10','h10',**linkHSParameters)
		lhs11 = self.addLink('s11','h11',**linkHSParameters)
		lhs12 = self.addLink('s12','h12',**linkHSParameters)
		lhs13 = self.addLink('s13','h13',**linkHSParameters)
		lhs14 = self.addLink('s14','h14',**linkHSParameters)
		lhs15 = self.addLink('s15','h15',**linkHSParameters)
		lhs16 = self.addLink('s16','h16',**linkHSParameters)
		lhs17 = self.addLink('s17','h17',**linkHSParameters)
		lhs18 = self.addLink('s18','h18',**linkHSParameters)
		lhs19 = self.addLink('s19','h19',**linkHSParameters)
		lhs20 = self.addLink('s20','h20',**linkHSParameters)
		lhs21 = self.addLink('s21','h21',**linkHSParameters)
		lhs22 = self.addLink('s22','h22',**linkHSParameters)
		lhs23 = self.addLink('s23','h23',**linkHSParameters)
		lhs24 = self.addLink('s24','h24',**linkHSParameters)
		lhs25 = self.addLink('s25','h25',**linkHSParameters)
		lhs26 = self.addLink('s26','h26',**linkHSParameters)
		lhs27 = self.addLink('s27','h27',**linkHSParameters)
		lhs28 = self.addLink('s28','h28',**linkHSParameters)
		lhs29 = self.addLink('s29','h29',**linkHSParameters)
		lhs30 = self.addLink('s30','h30',**linkHSParameters)
		lhs31 = self.addLink('s31','h31',**linkHSParameters)
		lhs32 = self.addLink('s32','h32',**linkHSParameters)
		lhs33 = self.addLink('s33','h33',**linkHSParameters)
		lhs34 = self.addLink('s34','h34',**linkHSParameters)
		lhs35 = self.addLink('s35','h35',**linkHSParameters)
		lhs36 = self.addLink('s36','h36',**linkHSParameters)
		lhs37 = self.addLink('s37','h37',**linkHSParameters)
		lhs38 = self.addLink('s38','h38',**linkHSParameters)
		lhs39 = self.addLink('s39','h39',**linkHSParameters)
		lhs40 = self.addLink('s40','h40',**linkHSParameters)
		lhs41 = self.addLink('s41','h41',**linkHSParameters)
		lhs42 = self.addLink('s42','h42',**linkHSParameters)
		lhs43 = self.addLink('s43','h43',**linkHSParameters)
		lhs44 = self.addLink('s44','h44',**linkHSParameters)
		lhs45 = self.addLink('s45','h45',**linkHSParameters)
		lhs46 = self.addLink('s46','h46',**linkHSParameters)
		lhs47 = self.addLink('s47','h47',**linkHSParameters)
		lhs48 = self.addLink('s48','h48',**linkHSParameters)
		lhs49 = self.addLink('s49','h49',**linkHSParameters)
		lhs50 = self.addLink('s50','h50',**linkHSParameters)
		lhs51 = self.addLink('s51','h51',**linkHSParameters)
		lhs52 = self.addLink('s52','h52',**linkHSParameters)
		lhs53 = self.addLink('s53','h53',**linkHSParameters)
		lhs54 = self.addLink('s54','h54',**linkHSParameters)
		lhs55 = self.addLink('s55','h55',**linkHSParameters)
		lhs56 = self.addLink('s56','h56',**linkHSParameters)
		lhs57 = self.addLink('s57','h57',**linkHSParameters)
		lhs58 = self.addLink('s58','h58',**linkHSParameters)
		lhs59 = self.addLink('s59','h59',**linkHSParameters)
		lhs60 = self.addLink('s60','h60',**linkHSParameters)
		lhs61 = self.addLink('s61','h61',**linkHSParameters)
		lhs62 = self.addLink('s62','h62',**linkHSParameters)
		lhs63 = self.addLink('s63','h63',**linkHSParameters)
		lhs64 = self.addLink('s64','h64',**linkHSParameters)
		lhs65 = self.addLink('s65','h65',**linkHSParameters)
		lhs66 = self.addLink('s66','h66',**linkHSParameters)
		lhs67 = self.addLink('s67','h67',**linkHSParameters)
		lhs68 = self.addLink('s68','h68',**linkHSParameters)
		lhs69 = self.addLink('s69','h69',**linkHSParameters)
		lhs70 = self.addLink('s70','h70',**linkHSParameters)
		lhs71 = self.addLink('s71','h71',**linkHSParameters)
		lhs72 = self.addLink('s72','h72',**linkHSParameters)
		lhs73 = self.addLink('s73','h73',**linkHSParameters)
		lhs74 = self.addLink('s74','h74',**linkHSParameters)
		lhs75 = self.addLink('s75','h75',**linkHSParameters)
		lhs76 = self.addLink('s76','h76',**linkHSParameters)
		lhs77 = self.addLink('s77','h77',**linkHSParameters)
		lhs78 = self.addLink('s78','h78',**linkHSParameters)
		lhs79 = self.addLink('s79','h79',**linkHSParameters)
		lhs80 = self.addLink('s80','h80',**linkHSParameters)
		lhs81 = self.addLink('s81','h81',**linkHSParameters)
		lhs82 = self.addLink('s82','h82',**linkHSParameters)
		lhs83 = self.addLink('s83','h83',**linkHSParameters)
		lhs84 = self.addLink('s84','h84',**linkHSParameters)
		lhs85 = self.addLink('s85','h85',**linkHSParameters)
		lhs86 = self.addLink('s86','h86',**linkHSParameters)
		lhs87 = self.addLink('s89','h87',**linkHSParameters)
		lhs88 = self.addLink('s90','h88',**linkHSParameters)
		lhs89 = self.addLink('s91','h89',**linkHSParameters)
		lhs90 = self.addLink('s92','h90',**linkHSParameters)
		lhs91 = self.addLink('s93','h91',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1',**linkSSParameters)
		lss1 = self.addLink('s0','s2',**linkSSParameters)
		lss2 = self.addLink('s1','s77',**linkSSParameters)
		lss3 = self.addLink('s2','s59',**linkSSParameters)
		lss4 = self.addLink('s3','s59',**linkSSParameters)
		lss5 = self.addLink('s3','s4',**linkSSParameters)
		lss6 = self.addLink('s4','s5',**linkSSParameters)
		lss7 = self.addLink('s5','s6',**linkSSParameters)
		lss8 = self.addLink('s6','s61',**linkSSParameters)
		lss9 = self.addLink('s7','s62',**linkSSParameters)
		lss10 = self.addLink('s7','s63',**linkSSParameters)
		lss11 = self.addLink('s8','s63',**linkSSParameters)
		lss12 = self.addLink('s8','s64',**linkSSParameters)
		lss13 = self.addLink('s9','s64',**linkSSParameters)
		lss14 = self.addLink('s9','s10',**linkSSParameters)
		lss15 = self.addLink('s10','s11',**linkSSParameters)
		lss16 = self.addLink('s12','s13',**linkSSParameters)
		lss17 = self.addLink('s13','s70',**linkSSParameters)
		lss18 = self.addLink('s14','s71',**linkSSParameters)
		lss19 = self.addLink('s14','s26',**linkSSParameters)
		lss20 = self.addLink('s15','s16',**linkSSParameters)
		lss21 = self.addLink('s15','s71',**linkSSParameters)
		lss22 = self.addLink('s16','s18',**linkSSParameters)
		lss23 = self.addLink('s17','s80',**linkSSParameters)
		lss24 = self.addLink('s18','s79',**linkSSParameters)
		lss25 = self.addLink('s19','s86',**linkSSParameters)
		lss26 = self.addLink('s19','s79',**linkSSParameters)
		lss27 = self.addLink('s20','s78',**linkSSParameters)
		lss28 = self.addLink('s20','s86',**linkSSParameters)
		lss29 = self.addLink('s21','s77',**linkSSParameters)
		lss30 = self.addLink('s21','s76',**linkSSParameters)
		lss31 = self.addLink('s22','s76',**linkSSParameters)
		lss32 = self.addLink('s22','s23',**linkSSParameters)
		lss33 = self.addLink('s23','s75',**linkSSParameters)
		lss34 = self.addLink('s24','s73',**linkSSParameters)
		lss35 = self.addLink('s24','s25',**linkSSParameters)
		lss36 = self.addLink('s25','s72',**linkSSParameters)
		lss37 = self.addLink('s26','s69',**linkSSParameters)
		lss38 = self.addLink('s27','s70',**linkSSParameters)
		lss39 = self.addLink('s27','s30',**linkSSParameters)
		lss40 = self.addLink('s28','s70',**linkSSParameters)
		lss41 = self.addLink('s28','s29',**linkSSParameters)
		lss42 = self.addLink('s29','s41',**linkSSParameters)
		lss43 = self.addLink('s30','s31',**linkSSParameters)
		lss44 = self.addLink('s31','s32',**linkSSParameters)
		lss45 = self.addLink('s32','s33',**linkSSParameters)
		lss46 = self.addLink('s33','s34',**linkSSParameters)
		lss47 = self.addLink('s34','s35',**linkSSParameters)
		lss48 = self.addLink('s36','s37',**linkSSParameters)
		lss49 = self.addLink('s36','s84',**linkSSParameters)
		lss50 = self.addLink('s37','s68',**linkSSParameters)
		lss51 = self.addLink('s38','s67',**linkSSParameters)
		lss52 = self.addLink('s38','s68',**linkSSParameters)
		lss53 = self.addLink('s39','s66',**linkSSParameters)
		lss54 = self.addLink('s39','s67',**linkSSParameters)
		lss55 = self.addLink('s40','s63',**linkSSParameters)
		lss56 = self.addLink('s40','s65',**linkSSParameters)
		lss57 = self.addLink('s41','s42',**linkSSParameters)
		lss58 = self.addLink('s42','s43',**linkSSParameters)
		lss59 = self.addLink('s43','s44',**linkSSParameters)
		lss60 = self.addLink('s44','s45',**linkSSParameters)
		lss61 = self.addLink('s45','s46',**linkSSParameters)
		lss62 = self.addLink('s46','s82',**linkSSParameters)
		lss63 = self.addLink('s47','s82',**linkSSParameters)
		lss64 = self.addLink('s47','s48',**linkSSParameters)
		lss65 = self.addLink('s48','s49',**linkSSParameters)
		lss66 = self.addLink('s49','s81',**linkSSParameters)
		lss67 = self.addLink('s50','s81',**linkSSParameters)
		lss68 = self.addLink('s50','s51',**linkSSParameters)
		lss69 = self.addLink('s51','s52',**linkSSParameters)
		lss70 = self.addLink('s53','s54',**linkSSParameters)
		lss71 = self.addLink('s54','s55',**linkSSParameters)
		lss72 = self.addLink('s55','s83',**linkSSParameters)
		lss73 = self.addLink('s56','s89',**linkSSParameters)
		lss74 = self.addLink('s56','s83',**linkSSParameters)
		lss75 = self.addLink('s57','s58',**linkSSParameters)
		lss76 = self.addLink('s57','s89',**linkSSParameters)
		lss77 = self.addLink('s58','s85',**linkSSParameters)
		lss78 = self.addLink('s60','s61',**linkSSParameters)
		lss79 = self.addLink('s60','s62',**linkSSParameters)
		lss80 = self.addLink('s65','s66',**linkSSParameters)
		lss81 = self.addLink('s66','s91',**linkSSParameters)
		lss82 = self.addLink('s69','s70',**linkSSParameters)
		lss83 = self.addLink('s73','s74',**linkSSParameters)
		lss84 = self.addLink('s74','s75',**linkSSParameters)
		lss85 = self.addLink('s77','s78',**linkSSParameters)
		lss86 = self.addLink('s79','s80',**linkSSParameters)
		lss87 = self.addLink('s84','s85',**linkSSParameters)
		lss88 = self.addLink('s90','s93',**linkSSParameters)
		lss89 = self.addLink('s91','s92',**linkSSParameters)
		lss90 = self.addLink('s92','s93',**linkSSParameters)
		
topos = { 'VtlWavenet2011': ( lambda: MininetNX() ) }