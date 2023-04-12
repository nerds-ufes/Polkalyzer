from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Add Switches
		s0 = self.addSwitch('s0')
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		#Add 2 hosts to each switch
		h0 = self.addHost('h0')
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0')
		lhs1 = self.addLink('s0','h1')
		lhs2 = self.addLink('s1','h2')
		lhs3 = self.addLink('s1','h3')
		lhs4 = self.addLink('s2','h4')
		lhs5 = self.addLink('s2','h5')
		lhs6 = self.addLink('s3','h6')
		lhs7 = self.addLink('s3','h7')
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1')
		lss1 = self.addLink('s0','s2')
		lss2 = self.addLink('s0','s3')
		lss3 = self.addLink('s1','s2')
		
topos = { 'Arpanet196912': ( lambda: MininetNX() ) }