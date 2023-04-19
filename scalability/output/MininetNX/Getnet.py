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
		#Add 1 hosts to each switch
		h0 = self.addHost('h0',**hostParameters)
		h1 = self.addHost('h1',**hostParameters)
		h2 = self.addHost('h2',**hostParameters)
		h3 = self.addHost('h3',**hostParameters)
		h4 = self.addHost('h4',**hostParameters)
		h5 = self.addHost('h5',**hostParameters)
		h6 = self.addHost('h6',**hostParameters)
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0',**linkHSParameters)
		lhs1 = self.addLink('s1','h1',**linkHSParameters)
		lhs2 = self.addLink('s2','h2',**linkHSParameters)
		lhs3 = self.addLink('s3','h3',**linkHSParameters)
		lhs4 = self.addLink('s4','h4',**linkHSParameters)
		lhs5 = self.addLink('s5','h5',**linkHSParameters)
		lhs6 = self.addLink('s6','h6',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1',**linkSSParameters)
		lss1 = self.addLink('s1','s2',**linkSSParameters)
		lss2 = self.addLink('s1','s4',**linkSSParameters)
		lss3 = self.addLink('s1','s6',**linkSSParameters)
		lss4 = self.addLink('s2','s3',**linkSSParameters)
		lss5 = self.addLink('s4','s5',**linkSSParameters)
		
topos = { 'Getnet': ( lambda: MininetNX() ) }