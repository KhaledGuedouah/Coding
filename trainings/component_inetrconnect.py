# Interview preparation practice module.
# Contains algorithms and data structure exercises for coding interviews.

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# ─── Abstraction de base : tout est un Component ───
class Component(ABC):
    def __init__(self, name: str):
        self.name = name
        self._ports: dict[str, "Port"] = {}

    def add_port(self, port: "Port"):
        self._ports[port.name] = port

    def get_port(self, name: str) -> "Port":
        return self._ports[name]

    @abstractmethod
    def configure(self): ...

# ─── Ports et Interconnexions ───
@dataclass
class Port:
    name: str
    direction: str          # "in", "out", "inout"
    width: int = 1          # nombre de bits
    protocol: str = "wire"  # "AXI", "APB", "wire", "IRQ"

class Connection:
    """Relie deux ports entre eux"""
    def __init__(self, source: Port, sink: Port):
        assert source.direction in ("out", "inout")
        assert sink.direction in ("in", "inout")
        assert source.width == sink.width
        self.source = source
        self.sink = sink

    def __repr__(self):
        return f"{self.source.name} -> {self.sink.name}"

# ─── Composants concrets ───
class CPUCore(Component):
    def __init__(self, name: str, arch: str = "ARM_Cortex_A78"):
        super().__init__(name)
        self.arch = arch
        self.add_port(Port("axi_master", "out", width=64, protocol="AXI"))
        self.add_port(Port("irq_in", "in", width=1, protocol="IRQ"))

    def configure(self):
        print(f"[{self.name}] Configuring {self.arch} core")

class MemoryController(Component):
    def __init__(self, name: str, mem_type: str = "LPDDR5"):
        super().__init__(name)
        self.mem_type = mem_type
        self.add_port(Port("axi_slave", "in", width=64, protocol="AXI"))

    def configure(self):
        print(f"[{self.name}] Init {self.mem_type} controller")

class InterruptController(Component):
    def __init__(self, name: str, num_irqs: int = 256):
        super().__init__(name)
        self.add_port(Port("irq_out", "out", width=1, protocol="IRQ"))

    def configure(self):
        print(f"[{self.name}] Mapping IRQ lines")

# ─── Le SoC : composition de composants ───
class SoC:
    def __init__(self, name: str):
        self.name = name
        self.components: dict[str, Component] = {}
        self.connections: list[Connection] = []

    def add_component(self, comp: Component):
        self.components[comp.name] = comp

    def connect(self, src_comp: str, src_port: str,
                      dst_comp: str, dst_port: str):
        source = self.components[src_comp].get_port(src_port)
        sink = self.components[dst_comp].get_port(dst_port)
        self.connections.append(Connection(source, sink))

    def configure_all(self):
        for comp in self.components.values():
            comp.configure()

    def show_topology(self):
        print(f"=== {self.name} Topology ===")
        for conn in self.connections:
            print(f"  {conn}")

# ─── Utilisation ───
snapdragon = SoC("Snapdragon_8_Gen3")
snapdragon.add_component(CPUCore("cpu0"))
snapdragon.add_component(MemoryController("ddr_ctrl"))
snapdragon.add_component(InterruptController("gic"))

snapdragon.connect("cpu0", "axi_master", "ddr_ctrl", "axi_slave")
snapdragon.connect("gic", "irq_out", "cpu0", "irq_in")

snapdragon.configure_all()
snapdragon.show_topology()
