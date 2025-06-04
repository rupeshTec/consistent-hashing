import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas=100):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []
        self.nodes = set()

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        self.nodes.add(node)
        for i in range(self.replicas):
            virtual_node = f"{node}#{i}"
            key = self._hash(virtual_node)
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node):
        self.nodes.discard(node)
        for i in range(self.replicas):
            virtual_node = f"{node}#{i}"
            key = self._hash(virtual_node)
            if key in self.ring:
                del self.ring[key]
                index = bisect.bisect_left(self.sorted_keys, key)
                if index < len(self.sorted_keys) and self.sorted_keys[index] == key:
                    self.sorted_keys.pop(index)

    def get_node(self, key):
        if not self.ring:
            return None
        hash_val = self._hash(key)
        index = bisect.bisect(self.sorted_keys, hash_val) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[index]]
