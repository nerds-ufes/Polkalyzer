from polka.tools import calculate_routeid, generate_nodeids

def to_TransmissionState(probeMatrix):
    o = []
    probe_state = []
    for probe in probeMatrix:
        for i in range(len(probe)):
            switch_state = [0] * len(probe)
            if i < len(probe) - 1:
                switch_state[i+1] = 1  # Ativar a porta para o próximo switch na probe
            probe_state.append(switch_state)
        o.append(probe_state)
    return o
